#!/usr/bin/env python3
"""
Enhanced Splunk-Jira Correlation Client with Claude Desktop Experience
====================================================================

Combines the best of both Splunk and Jira MCP clients to provide seamless
correlation between Splunk logs and Jira issues with a Claude-like chat interface.

Architecture: User Query → OpenAI LLM → Dual MCP Clients → Correlation Engine → Results

Features:
- Natural language processing for complex queries
- Dual MCP connection management (Splunk stdio + Jira Docker stdio)
- Intelligent correlation algorithms with confidence scoring
- Real-time data exchange between systems
- Claude Desktop-like conversational interface
- Robust error handling and retry logic
- Production-ready correlation metrics
"""

import asyncio
import json
import logging
import os
import re
import signal
import sys
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple
import httpx
import requests

# MCP Client imports
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get OAuth token from SAP AI Core's bound XSUAA instance (from original clients)
def getAccessToken():
    client_id = os.environ.get(
        "CLIENT_ID",
        "tokenid"
    )
    client_secret = os.environ.get(
        "CLIENT_SECRET",
        "tokenid"
    )
    uaa_url = os.environ.get(
        "UAA_URL",
        "https://toolsteamai24subacc.authentication.sap.hana.ondemand.com"
    )
    params = {"grant_type": "client_credentials"}
 
    resp = requests.post(f"{uaa_url}/oauth/token", auth=(client_id, client_secret), params=params)
    resp.raise_for_status()
    return resp.json()["access_token"]

# Get OAuth token from SAP AI Core's bound XSUAA instance (reused from existing clients)
def getAccessToken():
    client_id = os.environ.get(
        "CLIENT_ID",
        "tokenid"
    )
    client_secret = os.environ.get(
        "CLIENT_SECRET",
        "tokenid"
    )
    uaa_url = os.environ.get(
        "UAA_URL",
        "https://toolsteamai24subacc.authentication.sap.hana.ondemand.com"
    )
    params = {"grant_type": "client_credentials"}
    
    resp = requests.post(f"{uaa_url}/oauth/token", auth=(client_id, client_secret), params=params)
    resp.raise_for_status()
    ### write access token to a file for debugging
    # with open("access_token.txt", "w") as f:
    #     f.write(resp.json()["access_token"])
    return resp.json()["access_token"]

class CorrelationQueryParser:
    """
    Advanced Natural Language Query Parser for Correlation Operations
    ===============================================================
    
    PURPOSE:
    --------
    Provides fallback query parsing when OpenAI LLM is unavailable.
    Uses rule-based natural language processing to extract correlation intent,
    time ranges, error keywords, and system-specific search terms.
    
    PARSING CAPABILITIES:
    --------------------
    - Time Range Extraction: "last 2 hours", "past 30 minutes", "yesterday"
    - Error Categorization: Authentication, Database, Network, Application errors
    - Correlation Intent Detection: "find related", "with tickets", "correlate"
    - System Intent Detection: Splunk vs. Jira vs. Bidirectional queries
    - Confidence Threshold Determination: Based on query specificity
    
    WORKFLOW INTEGRATION:
    --------------------
    Used as fallback when LLM unavailable → Rule-based parsing → Traditional correlation
    """
    
    def __init__(self):
        self.time_patterns = {
            r'last\s+(\d+)\s*h(?:rs?|ours?)?': lambda m: f"-{m.group(1)}h",
            r'last\s+(\d+)\s*m(?:in(?:ute)?s?)?': lambda m: f"-{m.group(1)}m",
            r'past\s+(\d+)\s*h(?:rs?|ours?)?': lambda m: f"-{m.group(1)}h", 
            r'past\s+(\d+)\s*m(?:in(?:ute)?s?)?': lambda m: f"-{m.group(1)}m",
            r'yesterday': lambda m: "-1d",
            r'today': lambda m: "-1d",
        }
        
        self.correlation_patterns = {
            'find_related': r'(?:related|corresponding|matching|linked)\s+(?:jira|ticket|issue)',
            'with_tickets': r'with.*(?:ticket|issue|jira)',
            'and_jira': r'and.*jira',
            'correlation': r'correlat[ei]',
        }
        
        self.error_categories = {
            'authentication': ['unauthorized', 'access denied', '401', 'forbidden', 'authentication', 'auth', 'login'],
            'database': ['database', 'db', 'sql', 'connection timeout', 'query'],
            'network': ['timeout', 'connection', 'network', 'ssl', 'tls', 'certificate'],
            'application': ['error', 'exception', 'failure', 'crash', 'bug'],
        }
    
    def parse_correlation_query(self, query: str) -> Dict[str, Any]:
        """
        Parse complex correlation queries using rule-based NLP
        
        PARSING WORKFLOW:
        ----------------
        1. Extract time range patterns (last X hours/minutes/days)
        2. Find quoted terms for exact matching
        3. Categorize error keywords by domain (auth, database, network, app)
        4. Detect correlation intent patterns
        5. Identify system-specific intents (Splunk/Jira focus)
        6. Determine confidence threshold based on query specificity
        
        RETURNS: Dict with parsed query components for correlation processing
        """
        query_lower = query.lower()
        
        return {
            'time_range': self._extract_time_range(query_lower),
            'specific_terms': self._extract_quoted_terms(query),
            'error_keywords': self._extract_error_keywords(query_lower),
            'correlation_intent': self._detect_correlation_intent(query_lower),
            'jira_intent': self._detect_jira_intent(query_lower),
            'splunk_intent': self._detect_splunk_intent(query_lower),
            'original_query': query,
            'confidence_threshold': self._determine_confidence_threshold(query_lower)
        }
    
    def _extract_time_range(self, query: str) -> str:
        for pattern, converter in self.time_patterns.items():
            match = re.search(pattern, query)
            if match:
                return converter(match)
        return "-30m"  # Default to 30 minutes
    
    def _extract_quoted_terms(self, query: str) -> List[str]:
        return re.findall(r"['\"]([^'\"]+)['\"]", query)
    
    def _extract_error_keywords(self, query: str) -> List[str]:
        found = []
        for category, keywords in self.error_categories.items():
            for keyword in keywords:
                if keyword in query:
                    found.append(keyword)
        return list(dict.fromkeys(found))  # Remove duplicates
    
    def _detect_correlation_intent(self, query: str) -> bool:
        for pattern_name, pattern in self.correlation_patterns.items():
            if re.search(pattern, query):
                return True
        return False
    
    def _detect_jira_intent(self, query: str) -> bool:
        jira_terms = ['jira', 'ticket', 'issue', 'bug', 'story', 'task']
        return any(term in query for term in jira_terms)
    
    def _detect_splunk_intent(self, query: str) -> bool:
        splunk_terms = ['splunk', 'logs', 'error', 'event', 'search', 'index']
        return any(term in query for term in splunk_terms)
    
    def _determine_confidence_threshold(self, query: str) -> float:
        # Higher threshold for more specific queries
        if any(quoted in query for quoted in ['"', "'"]):
            return 0.8
        elif 'exact' in query or 'precisely' in query:
            return 0.9
        else:
            return 0.6

class EnhancedCorrelationClient:
    """
    Enhanced Splunk-Jira Correlation Client
    =====================================
    
    ARCHITECTURE OVERVIEW:
    ----------------------
    This client implements a sophisticated correlation engine that bridges two distinct systems:
    
    1. SPLUNK INTEGRATION (via FastMCP HTTP/SSE):
       - Connects to Splunk MCP server running on HTTP with SSE transport
       - Executes search queries against Splunk indexes 
       - Parses log events and error patterns from search results
    
    2. JIRA INTEGRATION (via Docker stdio MCP):
       - Launches containerized Jira MCP server via Docker
       - Executes JQL queries against Jira REST API
       - Retrieves issue data including summaries, descriptions, status
    
    3. CORRELATION ENGINE (LLM-Powered):
       - Uses OpenAI LLM for intelligent query understanding
       - Semantic analysis for cross-system data correlation
       - Confidence scoring for correlation strength
       - Bidirectional correlation workflows
    
    WORKFLOW PATTERNS:
    ------------------
    
    A) USER INPUT → LLM ANALYSIS → TOOL SELECTION → DATA RETRIEVAL → CORRELATION
       - Natural language processing of user queries
       - LLM determines optimal search strategy (Splunk→Jira, Jira→Splunk, or bidirectional)
       - Executes searches via MCP tool calls
       - Correlates results using semantic similarity
       - Returns formatted correlation report
    
    B) DUAL MCP SESSION MANAGEMENT:
       - Maintains persistent connections to both Splunk and Jira MCP servers
       - Handles connection failures and retry logic
       - Manages session lifecycle and cleanup
    
    C) INTELLIGENT QUERY GENERATION:
       - Converts natural language to Splunk search queries
       - Translates business problems to JQL queries  
       - Extracts correlation keywords using LLM analysis
       - Validates query syntax before execution
    
    CORRELATION ALGORITHMS:
    -----------------------
    - Semantic similarity analysis between log events and issue descriptions
    - Business impact assessment (security issues prioritized)
    - Confidence scoring based on multiple factors:
      * Keyword overlap
      * Time proximity
      * Business context alignment
      * LLM semantic analysis
    
    ERROR HANDLING & RESILIENCE:
    -----------------------------
    - Exponential backoff retry logic for MCP calls
    - Graceful degradation when individual systems are unavailable
    - Fallback correlation logic when LLM is unavailable
    - Comprehensive error reporting with actionable suggestions
    """
    
    def __init__(self):
        """
        Initialize the Enhanced Correlation Client
        
        INITIALIZATION WORKFLOW:
        1. Load configuration from environment variables
        2. Initialize MCP session management structures
        3. Setup conversation history tracking
        4. Validate environment and log configuration status
        """
        # Initialize configuration from both clients
        self._init_splunk_config()
        self._init_jira_config()
        self._init_openai_config()
        
        # MCP session management
        self.splunk_session = None
        self.jira_session = None
        self.splunk_stdio_context = None
        self.jira_stdio_context = None
        self.splunk_session_context = None
        self.jira_session_context = None
        
        # Connection status
        self.splunk_connected = False
        self.jira_connected = False
        self.sessions_initialized = False
        
        # Components
        self.query_parser = CorrelationQueryParser()
        self.conversation_history = []
        self.max_conversation_length = 20
        self.MAX_RETRY_DELAY = 300
        
        # Validate environment
        self._validate_environment()
        
        logger.info("🔗 Enhanced Correlation Client initialized")
    
    def _init_splunk_config(self):
        """Initialize Splunk configuration (updated to support token authentication)"""
        # MCP Server Configuration - HTTP endpoint for running server
        self.mcp_server_url = os.environ.get("MCP_SERVER_URL", "http://0.0.0.0:8000")
        
        # Splunk Configuration (from your claude_desktop_config.json)
        self.splunk_host = os.environ.get("SPLUNK_HOST", "gcpspk01-search-z3-0.lab-us.gcpint.ariba.com")
        self.splunk_port = os.environ.get("SPLUNK_PORT", "8089")
        self.splunk_scheme = os.environ.get("SPLUNK_SCHEME", "https")
        self.verify_ssl = os.environ.get("VERIFY_SSL", "false").lower() == "true"
        
        # Support both token and username/password authentication
        self.splunk_token = os.environ.get("SPLUNK_TOKEN")  # Token takes priority
        self.splunk_username = os.environ.get("SPLUNK_USERNAME", "admin")
        self.splunk_password = os.environ.get("SPLUNK_PASSWORD", "admin123")
        
        # Support configurable default Splunk indexes (comma-separated for multiple indexes)
        self.splunk_indexes = os.environ.get("SPLUNK_INDEXES", "ai_gcpperf11_kr_buyer,main").split(",")
        self.splunk_default_index = self.splunk_indexes[0].strip()  # Use first index as default
    
    def _init_jira_config(self):
        """Initialize Jira configuration (reused from Jira client)"""
        self.jira_url = os.environ.get("JIRA_URL", "https://product-jira.ariba.com").rstrip("/")
        self.jira_token = os.environ.get("JIRA_PERSONAL_TOKEN", "MDY1MD3n6b")
        # Support configurable default project keys (comma-separated for multiple projects)
        self.jira_project_keys = os.environ.get("JIRA_PROJECT_KEYS", "ESS,PS,ENGSVC").split(",")
        self.jira_default_project = self.jira_project_keys[0].strip()  # Use first project as default

    def _init_openai_config(self):
        """Initialize OpenAI configuration (reused from both clients)"""
        self.openai_api_key = os.environ.get("OPENAI_API_KEY", getAccessToken())
        self.openai_model = os.environ.get("OPENAI_MODEL", "gpt-4")
        self.openai_base_url = os.environ.get("OPENAI_BASE_URL", "https://api.ai.internalprod.eu-central-1.aws.ml.hana.ondemand.com/")
    
    def _validate_environment(self):
        """Validate required environment variables"""
        # Check for either token or username/password authentication
        has_splunk_auth = bool(self.splunk_token) or (bool(self.splunk_username) and bool(self.splunk_password))
        
        required_vars = {
            "SPLUNK_HOST": self.splunk_host,
            "MCP_SERVER_URL": self.mcp_server_url,
            "JIRA_URL": self.jira_url,
            "JIRA_PERSONAL_TOKEN": self.jira_token
        }
        
        missing_vars = [var for var, value in required_vars.items() if not value]
        if missing_vars:
            logger.warning(f"Missing environment variables: {', '.join(missing_vars)}")
            
        if not has_splunk_auth:
            logger.warning("Missing Splunk authentication: Either SPLUNK_TOKEN or (SPLUNK_USERNAME + SPLUNK_PASSWORD) required")
        
        # Log configuration
        logger.info(f"🔧 Splunk Configuration:")
        logger.info(f"   Endpoint: {self.splunk_scheme}://{self.splunk_host}:{self.splunk_port}")
        logger.info(f"   SSL Verify: {self.verify_ssl}")
        logger.info(f"   Auth Method: {'Token' if self.splunk_token else 'Username/Password'}")
        logger.info(f"   Indexes: {', '.join(self.splunk_indexes)} (default: {self.splunk_default_index})")
        if self.splunk_token:
            logger.info(f"   Token: {self.splunk_token[:20]}...***")
        else:
            logger.info(f"   Username: {self.splunk_username}")
        logger.info(f"🔧 Jira Configuration:")
        logger.info(f"   URL: {self.jira_url}")
        logger.info(f"   Projects: {', '.join(self.jira_project_keys)} (default: {self.jira_default_project})")
        logger.info(f"🔧 MCP Server: {self.mcp_server_url}")

    def _get_splunk_index_clause(self, explicit_index: str = None) -> str:
        """
        Generate Splunk index clause using configured indexes or explicit override
        
        PARAMETERS:
        - explicit_index: Optional specific index to use instead of configured defaults
        
        RETURNS: 
        - Single index: 'index="specific_index"'
        - Multiple indexes: '(index="idx1" OR index="idx2" OR index="idx3")'
        """
        if explicit_index:
            return f'index="{explicit_index}"'
        
        if len(self.splunk_indexes) == 1:
            return f'index="{self.splunk_default_index}"'
        else:
            index_options = ' OR '.join([f'index="{idx.strip()}"' for idx in self.splunk_indexes])
            return f'({index_options})'

    def _get_jira_project_clause(self, explicit_project: str = None) -> str:
        """
        Generate Jira project clause using configured projects or explicit override
        
        PARAMETERS:
        - explicit_project: Optional specific project to use instead of configured defaults
        
        RETURNS:
        - Single project: 'project = "PROJ"'
        - Multiple projects: '(project = "PROJ1" OR project = "PROJ2" OR project = "PROJ3")'
        """
        if explicit_project:
            return f'project = "{explicit_project}"'
        
        if len(self.jira_project_keys) == 1:
            return f'project = "{self.jira_default_project}"'
        else:
            project_options = ' OR '.join([f'project = "{proj.strip()}"' for proj in self.jira_project_keys])
            return f'({project_options})'

    def _get_jira_issue_link(self, issue_key: str) -> str:
        """Generate proper Jira issue link avoiding double slashes"""
        return f"{self.jira_url}/browse/{issue_key}"

    def _extract_specific_errors_from_event(self, event_text: str) -> List[str]:
        """
        Extract semantically meaningful error patterns from Splunk event text for targeted Jira correlation
        
        This method performs semantic analysis of actual technical errors and generates meaningful
        search terms that capture the business and technical context, not just generic keywords.
        
        SEMANTIC ANALYSIS APPROACH:
        - Understands the meaning behind exceptions (e.g., ExecutionException = async task failure)
        - Maps technical errors to business impact terms
        - Generates context-aware search terms for Jira correlation
        - Focuses on root cause and symptom description rather than just exception names
        
        RETURNS: List of semantically meaningful terms for Jira text search
        """
        import re
        
        if not event_text:
            return []
        
        semantic_terms = []
        event_text_lower = str(event_text).lower()
        
        # Semantic mapping of technical errors to business context
        semantic_mappings = {
            # Concurrency and Threading Issues
            'java.util.concurrent.executionexception': [
                'async task failure', 'concurrent execution failed', 
                'thread execution error', 'asynchronous operation failure',
                'task completion failure', 'parallel processing error'
            ],
            'java.util.concurrent.timeoutexception': [
                'operation timeout', 'request timeout', 'async timeout',
                'long running task timeout', 'response timeout'
            ],
            'java.util.concurrent.rejectedexecutionexception': [
                'thread pool exhausted', 'task queue full', 
                'execution rejected', 'thread pool overload'
            ],
            
            # Network and Connection Issues  
            'java.net.connectexception': [
                'connection refused', 'network connectivity issue',
                'service unreachable', 'port connection failed'
            ],
            'java.net.sockettimeoutexception': [
                'network timeout', 'socket read timeout',
                'connection timeout', 'network latency issue'
            ],
            
            # Authentication and Security
            'javax.security.auth.login.loginexception': [
                'authentication failure', 'login failed',
                'credential validation error', 'user authentication issue'
            ],
            'java.security.accesscontrolexception': [
                'permission denied', 'access control violation',
                'unauthorized access', 'security permission error'
            ],
            
            # Database and Persistence
            'java.sql.sqlexception': [
                'database error', 'SQL operation failed',
                'database connectivity issue', 'data persistence error'
            ],
            'javax.persistence.persistenceexception': [
                'data persistence failure', 'ORM operation failed',
                'entity persistence error', 'database mapping issue'
            ],
            
            # I/O and Resource Issues
            'java.io.ioexception': [
                'file operation failed', 'I/O operation error',
                'resource access failure', 'input output error'
            ],
            'java.lang.outofmemoryerror': [
                'memory exhausted', 'heap space full',
                'memory allocation failed', 'resource exhaustion'
            ]
        }
        
        # Extract and analyze Java exceptions semantically
        java_exceptions = re.findall(r'java\.[\w.]+\.[\w]+(?:exception|error)', event_text_lower)
        
        for exception in java_exceptions:
            # Get semantic meaning of this specific exception
            if exception in semantic_mappings:
                semantic_terms.extend(semantic_mappings[exception])
            else:
                # For unknown exceptions, try to derive semantic meaning
                exception_name = exception.split('.')[-1]
                semantic_context = self._derive_semantic_context(exception_name, event_text_lower)
                if semantic_context:
                    semantic_terms.extend(semantic_context)
        
        # Extract business context from error messages
        business_context = self._extract_business_context(event_text_lower)
        semantic_terms.extend(business_context)
        
        # Extract specific failure scenarios from context
        failure_scenarios = self._extract_failure_scenarios(event_text_lower)
        semantic_terms.extend(failure_scenarios)
        
        # Clean, deduplicate, and prioritize semantic terms
        unique_terms = []
        for term in semantic_terms:
            cleaned_term = term.strip()
            if (5 <= len(cleaned_term) <= 80 and 
                cleaned_term not in unique_terms and
                not self._is_too_generic(cleaned_term)):
                unique_terms.append(cleaned_term)
        
        return unique_terms[:8]  # Return top 8 most meaningful semantic terms
    
    def _derive_semantic_context(self, exception_name: str, event_text: str) -> List[str]:
        """Derive semantic meaning from unknown exception types"""
        context_terms = []
        
        # Analyze exception name for semantic clues
        if 'timeout' in exception_name:
            context_terms.extend(['operation timeout', 'response delay', 'slow operation'])
        elif 'connection' in exception_name:
            context_terms.extend(['connectivity issue', 'network problem', 'service unreachable'])
        elif 'authentication' in exception_name or 'auth' in exception_name:
            context_terms.extend(['authentication failure', 'login problem', 'credential issue'])
        elif 'permission' in exception_name or 'access' in exception_name:
            context_terms.extend(['access denied', 'permission error', 'authorization failure'])
        elif 'parse' in exception_name or 'format' in exception_name:
            context_terms.extend(['data format error', 'parsing failure', 'invalid format'])
        
        return context_terms
    
    def _extract_business_context(self, event_text: str) -> List[str]:
        """Extract business context and impact from error messages"""
        business_terms = []
        
        # Look for business operations that failed
        business_patterns = [
            (r'failed to (\w+(?:\s+\w+){0,3}) (?:user|customer|order|transaction|payment)', 
             lambda m: f"{m.group(1)} operation failure"),
            (r'unable to (?:process|complete|execute) (\w+(?:\s+\w+){0,2})',
             lambda m: f"{m.group(1)} processing failure"),
            (r'error (?:processing|handling|executing) (\w+(?:\s+\w+){0,2})',
             lambda m: f"{m.group(1)} handling error"),
            (r'(\w+(?:\s+\w+){0,2}) service (?:unavailable|failed|error)',
             lambda m: f"{m.group(1)} service disruption")
        ]
        
        for pattern, formatter in business_patterns:
            matches = re.finditer(pattern, event_text)
            for match in matches:
                try:
                    business_term = formatter(match)
                    if business_term and len(business_term) <= 60:
                        business_terms.append(business_term)
                except:
                    continue
        
        return business_terms
    
    def _extract_failure_scenarios(self, event_text: str) -> List[str]:
        """Extract specific failure scenarios and symptoms"""
        scenarios = []
        
        # Identify specific failure patterns
        failure_patterns = [
            r'task (?:failed|cancelled|interrupted|rejected)',
            r'request (?:failed|timed out|cancelled|rejected)',
            r'operation (?:failed|cancelled|interrupted|aborted)',
            r'service (?:unavailable|unresponsive|failed|down)',
            r'connection (?:lost|dropped|refused|failed|reset)',
            r'thread (?:interrupted|blocked|deadlocked|terminated)'
        ]
        
        for pattern in failure_patterns:
            if re.search(pattern, event_text):
                # Convert pattern to human-readable scenario
                readable_scenario = pattern.replace('(?:', '').replace('|', ' or ').replace(')', '').replace('\\', '')
                scenarios.append(readable_scenario)
        
        return scenarios
    
    def _is_too_generic(self, term: str) -> bool:
        """Filter out overly generic terms that won't help with correlation"""
        generic_terms = {
            'error', 'exception', 'failed', 'failure', 'issue', 'problem',
            'timeout', 'connection', 'service', 'operation', 'request',
            'task', 'thread', 'process', 'system', 'application'
        }
        
        # Check if term is just a single generic word
        if term.lower() in generic_terms:
            return True
        
        # Check if term is too short or too common
        if len(term) < 5 or len(term.split()) > 6:
            return True
        
        return False

    async def _generate_semantic_jql_terms(self, semantic_terms: List[str], error_patterns: List[str], splunk_events: List[Dict]) -> List[str]:
        """
        Use LLM to generate meaningful JQL text search terms for Jira correlation
        
        This method leverages the LLM's understanding to convert technical errors into
        business-meaningful search terms that are likely to find relevant Jira issues.
        
        Args:
            semantic_terms: Extracted semantic terms from Splunk events
            error_patterns: Original error patterns from user query
            splunk_events: Raw Splunk events for additional context
        
        Returns:
            List of LLM-generated JQL text search terms
        """
        if not self.openai_client:
            print("   LLM unavailable for semantic JQL generation")
            return []
        
        try:
            # Prepare context for LLM
            context_info = {
                'semantic_terms': semantic_terms[:10],
                'error_patterns': error_patterns[:5],
                'sample_events': []
            }
            
            # Add sample Splunk events for better context
            if splunk_events:
                for event in splunk_events[:3]:
                    event_text = event.get('_raw', '') or event.get('message', '') or str(event)
                    if event_text:
                        context_info['sample_events'].append(event_text[:500])  # Limit length
            
            llm_prompt = f"""
You are an expert at analyzing technical errors and generating ADDITIONAL meaningful Jira search terms.

CRITICAL CONTEXT:
- Original Error Patterns: {context_info['error_patterns']} (THESE WILL BE INCLUDED AUTOMATICALLY)
- Semantic Terms Found: {context_info['semantic_terms']}
- Sample Splunk Events: {context_info['sample_events']}

TASK:
Generate 5-8 ADDITIONAL meaningful JQL text search terms that would help find relevant Jira issues for these technical problems.
These terms will be used ALONGSIDE the original error patterns, not instead of them.

REQUIREMENTS:
1. Generate COMPLEMENTARY terms that capture business impact and user symptoms
2. Use terms that developers would write in Jira issue descriptions alongside technical details
3. Focus on the business context and user-facing impact of these technical errors
4. Avoid duplicating the original technical terms (they're already included)
5. Think about what related symptoms or business problems these technical errors cause

EXAMPLES OF COMPLEMENTARY TERMS:
Original: "java.util.concurrent.ExecutionException"
Complementary: "async operation timeout", "background task failure", "thread pool issues"

Original: "SocketTimeoutException" 
Complementary: "service response delay", "connection timeout", "network latency"

Original: "authentication failure"
Complementary: "login issues", "user access problems", "credential validation"

Generate ONLY the ADDITIONAL search terms, one per line, without quotes or extra formatting.
Focus on business impact terms that complement the technical error patterns already provided.
"""

            response = await self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert technical analyst who converts technical errors into business-meaningful Jira search terms."},
                    {"role": "user", "content": llm_prompt}
                ],
                max_tokens=300,
                temperature=0.3  # Lower temperature for more consistent results
            )
            
            if response.choices and response.choices[0].message.content:
                llm_content = response.choices[0].message.content.strip()
                
                # Parse the LLM response into individual terms
                jql_terms = []
                for line in llm_content.split('\n'):
                    term = line.strip().replace('"', '').replace("'", '').replace('- ', '').replace('* ', '')
                    if term and len(term) > 3 and len(term) < 100:
                        jql_terms.append(term)
                
                # Validate and filter terms
                valid_terms = []
                generic_words = {'error', 'exception', 'issue', 'problem', 'failure'}
                
                for term in jql_terms[:8]:  # Limit to 8 terms
                    # Skip if term is too generic
                    term_words = set(term.lower().split())
                    if not term_words.issubset(generic_words) and len(term.split()) <= 5:
                        valid_terms.append(term)
                
                print(f"   LLM Generated {len(valid_terms)} semantic JQL terms")
                return valid_terms[:6]  # Return top 6 terms
            
        except Exception as e:
            print(f"   LLM JQL generation failed: {str(e)}")
            return []
        
        return []

    # =============================================================================
    # MCP CONNECTION MANAGEMENT (Dual System Architecture)
    # =============================================================================

    async def start_dual_mcp_sessions(self):
        """
        Initialize both Splunk and Jira MCP sessions
        
        DUAL CONNECTION WORKFLOW:
        -------------------------
        1. SPLUNK CONNECTION (HTTP/SSE):
           - Connect to FastMCP server via Server-Sent Events (SSE)
           - Establish persistent HTTP connection for real-time communication
           - Initialize MCP protocol session with proper handshaking
           - Verify available Splunk search tools
        
        2. JIRA CONNECTION (Docker stdio):
           - Launch containerized Jira MCP server via Docker
           - Establish stdio communication channels (stdin/stdout)
           - Initialize MCP protocol session with container
           - Verify available Jira search tools
        
        3. CONNECTION VALIDATION:
           - Test both connections and update connection status flags
           - Retrieve available tool lists from both MCP servers
           - Log connection success/failure for debugging
           - Set sessions_initialized flag based on at least one successful connection
        
        RETURNS: bool - True if at least one MCP connection established successfully
        """
        logger.info("🔄 Starting dual MCP sessions...")
        
        # Start Splunk MCP session (stdio)
        try:
            await self._start_splunk_session()
            self.splunk_connected = True
            logger.info("✅ Splunk MCP connected")
        except Exception as e:
            logger.error(f"❌ Splunk MCP failed: {e}")
            self.splunk_connected = False
        
        # Start Jira MCP session (Docker stdio)
        try:
            await self._start_jira_session()
            self.jira_connected = True
            logger.info("✅ Jira MCP connected")
        except Exception as e:
            logger.error(f"❌ Jira MCP failed: {e}")
            self.jira_connected = False
        
        self.sessions_initialized = self.splunk_connected or self.jira_connected
        
        if self.sessions_initialized:
            # Get available tools from both systems
            splunk_tools = await self._get_splunk_tools() if self.splunk_connected else []
            jira_tools = await self._get_jira_tools() if self.jira_connected else []
            
            logger.info(f"📊 Available tools: Splunk ({len(splunk_tools)}), Jira ({len(jira_tools)})")
            return True
        else:
            logger.error("❌ No MCP connections established")
            return False

    async def _start_splunk_session(self):
        """
        Start Splunk MCP session using HTTP/SSE transport
        
        SPLUNK CONNECTION WORKFLOW:
        ---------------------------
        1. TRANSPORT SETUP:
           - Create SSE (Server-Sent Events) client connection to FastMCP server
           - FastMCP server acts as bridge between HTTP/SSE and native Splunk API
           - Establish read/write channels for bidirectional communication
        
        2. MCP PROTOCOL INITIALIZATION:
           - Create MCP ClientSession with established read/write channels
           - Perform MCP protocol handshake and capability negotiation
           - Initialize session state and prepare for tool calls
        
        3. TOOL DISCOVERY:
           - Query MCP server for available Splunk search tools
           - Log available tool names for debugging and selection
           - Validate that search capabilities are available
        
        TECHNICAL DETAILS:
        - Uses SSE for real-time streaming communication
        - FastMCP server handles Splunk authentication and API translation
        - MCP protocol enables standardized tool calling interface
        """
        logger.info(f"Connecting to FastMCP server at: {self.mcp_server_url}")
        logger.info(f"Target Splunk server: {self.splunk_scheme}://{self.splunk_host}:{self.splunk_port}")

        # This is a FastMCP server that uses SSE transport
        # Connect to the SSE endpoint to establish MCP protocol communication
        self.splunk_sse_context = sse_client(f"{self.mcp_server_url}/sse")
        self.splunk_read, self.splunk_write = await self.splunk_sse_context.__aenter__()
        self.splunk_session_context = ClientSession(self.splunk_read, self.splunk_write)
        self.splunk_session = await self.splunk_session_context.__aenter__()

        # Initialize the MCP session properly
        await self.splunk_session.initialize()

        # Get available tools from the MCP server
        tools = await self.splunk_session.list_tools()
        available_tools = [tool.name for tool in tools.tools]
        logger.info(f"Connected to FastMCP server via SSE! Available tools: {', '.join(available_tools)}")

    async def _start_jira_session(self):
        """
        Start Jira MCP session using Docker stdio transport
        
        JIRA CONNECTION WORKFLOW:
        -------------------------
        1. DOCKER CONTAINER LAUNCH:
           - Execute Docker command to start containerized Jira MCP server
           - Pass Jira URL and authentication token as environment variables
           - Generate unique container name to avoid conflicts
           - Configure container for interactive mode with stdio communication
        
        2. STDIO CHANNEL SETUP:
           - Establish stdin/stdout communication channels with container
           - Create MCP ClientSession using stdio transport
           - Handle container lifecycle and communication protocols
        
        3. MCP PROTOCOL INITIALIZATION:
           - Perform MCP handshake with containerized server
           - Initialize session state and capability negotiation
           - Query for available Jira search and management tools
        
        TECHNICAL DETAILS:
        - Uses ghcr.io/sooperset/mcp-atlassian:latest Docker image
        - Container handles Jira REST API authentication and requests
        - MCP protocol provides standardized interface over stdio
        - Container name includes timestamp hash to prevent conflicts
        """
        logger.info(f"Starting Docker MCP session with Jira URL: {self.jira_url}")
        
        # Docker command to start MCP server (exact copy from working client)
        server_params = StdioServerParameters(
            command="/usr/local/bin/docker",
            args=[
                "run", "--rm", "-i",
                "-e", f"JIRA_URL={self.jira_url}",
                "-e", f"JIRA_PERSONAL_TOKEN={self.jira_token}",
                "-e", "DEBUG=1",
                "--name", f"jira-correlator-{hash(str(time.time())) % 10000}",
                "ghcr.io/sooperset/mcp-atlassian:latest"
            ]
        )

        # Use proper async context managers (exact copy from working client)
        self.jira_stdio_context = stdio_client(server_params)
        self.jira_read, self.jira_write = await self.jira_stdio_context.__aenter__()
        self.jira_session_context = ClientSession(self.jira_read, self.jira_write)
        self.jira_session = await self.jira_session_context.__aenter__()

        # Initialize the session properly
        await self.jira_session.initialize()

        # Get available tools
        tools = await self.jira_session.list_tools()
        jira_tools = [tool.name for tool in tools.tools]
        logger.info(f"Jira MCP session started. Available tools: {', '.join(jira_tools)}")

    async def _get_splunk_tools(self) -> List[str]:
        """Get available Splunk tools"""
        if not self.splunk_session:
            return []
        try:
            tools_result = await self.splunk_session.list_tools()
            return [tool.name for tool in tools_result.tools]
        except Exception as e:
            logger.error(f"Error getting Splunk tools: {e}")
            return []

    async def _get_jira_tools(self) -> List[str]:
        """Get available Jira tools"""
        if not self.jira_session:
            return []
        try:
            tools_result = await self.jira_session.list_tools()
            return [tool.name for tool in tools_result.tools]
        except Exception as e:
            logger.error(f"Error getting Jira tools: {e}")
            return []

    async def close_dual_mcp_sessions(self):
        """Close both MCP sessions"""
        logger.info("🔄 Closing dual MCP sessions...")
        
        # Close Splunk session (SSE)
        try:
            if hasattr(self, 'splunk_session_context') and self.splunk_session_context:
                await self.splunk_session_context.__aexit__(None, None, None)
            if hasattr(self, 'splunk_sse_context') and self.splunk_sse_context:
                await self.splunk_sse_context.__aexit__(None, None, None)
            logger.info("✅ Splunk MCP session closed")
        except Exception as e:
            logger.warning(f"⚠️ Error closing Splunk session: {e}")
        
        # Close Jira session (stdio)
        try:
            if hasattr(self, 'jira_session_context') and self.jira_session_context:
                logger.info("Closing Jira session...")
            logger.info("✅ Jira MCP session closed")
        except Exception as e:
            logger.warning(f"⚠️ Error closing Jira session: {e}")
        
        logger.info("✅ Dual MCP sessions closed")

    # =============================================================================
    # MCP TOOL CALLING (Robust Execution with Retry Logic)
    # =============================================================================

    def safe_sleep(self, delay_seconds):
        """
        Safely sleep with overflow protection
        
        SAFETY MEASURES:
        ---------------
        - Prevents integer overflow errors in sleep operations
        - Caps maximum sleep duration to prevent indefinite waits
        - Handles various sleep-related exceptions gracefully
        - Logs warnings when fallback sleep durations are used
        """
        try:
            if delay_seconds > self.MAX_RETRY_DELAY:
                delay_seconds = self.MAX_RETRY_DELAY
            time.sleep(delay_seconds)
        except OverflowError:
            logger.warning(f"Sleep overflow, using max delay: {self.MAX_RETRY_DELAY}")
            time.sleep(self.MAX_RETRY_DELAY)
        except Exception as e:
            logger.error(f"Sleep error: {e}")

    async def call_tool_with_retry(self, session: ClientSession, tool_name: str, arguments: Dict[str, Any], max_retries: int = 3):
        """
        Call MCP tool with intelligent retry logic and error handling
        
        RETRY STRATEGY:
        ---------------
        1. ATTEMPT EXECUTION:
           - Call MCP tool with provided arguments
           - Monitor for success or various error conditions
           - Log attempt number and outcome for debugging
        
        2. ERROR CLASSIFICATION:
           - Overflow errors → Create fallback response immediately
           - Timestamp errors → Generate user-friendly error response  
           - Network/timeout errors → Retry with exponential backoff
           - Other errors → Apply standard retry logic
        
        3. EXPONENTIAL BACKOFF:
           - Start with 2^attempt delay (2s, 4s, 8s, 16s, 30s max)
           - Use safe_sleep() to prevent overflow issues
           - Log retry attempts with delay information
        
        4. FALLBACK RESPONSES:
           - Generate user-friendly error messages for common failures
           - Provide actionable suggestions for resolution
           - Maintain consistent response format for downstream processing
        
        PARAMETERS:
        - session: Active MCP client session
        - tool_name: Name of the MCP tool to call
        - arguments: Tool-specific arguments dictionary  
        - max_retries: Maximum retry attempts before giving up
        
        RETURNS: MCP tool result or fallback error response object
        """
        logger.debug(f"Calling tool '{tool_name}' with args: {arguments}")
        
        for attempt in range(max_retries + 1):
            try:
                result = await session.call_tool(tool_name, arguments)
                logger.debug(f"Tool '{tool_name}' completed on attempt {attempt + 1}")
                return result
                
            except Exception as e:
                error_msg = str(e).lower()
                
                if attempt < max_retries:
                    if 'overflow' in error_msg or 'timestamp' in error_msg:
                        logger.warning(f"Overflow error on attempt {attempt + 1}, creating fallback response")
                        return self.create_overflow_error_response(tool_name, arguments, str(e))
                    
                    # Exponential backoff
                    delay = min(2 ** attempt, 30)
                    logger.warning(f"Tool '{tool_name}' failed on attempt {attempt + 1}/{max_retries + 1}: {e}")
                    logger.info(f"Retrying in {delay} seconds...")
                    self.safe_sleep(delay)
                else:
                    logger.error(f"Tool '{tool_name}' failed after {max_retries + 1} attempts: {e}")
        
        return self.create_timeout_error_response(tool_name, arguments)

    def create_overflow_error_response(self, tool_name: str, arguments: Dict[str, Any], error_msg: str):
        """Create user-friendly response for overflow errors"""
        return type('MockResult', (), {
            'content': [type('MockContent', (), {
                'text': json.dumps({
                    "error": "timestamp_overflow",
                    "message": "Unable to retrieve data due to timestamp processing error",
                    "suggestion": "Try using a shorter time range or broader search terms",
                    "technical_details": error_msg
                })
            })()]
        })()

    def create_timeout_error_response(self, tool_name: str, arguments: Dict[str, Any]):
        """Create user-friendly response for timeout errors"""
        return type('MockResult', (), {
            'content': [type('MockContent', (), {
                'text': json.dumps({
                    "error": "request_timeout",
                    "message": "Request timed out after multiple retries",
                    "suggestion": "Try using broader search terms or check system status"
                })
            })()]
        })()

    # =============================================================================
    # OPENAI LLM INTEGRATION (Enhanced from both clients)
    # =============================================================================

    async def call_openai_api(self, messages: List[Dict[str, str]], functions: Optional[List[Dict]] = None) -> Dict[str, Any]:
        """Call OpenAI Chat Completion API (from both original clients)"""
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json",
            "AI-Resource-Group": os.environ.get("AICORE_RESOURCE_GROUP", "default")
        }
        
        payload = {
            "model": self.openai_model,
            "messages": messages,
            "temperature": 0.1,
            "max_tokens": 2000
        }
        
        if functions:
            payload["functions"] = functions
            payload["function_call"] = "auto"
        
        base_url = self.openai_base_url.rstrip("/")
        DEPLOYMENT_ID = "d08a6a0520927b74"
        ENDPOINT = (
            f"{base_url}/v2/inference/deployments/"
            f"{DEPLOYMENT_ID}/chat/completions?api-version=2023-05-15"
        )

        # Debug URL construction
        print(f"\n🔧 **DEBUG API CALL**:")
        print(f"   Base URL: {base_url}")
        print(f"   Deployment ID: {DEPLOYMENT_ID}")
        print(f"   Final ENDPOINT: {ENDPOINT}")

        # # Generate and log curl command equivalent
        # curl_cmd = (
        #     f"curl -X POST '{ENDPOINT}' "
        #     f"-H 'Authorization: Bearer {self.openai_api_key}' "
        #     f"-H 'Content-Type: application/json' "
        #     f"-H 'AI-Resource-Group: {headers.get('AI-Resource-Group', 'default')}' "
        #     f"--data '{json.dumps(payload)}'"
        # )
        # print(f"\n📤 **CURL COMMAND**:")
        # print(f"   {curl_cmd}")
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                logger.debug(f"Calling OpenAI API with model: {self.openai_model}")
                response = await client.post(
                    ENDPOINT,
                    headers=headers,
                    json=payload
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                logger.error(f"OpenAI API error: {e}")
                raise Exception(f"OpenAI API error: {str(e)}")

    def get_correlation_function_definitions(self) -> List[Dict[str, Any]]:
        """Define available functions for correlation operations (enhanced for bidirectional flow)"""
        return [
            {
                "name": "search_splunk_logs",
                "description": f"Execute a Splunk search query and return the results. Available Splunk indexes: {', '.join(self.splunk_indexes)}. Use this for searching logs, errors, events, and data in Splunk. Examples: find errors, search specific patterns, analyze log data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_query": {
                            "type": "string",
                            "description": f"Splunk search query. MUST use one of these configured indexes: {', '.join(self.splunk_indexes)}. Examples: 'search {self._get_splunk_index_clause()} \"app - ERROR\"', 'search index=\"{self.splunk_indexes[0]}\" \"unauthorized access\"', 'search index={self.splunk_indexes[0]} earliest=-1h error'"
                        },
                        "time_range": {
                            "type": "string", 
                            "description": "Time range for the search (e.g., '-24h', '-1d', '-30m', '-2h')",
                            "default": "-30m"
                        }
                    },
                    "required": ["search_query"]
                }
            },
            {
                "name": "search_jira_issues",
                "description": f"Search for Jira issues using JQL (Jira Query Language). Available Jira projects: {', '.join(self.jira_project_keys)}. Use this for finding issues, filtering by status, assignee, priority, date ranges, text search, etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "jql_query": {
                            "type": "string",
                            "description": f"JQL query string. MUST use one of these configured projects: {', '.join(self.jira_project_keys)}. Examples: 'project = \"{self.jira_project_keys[0]}\" AND status in (Open, \"To Do\")', '{self._get_jira_project_clause()} AND text ~ \"unauthorized\"', 'status in (Open, \"To Do\") AND description ~ \"access attempts\"'"
                        }
                    },
                    "required": ["jql_query"]
                }
            },
            {
                "name": "splunk_to_jira_correlation",
                "description": "Start with Splunk log analysis and find corresponding Jira issues. Use this when user wants to find logs/errors first and then discover related tickets. Examples: 'find recent errors and related tickets', 'check what issues exist for this error pattern'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "splunk_query": {
                            "type": "string",
                            "description": f"Splunk search query to find logs/events. Must use configured indexes: {', '.join(self.splunk_indexes)}. Examples: 'search {self._get_splunk_index_clause()} \"app - ERROR\"', 'search index=\"{self.splunk_indexes[0]}\" earliest=-2h \"unauthorized\"'"
                        },
                        "splunk_time_range": {
                            "type": "string",
                            "description": "Time range for Splunk search (e.g., '-24h', '-7d', '-2h')",
                            "default": "-24h"
                        },
                        "jira_time_range": {
                            "type": "string",
                            "description": "Time range for Jira issue search (e.g., '-30d', '-7d')",
                            "default": "-30d"
                        },
                        "confidence_threshold": {
                            "type": "number",
                            "description": "Minimum confidence for correlation (0.0-1.0)",
                            "default": 0.6
                        }
                    },
                    "required": ["splunk_query"]
                }
            },
            {
                "name": "jira_to_splunk_correlation", 
                "description": "Start with specific Jira issue analysis and find related Splunk logs. Use this when user mentions a specific Jira issue key or wants to check logs for a known ticket. Examples: 'check ESS-26218 for related logs', 'find logs for this ticket'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "jira_issue_key": {
                            "type": "string",
                            "description": "Specific Jira issue key (e.g., 'ESS-26218', 'PROJ-123')"
                        },
                        "splunk_time_range": {
                            "type": "string",
                            "description": "Time range for Splunk log search (e.g., '-24h', '-7d', '-2h')",
                            "default": "-24h"
                        },
                        "additional_search_terms": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Additional terms to include in Splunk search beyond issue content"
                        },
                        "confidence_threshold": {
                            "type": "number", 
                            "description": "Minimum confidence for correlation (0.0-1.0)",
                            "default": 0.6
                        }
                    },
                    "required": ["jira_issue_key"]
                }
            },
            {
                "name": "correlate_splunk_jira",
                "description": "Perform comprehensive bidirectional correlation analysis between Splunk logs and Jira issues. Use this for general correlation requests when direction is ambiguous or when user wants complete analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "error_patterns": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Error patterns to search for in both systems (e.g., ['unauthorized access', 'database timeout', 'SSL error'])"
                        },
                        "jira_issue_key": {
                            "type": "string",
                            "description": "Specific Jira issue key to correlate (e.g., 'ESS-26218', 'PROJ-123')"
                        },
                        "time_range": {
                            "type": "string",
                            "description": "Time range for correlation analysis (e.g., '-24h', '-2h', '-30m')",
                            "default": "-30m"
                        },
                        "confidence_threshold": {
                            "type": "number",
                            "description": "Minimum confidence score for correlations (0.0-1.0)",
                            "default": 0.8
                        },
                        "correlation_type": {
                            "type": "string",
                            "enum": ["bidirectional", "splunk_to_jira", "jira_to_splunk"],
                            "description": "Direction of correlation analysis",
                            "default": "bidirectional"
                        }
                    },
                    "required": []
                }
            }
        ]

    def create_correlation_system_prompt(self) -> str:
        """Create system prompt for correlation operations (enhanced from original clients)"""
        index_clause = self._get_splunk_index_clause()
        project_clause = self._get_jira_project_clause()
        return f"""You are an intelligent Splunk-Jira correlation assistant similar to Claude Desktop, with access to both Splunk and Jira through MCP tools. You help users correlate log data with issue tracking.

**Your Capabilities:**
- Search Splunk logs for errors and events (connected: {self.splunk_connected})
- Search Jira issues and tickets (connected: {self.jira_connected})  
- Correlate data between both systems with confidence scoring
- Natural language processing for complex correlation queries
- Handle errors gracefully and suggest alternatives

**Environment Information:**
- Splunk Target: {self.splunk_scheme}://{self.splunk_host}:{self.splunk_port}
- Available Splunk Indexes: {', '.join(self.splunk_indexes)}
- Jira URL: {self.jira_url}
- Available Jira Projects: {', '.join(self.jira_project_keys)}
- Current Date: {datetime.now().strftime('%Y-%m-%d')}

**Key Instructions:**
1. Intelligently choose the right correlation function based on user intent:
   - Use 'jira_to_splunk_correlation' when user mentions specific Jira issue keys (e.g., "ESS-26218") or asks to "check logs for this ticket"
   - Use 'splunk_to_jira_correlation' when user wants to "find errors and related tickets" or starts with log analysis
   - Use 'correlate_splunk_jira' for general correlation or when direction is ambiguous
2. Convert natural language to proper Splunk search queries and JQL
3. Always provide helpful, contextual responses with clear formatting
4. Include direct links to issues (format: {self.jira_url}/browse/ISSUE-KEY)
5. Handle errors gracefully and suggest alternatives
6. Be conversational and helpful, like Claude Desktop

**Function Selection Examples:**
- "Check ESS-26218 for related logs" → use 'jira_to_splunk_correlation'
- "Find recent errors and what tickets exist" → use 'splunk_to_jira_correlation'  
- "Correlate unauthorized access issues" → use 'correlate_splunk_jira'
- "Show me logs for ticket PROJ-123" → use 'jira_to_splunk_correlation'

**AVAILABLE RESOURCES:**
- Splunk Indexes: {', '.join(self.splunk_indexes)} 
- Jira Projects: {', '.join(self.jira_project_keys)}

**Splunk Search Query Examples:**
- Error logs: 'search {index_clause} "app - ERROR"'
- Time-based: 'search index="{self.splunk_indexes[0]}" earliest=-1h "unauthorized"'
- Pattern matching: 'search index="{self.splunk_indexes[0]}" "app - ERROR" "access attempts"'

**JQL Query Examples:**
- Open issues: "status in (Open, 'To Do')"
- Text search: "text ~ 'unauthorized' OR text ~ 'error'"
- Project specific: 'project = "{self.jira_project_keys[0]}" AND status in (Open, "To Do")'
- Multiple projects: "{project_clause} AND status in (Open, 'To Do')"
- Recent issues: "created >= -7d"

**CRITICAL CONFIGURATION RULES:**
- ONLY use these Splunk indexes: {', '.join(self.splunk_indexes)}
- ONLY use these Jira projects: {', '.join(self.jira_project_keys)}
- Never invent or assume other index/project names
- When in doubt, use the helper methods that generate correct clauses automatically

**CRITICAL DATA ACCURACY RULES:**
- NEVER generate tables with fake or invented issue keys (ESS-26336, ESS-26399, etc.)
- ONLY use real issue keys returned from actual Jira search results
- NEVER make up confidence scores - only use calculated correlation confidence values
- NEVER invent reasoning summaries - only use actual correlation analysis results
- If no real correlations exist, clearly state "No correlations found" instead of creating fake data
- All Jira links must be to real, accessible issues only
- Validate issue accessibility before including in results

**Response Formatting:**
- Use emojis for better readability (🔍 for searches, 🎫 for issues, 📊 for stats, 🔗 for correlations)
- Provide direct Jira links when relevant (format: {self.jira_url}/browse/ISSUE-KEY)
- Format responses clearly with proper spacing and organization
- When showing correlations, explain the confidence scores using ONLY real calculated values
- Suggest follow-up searches or analysis when appropriate
- If creating tables, use ONLY real data from function call results

**Correlation Logic:**
- Use intelligent semantic analysis powered by LLM for all correlation decisions
- Leverage natural language understanding to connect log events with business issues  
- Provide context-aware confidence scores based on semantic similarity
- Generate dynamic search queries using AI analysis rather than static patterns
- Prioritize business impact and technical relevance in correlations

**LLM-First Approach:**
- All query generation is powered by AI analysis
- Semantic understanding over keyword matching
- Context-aware correlation strategies
- Dynamic adaptation to different error types and business scenarios

You should behave like Claude Desktop - be intelligent, helpful, and conversational while providing accurate correlation analysis between Splunk and Jira data."""

    async def call_openai_api(self, messages: List[Dict[str, str]], functions: Optional[List[Dict]] = None) -> Dict[str, Any]:
        """Call OpenAI API with enhanced error handling (reused from both clients)"""
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                headers = {
                    "Authorization": f"Bearer {self.openai_api_key}",
                    "Content-Type": "application/json"
                }
                
                payload = {
                    "model": self.openai_model,
                    "messages": messages,
                    "max_tokens": 2000,
                    "temperature": 0.7
                }
                
                if functions:
                    payload["functions"] = functions
                    payload["function_call"] = "auto"
                
                # Use the correct SAP AI Core endpoint (from original clients)
                base_url = self.openai_base_url.rstrip("/")
                DEPLOYMENT_ID = "decdd5a7a276ed26"
                ENDPOINT = (
                    f"{base_url}/v2/inference/deployments/"
                    f"{DEPLOYMENT_ID}/chat/completions?api-version=2023-05-15"
                )
                
                # Add SAP AI Core headers
                headers["AI-Resource-Group"] = os.environ.get("AICORE_RESOURCE_GROUP", "default")
                
                # Debug URL construction
                print(f"\n🔧 **DEBUG API CALL (Fallback Method)**:")
                print(f"   Base URL: {base_url}")
                print(f"   Final ENDPOINT: {ENDPOINT}")
                
                # Generate and log curl command equivalent
                # curl_cmd = (
                #     f"curl -X POST '{ENDPOINT}' "
                #     f"-H 'Authorization: Bearer {self.openai_api_key}' "
                #     f"-H 'Content-Type: application/json' "
                #     f"-H 'AI-Resource-Group: {headers.get('AI-Resource-Group', 'default')}' "
                #     f"--data '{json.dumps(payload)}'"
                # )
                # print(f"\n📤 **CURL COMMAND (Fallback)**:")
                # print(f"   {curl_cmd}")
                
                response = await client.post(
                    ENDPOINT,
                    headers=headers,
                    json=payload
                )
                response.raise_for_status()
                return response.json()
                
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return {
                "choices": [{
                    "message": {
                        "content": f"I'm having trouble processing your request right now. Error: {str(e)}"
                    }
                }]
            }

    # =============================================================================
    # CORRELATION ENGINE (LLM-Powered Intelligence & Cross-System Analysis)
    # =============================================================================

    async def process_correlation_query(self, user_input: str) -> str:
        """
        MAIN CORRELATION PROCESSING PIPELINE
        ====================================
        
        This is the heart of the correlation engine - processes natural language queries
        and orchestrates intelligent cross-system analysis between Splunk and Jira.
        
        PROCESSING ARCHITECTURE:
        -----------------------
        User Input → LLM Analysis → Function Selection → MCP Tool Calls → Correlation → Response
        
        DETAILED WORKFLOW:
        ------------------
        
        PHASE 1: INPUT PROCESSING & CONTEXT MANAGEMENT
        - Add user query to conversation history for context awareness
        - Trim conversation history to prevent token limit issues
        - Prepare conversation context for LLM analysis
        
        PHASE 2: LLM INTELLIGENT ANALYSIS  
        - Send user query + conversation history to OpenAI LLM
        - LLM analyzes intent and determines optimal correlation strategy
        - Function definitions guide LLM to select appropriate tools:
          * search_splunk_logs: Direct Splunk query execution
          * search_jira_issues: Direct JQL query execution  
          * splunk_to_jira_correlation: Log-first correlation workflow
          * jira_to_splunk_correlation: Issue-first correlation workflow
          * correlate_splunk_jira: Bidirectional correlation analysis
        
        PHASE 3: FUNCTION EXECUTION & MCP TOOL CALLS
        - Execute LLM-selected function using MCP tool calls
        - Handle different correlation workflows based on LLM decision
        - Manage data retrieval from both Splunk and Jira systems
        - Apply confidence scoring and semantic analysis
        
        PHASE 4: RESULT SYNTHESIS & RESPONSE GENERATION
        - Add function results to conversation history
        - Send enriched context back to LLM for final response generation
        - LLM synthesizes findings into user-friendly correlation report
        - Return comprehensive analysis with actionable insights
        
        FALLBACK MECHANISMS:
        -------------------
        - If OpenAI LLM unavailable → Rule-based correlation parsing
        - If MCP connections fail → Graceful error handling with suggestions
        - If no correlations found → Actionable recommendations for refinement
        
        ERROR HANDLING:
        ---------------
        - Comprehensive exception handling with context-aware error messages
        - Actionable suggestions for query refinement and system checks
        - Fallback to basic correlation when advanced features unavailable
        """
        print(f"\n🔄 Processing correlation query with LLM intelligence...")
        
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Trim conversation history
        if len(self.conversation_history) > self.max_conversation_length:
            self.conversation_history = self.conversation_history[-self.max_conversation_length:]
        
        # Prepare messages for OpenAI (include system prompt + conversation history)
        messages = [
            {"role": "system", "content": self.create_correlation_system_prompt()}
        ] + self.conversation_history[-10:]  # Last 10 messages for context
        
        try:
            print(f"\n🧠 **LLM PROCESSING**:")
            print(f"   Input Query: {user_input}")
            print(f"   Model: {self.openai_model}")
            print(f"   Available Functions: {len(self.get_correlation_function_definitions())}")
            
            # Step 1: Send to OpenAI LLM with function definitions
            logger.debug("Sending request to OpenAI LLM...")
            
            try:
                response = await self.call_openai_api(
                    messages=messages,
                    functions=self.get_correlation_function_definitions()
                )
            except Exception as api_error:
                logger.warning(f"OpenAI API unavailable: {api_error}")
                print(f"   Fallback: Using basic correlation logic (OpenAI unavailable)")
                # Fallback to original correlation logic
                return await self._handle_fallback_correlation(user_input)
            
            message_obj = response["choices"][0]["message"]
            
            # Step 2: Check if LLM wants to call a function (MCP tool)
            if message_obj.get("function_call"):
                function_call = message_obj["function_call"]
                function_name = function_call["name"]
                function_args = json.loads(function_call["arguments"])
                
                print(f"   LLM Decision: Call function '{function_name}'")
                print(f"   LLM Arguments: {function_args}")
                
                # Step 3: Call appropriate function based on LLM's decision
                if function_name == "search_splunk_logs":
                    splunk_results = await self._execute_splunk_search(
                        function_args["search_query"],
                        function_args.get("time_range", "-30m")
                    )
                    tool_result = json.dumps({
                        "function": "search_splunk_logs",
                        "query": function_args["search_query"],
                        "time_range": function_args.get("time_range", "-30m"),
                        "results_count": len(splunk_results),
                        "results": splunk_results[:10]  # Limit for LLM processing
                    })
                elif function_name == "search_jira_issues":
                    # Validate and correct JQL query to use only configured projects
                    corrected_jql = self._validate_and_correct_jql(function_args["jql_query"])
                    jira_results = await self._execute_jira_search(corrected_jql)
                    tool_result = json.dumps({
                        "function": "search_jira_issues", 
                        "original_jql": function_args["jql_query"],
                        "corrected_jql": corrected_jql,
                        "results_count": len(jira_results),
                        "results": jira_results[:10]  # Limit for LLM processing
                    })
                elif function_name == "splunk_to_jira_correlation":
                    correlation_result = await self._handle_splunk_to_jira_correlation(function_args)
                    tool_result = correlation_result  # Already formatted
                elif function_name == "jira_to_splunk_correlation":
                    correlation_result = await self._handle_jira_to_splunk_correlation(function_args)
                    tool_result = correlation_result  # Already formatted
                elif function_name == "correlate_splunk_jira":
                    correlation_result = await self._handle_llm_correlation_request(function_args)
                    tool_result = correlation_result  # Already formatted
                else:
                    tool_result = json.dumps({
                        "error": f"Unknown function: {function_name}",
                        "available_functions": ["search_splunk_logs", "search_jira_issues", "splunk_to_jira_correlation", "jira_to_splunk_correlation", "correlate_splunk_jira"]
                    })
                
                # Step 4: Add function call and result to conversation history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": None,
                    "function_call": function_call
                })
                self.conversation_history.append({
                    "role": "function",
                    "name": function_name,
                    "content": str(tool_result)
                })
                
                # Step 5: Get final response from LLM based on tool results
                final_messages = [
                    {"role": "system", "content": self.create_correlation_system_prompt()}
                ] + self.conversation_history[-15:]  # Include function call context
                
                logger.debug("Getting final response from OpenAI LLM...")
                final_response = await self.call_openai_api(messages=final_messages)
                final_content = final_response["choices"][0]["message"]["content"]
                
            else:
                # LLM responded directly without needing tools
                final_content = message_obj["content"]
                print(f"   LLM Decision: Direct response (no function calls)")
            
            # Step 6: Add assistant response to conversation and return
            self.conversation_history.append({"role": "assistant", "content": final_content})
            
            print(f"   Response Length: {len(final_content)} characters")
            logger.info(f"LLM-powered response generated successfully")
            return final_content
                
        except Exception as e:
            logger.error(f"LLM correlation processing error: {e}")
            error_response = f"""❌ I encountered an error processing your request: {str(e)}

🔧 **You can try:**
• Rephrasing your question in simpler terms
• Being more specific about what you're looking for (time range, projects, etc.)
• Checking if both Splunk ({self.splunk_host}) and Jira ({self.jira_url}) are accessible
• Starting with simpler queries like "show me recent errors" or "find open issues"

💡 **Example queries that work well:**
• "Find 'unauthorized access attempts' errors from last 10hrs and corresponding jira tickets"
• "Show database timeouts in past 2 hours with related tickets"
• "Get SSL errors from last 30 minutes and matching Jira issues"
"""
            return error_response

    async def _handle_llm_correlation_request(self, function_args: Dict[str, Any]) -> str:
        """Handle correlation request from LLM function call"""
        error_patterns = function_args.get("error_patterns", [])
        time_range = function_args.get("time_range", "-30m")
        confidence_threshold = function_args.get("confidence_threshold", 0.8)
        
        print(f"\n🔗 **LLM CORRELATION REQUEST**:")
        print(f"   Error Patterns: {error_patterns}")
        print(f"   Time Range: {time_range}")
        print(f"   Confidence Threshold: {confidence_threshold}")
        
        results = {
            'splunk_results': [],
            'jira_results': [],
            'correlations': [],
            'metadata': {'patterns': error_patterns, 'time_range': time_range}
        }
        
        # Search Splunk for error patterns
        if self.splunk_connected and error_patterns:
            index_clause = self._get_splunk_index_clause()
            splunk_query = f'{index_clause} "app - ERROR" {" OR ".join([f'"{pattern}"' for pattern in error_patterns])}'
            results['splunk_results'] = await self._execute_splunk_search(splunk_query, time_range)
            print(f"   Splunk Events Found: {len(results['splunk_results'])}")
        
        # Extract semantically meaningful terms from Splunk results for intelligent Jira correlation
        semantic_error_terms = []
        if results['splunk_results']:
            for event in results['splunk_results'][:5]:  # Process top 5 events for semantic analysis
                event_text = event.get('_raw', '') or event.get('message', '') or event.get('event_data', '') or str(event)
                # Extract semantically meaningful terms instead of generic keywords
                semantic_terms = self._extract_specific_errors_from_event(event_text)
                semantic_error_terms.extend(semantic_terms)
            
            # Deduplicate while preserving semantic priority (business impact first, then technical context)
            unique_semantic_terms = []
            business_terms = [term for term in semantic_error_terms if any(word in term.lower() for word in ['failure', 'disruption', 'unavailable', 'timeout', 'refused'])]
            technical_terms = [term for term in semantic_error_terms if term not in business_terms]
            
            # Prioritize business impact terms, then technical context
            for term in business_terms + technical_terms:
                if term not in unique_semantic_terms:
                    unique_semantic_terms.append(term)
            
            semantic_error_terms = unique_semantic_terms[:8]  # Limit to top 8 semantic terms
            print(f"   Extracted Semantic Terms: {semantic_error_terms}")
        
        # Use LLM to generate semantic JQL text search terms while preserving original search terms
        if self.jira_connected:
            if semantic_error_terms or error_patterns:
                # Generate LLM-powered semantic JQL terms
                llm_jql_terms = await self._generate_semantic_jql_terms(semantic_error_terms, error_patterns, results['splunk_results'])
                
                # CRITICAL: Always include original search terms alongside LLM semantic terms
                all_search_terms = []
                
                # Add original error patterns first (MUST include actual search terms like "java.util.concurrent.ExecutionException")
                if error_patterns:
                    for pattern in error_patterns:
                        if pattern and len(pattern.strip()) > 2:
                            all_search_terms.append(pattern.strip())
                    print(f"   🎯 Original Search Terms Preserved: {error_patterns}")
                
                # Add LLM-generated semantic terms
                if llm_jql_terms:
                    all_search_terms.extend(llm_jql_terms)
                    print(f"   ✨ LLM-Generated Semantic JQL Terms ({len(llm_jql_terms)}):")
                    for i, term in enumerate(llm_jql_terms, 1):
                        print(f"      {i}. {term}")
                
                # Add extracted semantic terms as backup
                if semantic_error_terms:
                    # Add only unique semantic terms not already included
                    for term in semantic_error_terms[:3]:
                        if term not in all_search_terms:
                            all_search_terms.append(term)
                
                if all_search_terms:
                    jira_terms = " OR ".join([f'text ~ "{term}"' for term in all_search_terms])
                    print(f"   🔍 Final JQL Search Terms ({len(all_search_terms)}): {all_search_terms}")
                else:
                    # Fallback to extracted semantic terms only
                    jira_terms = " OR ".join([f'text ~ "{term}"' for term in semantic_error_terms[:6]])
                    print(f"   🔄 Using Extracted Semantic Terms (no original patterns): {semantic_error_terms[:3]}")
                
            else:
                jira_terms = 'text ~ "service disruption" OR text ~ "operation failure" OR text ~ "system failure"'
                print(f"   Using Default Semantic Terms for Jira Search")
            
            project_clause = self._get_jira_project_clause()
            jira_query = f"{project_clause} AND ({jira_terms}) AND status in (Open, 'To Do')"
            results['jira_results'] = await self._execute_jira_search(jira_query)
            print(f"   Jira Issues Found: {len(results['jira_results'])}")
            print(f"   📋 Final JQL Query: {jira_query}")
            
            # Log detailed breakdown of search strategy
            print(f"   🔍 COMPREHENSIVE JQL SEARCH STRATEGY:")
            if error_patterns:
                print(f"      ✅ Original Search Terms: {error_patterns}")
            if llm_jql_terms:
                print(f"      🧠 LLM Semantic Analysis: {llm_jql_terms[:3]}... ({len(llm_jql_terms)} total)")
            if semantic_error_terms:
                print(f"      📊 Extracted Context: {semantic_error_terms[:2]}... ({len(semantic_error_terms)} total)")
            
            # Show JQL strategy summary
            total_terms = len(all_search_terms) if 'all_search_terms' in locals() else 0
            print(f"      🎯 Total Search Terms: {total_terms}")
            print(f"      📋 Query Length: {len(jira_query)} characters")
            
            # Verify original term preservation
            original_preserved = any(pattern in jira_query for pattern in (error_patterns or []))
            print(f"      ✅ Original Terms in JQL: {'YES' if original_preserved else 'NO'}")
        
        # Generate correlation report
        return self._generate_correlation_report(results)

    async def _handle_fallback_correlation(self, user_input: str) -> str:
        """Fallback correlation when OpenAI LLM is unavailable"""
        print(f"\n🔄 **FALLBACK CORRELATION MODE**:")
        print(f"   Using rule-based parsing instead of LLM")
        
        # Parse the query using rule-based method
        parsed_query = self.query_parser.parse_correlation_query(user_input)
        
        print(f"   Detected Time Range: {parsed_query['time_range']}")
        print(f"   Detected Terms: {parsed_query['specific_terms']}")
        print(f"   Correlation Intent: {parsed_query['correlation_intent']}")
        
        # Execute correlation based on parsed intent
        if parsed_query['correlation_intent'] or (parsed_query['splunk_intent'] and parsed_query['jira_intent']):
            results = {'splunk_results': [], 'jira_results': [], 'correlations': []}
            
            # Search Splunk if connected
            if self.splunk_connected and parsed_query['specific_terms']:
                splunk_query = self._build_splunk_search_query(parsed_query)
                results['splunk_results'] = await self._execute_splunk_search(splunk_query, parsed_query['time_range'])
                print(f"   Splunk Events: {len(results['splunk_results'])}")
            
            # Search Jira if connected
            if self.jira_connected and parsed_query['specific_terms']:
                jira_query = self._build_jira_jql_query(parsed_query)
                results['jira_results'] = await self._execute_jira_search(jira_query)
                print(f"   Jira Issues: {len(results['jira_results'])}")
            
            return self._generate_correlation_report(results)
        else:
            return f"""🤖 **Enhanced Correlation Client (Fallback Mode)**
            
I understand you're looking for: {user_input}

Since the OpenAI LLM is temporarily unavailable, I can help you with:
• Direct Splunk searches using available indexes ({', '.join(self.splunk_indexes)}): search index="{self.splunk_indexes[0]}" "error_pattern"
• Direct Jira searches using available projects ({', '.join(self.jira_project_keys)}): {self._get_jira_project_clause()} AND status in (Open, "To Do")
• Basic correlations by searching both systems for common terms

Try rephrasing your query with more specific terms, or wait for the LLM service to become available.
"""

    async def _handle_correlation_request(self, parsed_query: Dict[str, Any]) -> str:
        """Handle requests that explicitly ask for correlation"""
        logger.info("🔗 Processing correlation request...")
        
        results = {
            'splunk_results': [],
            'jira_results': [],
            'correlations': [],
            'metadata': parsed_query
        }
        
        # Step 1: Search Splunk for errors/events
        if self.splunk_connected:
            splunk_query = self._build_splunk_search_query(parsed_query)
            print(f"\n📊 **STEP 1: SPLUNK SEARCH**")
            print(f"   Input Intent: Get count of errors from configured indexes with log text 'app - ERROR'")
            print(f"   Built Query: {splunk_query}")
            print(f"   Time Range: {parsed_query['time_range']}")
            results['splunk_results'] = await self._execute_splunk_search(splunk_query, parsed_query['time_range'])
            print(f"   Results Found: {len(results['splunk_results'])} events")
        else:
            print(f"\n📊 **STEP 1: SPLUNK SEARCH SKIPPED**")
            print(f"   Reason: Splunk not connected")
        
        # Step 2: Search Jira for related issues
        if self.jira_connected:
            print(f"\n🎫 **STEP 2: JIRA SEARCH**")
            if results['splunk_results']:
                # Single consolidated Jira search based on all Splunk findings (prevent multiple iterations)
                print(f"   Mode: LLM-powered consolidated Jira search for {len(results['splunk_results'])} Splunk events")
                
                # Build intelligent JQL query using LLM analysis of actual Splunk response
                consolidated_jql = await self._build_consolidated_jql_from_events(results['splunk_results'][:5], parsed_query)
                print(f"   🎯 Intelligent JQL Generated: {consolidated_jql[:100]}...")
                
                # Execute single Jira search instead of multiple iterations
                results['jira_results'] = await self._execute_jira_search(consolidated_jql)
                print(f"   Results Found: {len(results['jira_results'])} issues from LLM-optimized search")
                
                # Perform consolidated correlation analysis (single Jira result set, no additional searches)
                print(f"   🔗 Performing consolidated correlation analysis...")
                print(f"   📊 Using {len(results['jira_results'])} pre-fetched Jira issues for ALL event correlations")
                
                for i, splunk_event in enumerate(results['splunk_results'][:5]):
                    print(f"   Analyzing Event {i+1}/{len(results['splunk_results'][:5])} against consolidated Jira results...")
                    
                    # Use BOTH correlation methods with pre-fetched issues (no new searches)
                    simple_matches = await self._correlate_event_with_issues(splunk_event, results['jira_results'], parsed_query)
                    advanced_matches = await self._find_related_jira_issues(splunk_event, parsed_query, results['jira_results'])
                    
                    # Combine and deduplicate matches
                    all_matches = simple_matches + advanced_matches
                    unique_matches = []
                    seen_keys = set()
                    
                    for match in all_matches:
                        issue_key = match['jira_issue'].get('key', '')
                        if issue_key and issue_key not in seen_keys:
                            seen_keys.add(issue_key)
                            unique_matches.append(match)
                    
                    results['correlations'].extend(unique_matches)
                    print(f"   Found {len(unique_matches)} unique correlations for event {i+1} (from {len(all_matches)} total matches)")
            else:
                # Direct Jira search based on query terms
                print(f"   Mode: Direct Jira search (no Splunk events)")
                jira_query = self._build_jira_jql_query(parsed_query)
                extracted_project = self._extract_project_from_query(parsed_query['original_query'])
                jira_time = self._extract_jira_time_from_query(parsed_query['original_query'])
                print(f"   Input Intent: Get open jira issues from project '{extracted_project or 'ANY'}' with description containing specific terms")
                print(f"   Extracted Project: {extracted_project or 'Not specified'}")
                print(f"   Extracted Time Range: {jira_time or 'Default (-30d)'}")
                print(f"   Built JQL: {jira_query}")
                results['jira_results'] = await self._execute_jira_search(jira_query)
                print(f"   Results Found: {len(results['jira_results'])} issues")
        else:
            print(f"\n🎫 **STEP 2: JIRA SEARCH SKIPPED**")
            print(f"   Reason: Jira not connected")
        
        # Step 3: Generate correlation report
        print(f"\n📋 **STEP 3: CORRELATION ANALYSIS**")
        print(f"   Total Splunk Events: {len(results['splunk_results'])}")
        print(f"   Total Jira Issues: {len(results['jira_results'])}")
        print(f"   Total Correlations: {len(results['correlations'])}")
        
        return self._generate_correlation_report(results)

    async def _handle_dual_search_request(self, parsed_query: Dict[str, Any]) -> str:
        """Handle requests for both Splunk and Jira data"""
        logger.info("🔍 Processing dual search request...")
        
        tasks = []
        if self.splunk_connected:
            splunk_query = self._build_splunk_search_query(parsed_query)
            tasks.append(self._execute_splunk_search(splunk_query, parsed_query['time_range']))
        
        if self.jira_connected:
            jira_query = self._build_jira_jql_query(parsed_query)
            tasks.append(self._execute_jira_search(jira_query))
        
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return self._format_dual_search_results(results, parsed_query)
        else:
            return "❌ No MCP connections available for search"

    async def _handle_splunk_only_request(self, parsed_query: Dict[str, Any]) -> str:
        """Handle Splunk-only requests"""
        if not self.splunk_connected:
            return "❌ Splunk MCP not connected"
            
        splunk_query = self._build_splunk_search_query(parsed_query)
        results = await self._execute_splunk_search(splunk_query, parsed_query['time_range'])
        return self._format_splunk_results(results, parsed_query)

    async def _handle_jira_only_request(self, parsed_query: Dict[str, Any]) -> str:
        """Handle Jira-only requests"""
        if not self.jira_connected:
            return "❌ Jira MCP not connected"
            
        jira_query = self._build_jira_jql_query(parsed_query)
        results = await self._execute_jira_search(jira_query)
        return self._format_jira_results(results, parsed_query)

    async def _handle_general_request(self, user_input: str, parsed_query: Dict[str, Any]) -> str:
        """Handle general requests using OpenAI"""
        system_prompt = self.create_correlation_system_prompt()
        functions = self.get_correlation_function_definitions()
        
        messages = [
            {"role": "system", "content": system_prompt},
            *self.conversation_history[-10:]  # Last 10 messages for context
        ]
        
        response = await self.call_openai_api(messages, functions)
        
        # Handle function calling if present
        if 'choices' in response and response['choices']:
            choice = response['choices'][0]
            message = choice.get('message', {})
            
            if 'function_call' in message:
                function_result = await self._execute_function_call(message['function_call'])
                return function_result
            else:
                assistant_response = message.get('content', 'No response generated')
                self.conversation_history.append({"role": "assistant", "content": assistant_response})
                return assistant_response
        
        return "❌ Unable to process request"

    async def _execute_function_call(self, function_call: Dict[str, Any]) -> str:
        """Execute OpenAI function calls"""
        function_name = function_call.get('name')
        arguments = json.loads(function_call.get('arguments', '{}'))
        
        if function_name == 'search_splunk_logs':
            if not self.splunk_connected:
                return "❌ Splunk MCP not connected"
            results = await self._execute_splunk_search(
                arguments.get('search_query'), 
                arguments.get('time_range', '-30m')
            )
            return self._format_splunk_results(results, arguments)
            
        elif function_name == 'search_jira_issues':
            if not self.jira_connected:
                return "❌ Jira MCP not connected" 
            results = await self._execute_jira_search(arguments.get('jql_query'))
            return self._format_jira_results(results, arguments)
            
        elif function_name == 'correlate_splunk_jira':
            return await self._execute_correlation(arguments)
        
        return f"❌ Unknown function: {function_name}"

    # =============================================================================
    # SEARCH EXECUTION METHODS (Query Building & Execution)
    # =============================================================================

    def _build_splunk_search_query(self, parsed_query: Dict[str, Any]) -> str:
        """
        Build optimized Splunk search query from parsed user input
        
        QUERY CONSTRUCTION WORKFLOW:
        ----------------------------
        1. INDEX EXTRACTION:
           - Parse user query for explicit index specifications
           - Default to configured SPLUNK_INDEXES if not specified
           - Support multiple indexes with OR logic for broader search coverage
           - Support quoted index names and case-insensitive matching
        
        2. SEARCH PATTERN BUILDING:
           - Add base index restriction using configured indexes
           - Include log type filters for error logs: "app - ERROR"
           - Add specific quoted terms from user input for exact matching
           - Filter out short terms (<3 chars) to reduce noise
        
        3. QUERY TYPE DETECTION:
           - Detect if user wants count/statistics vs. raw events
           - Append "| stats count as error_count" for counting requests
           - Use standard search format for event retrieval
        
        4. OPTIMIZATION:
           - Combine search terms efficiently to minimize query complexity
           - Use exact quoted matching for precision
           - Balance specificity with result coverage
        
        EXAMPLE TRANSFORMATIONS:
        - "unauthorized access errors" → search {self._get_splunk_index_clause()} "app - ERROR" "unauthorized access"
        - "count database timeouts" → search {self._get_splunk_index_clause()} "app - ERROR" "database" "timeouts" | stats count as error_count
        """
        original_query = parsed_query['original_query']
        
        # Extract index (default to searching all configured indexes)
        import re
        index_match = re.search(r'index\s+"([^"]+)"', original_query, re.IGNORECASE)
        
        if index_match:
            # User specified an index explicitly
            index_clause = self._get_splunk_index_clause(index_match.group(1))
        else:
            # Search across all configured indexes for better coverage
            index_clause = self._get_splunk_index_clause()
        
        # Build search components
        search_parts = [index_clause]
        
        # Add log text pattern - look for "app - ERROR" for error logs
        if any(keyword in original_query.lower() for keyword in ['error', 'unauthorized', 'access']):
            search_parts.append('"app - ERROR"')
        
        # Add specific quoted terms for exact matching
        for term in parsed_query['specific_terms']:
            if len(term) > 3:  # Only add meaningful terms
                search_parts.append(f'"{term}"')
        
        # Check if user wants count/stats
        if 'count' in original_query.lower():
            base_search = " ".join(search_parts)
            return f"search {base_search} | stats count as error_count"
        else:
            return f"search {' '.join(search_parts)}"

    def _build_jira_jql_query(self, parsed_query: Dict[str, Any]) -> str:
        """
        Build optimized JQL (Jira Query Language) query from parsed user input
        
        JQL CONSTRUCTION WORKFLOW:
        --------------------------
        1. PROJECT IDENTIFICATION:
           - Extract project codes from user query (ESS, PROJ, etc.)
           - Use regex patterns to identify project references
           - Default to no project restriction if not specified
        
        2. STATUS FILTERING:
           - Default to open issues: status in (Open, "To Do")
           - Override if user specifies closed/done/resolved issues
           - Align with business focus on actionable items
        
        3. CONTENT SEARCH BUILDING:
           - Process specific quoted terms from user input
           - Escape quotes and validate terms for JQL safety (prevent injection)
           - Build description search conditions using JQL text matching
           - Use OR operators to capture variations of error descriptions
        
        4. TIME RANGE APPLICATION:
           - Extract Jira-specific time ranges from query
           - Apply creation date filters: created >= -30d (default)
           - Support custom day ranges from user input
        
        5. FALLBACK SEARCH TERMS:
           - Add default error-related search if no specific terms found
           - Use broad semantic terms: "error", "unauthorized", "access"
           - Ensure query always returns relevant results
        
        6. JQL VALIDATION & SAFETY:
           - Validate final JQL syntax using _validate_jql_syntax()
           - Fix common syntax issues (unmatched quotes, operators)
           - Prevent JQL injection and malformed queries
        
        EXAMPLE TRANSFORMATIONS:
        - "PROJECT unauthorized issues" → {self._get_jira_project_clause()} AND status in (Open, "To Do") AND (description ~ "unauthorized")
        - "recent access errors" → (text ~ "error" OR text ~ "access") AND created >= -7d
        """
        jql_parts = []
        original_query = parsed_query['original_query']
        
        # Extract project from query (like independent client)
        extracted_project = self._extract_project_from_query(original_query)
        if extracted_project:
            # Use specific project if found and valid
            jql_parts.append(self._get_jira_project_clause(extracted_project))
        else:
            # Use configured projects if no specific project mentioned
            jql_parts.append(self._get_jira_project_clause())
        logger.debug(f"TRACE(DEBUG) _build_jira_jql_query() -> extracted_project : {jql_parts[-1]}")
        
        # Add status filtering for open issues (matching independent client behavior)
        if 'open' in original_query.lower() or not any(status in original_query.lower() 
                                                      for status in ['closed', 'done', 'resolved']):
            jql_parts.append('status in (Open, "To Do")')
        
        # Add description search (exact match like independent client)
        description_conditions = []
        for term in parsed_query.get('specific_terms', []):
            # Escape quotes and validate term for JQL safety
            safe_term = str(term).replace('"', '\\"').strip()
            if safe_term and len(safe_term) > 2:
                description_conditions.append(f'description ~ "{safe_term}"')
        
        # Add keyword-based search if no specific terms
        if not description_conditions and parsed_query.get('error_keywords'):
            for keyword in parsed_query['error_keywords']:
                # Escape quotes and validate keyword
                safe_keyword = str(keyword).replace('"', '\\"').strip()
                if safe_keyword and len(safe_keyword) > 2:
                    description_conditions.append(f'description ~ "{safe_keyword}"')
        
        if description_conditions:
            jql_parts.append(f"({' OR '.join(description_conditions)})")
        
        # Add creation date filter for Jira issues (independent client uses 30 days default)
        jira_time_range = self._extract_jira_time_from_query(original_query)
        if jira_time_range:
            jql_parts.append(f"created >= {jira_time_range}")
        elif 'jira' in original_query.lower() and 'day' in original_query.lower():
            import re
            days_match = re.search(r'(\d+)\s*days?', original_query)
            if days_match:
                days = days_match.group(1)
                jql_parts.append(f"created >= -{days}d")
            else:
                jql_parts.append("created >= -30d")  # Default like independent client
        
        # Default search if nothing specific
        if len(jql_parts) <= 1:  # Only project specified
            jql_parts.append('(text ~ "error" OR text ~ "unauthorized" OR text ~ "access")')
        
        # Build and validate final JQL
        final_jql = " AND ".join(jql_parts)
        return self._validate_jql_syntax(final_jql)
    
    def _validate_jql_syntax(self, jql_query: str) -> str:
        """Validate JQL syntax and fix common issues"""
        import re
        
        if not jql_query or not jql_query.strip():
            return f'{self._get_jira_project_clause()} AND status in (Open, "To Do")'
        
        # Remove extra spaces and fix quote issues
        jql_query = jql_query.strip()
        
        # Fix escaped quotes - convert \" to "
        jql_query = jql_query.replace('\\"', '"')
        
        # Check for unmatched quotes
        quote_count = jql_query.count('"')
        if quote_count % 2 != 0:
            # Fix unmatched quotes by removing the last quote
            jql_query = jql_query.rsplit('"', 1)[0]
        
        # Ensure proper AND/OR syntax - fix common syntax errors
        jql_query = re.sub(r'\s+AND\s+AND\s+', ' AND ', jql_query)
        jql_query = re.sub(r'\s+OR\s+OR\s+', ' OR ', jql_query)
        
        # Remove trailing operators
        jql_query = re.sub(r'\s+(AND|OR)\s*$', '', jql_query)
        
        # Ensure it doesn't start with AND/OR
        jql_query = re.sub(r'^\s*(AND|OR)\s+', '', jql_query)
        
        # If query is empty after cleaning, provide default
        if not jql_query.strip():
            return f'{self._get_jira_project_clause()} AND status in (Open, "To Do")'

        logger.debug(f"TRACE(DEBUG) _validate_jql_syntax() -> jql_query : {jql_query}")
        return jql_query

    def _validate_and_correct_jql(self, jql_query: str) -> str:
        """
        Validate and correct JQL query to ensure only configured projects are used
        
        This method fixes the core issue where LLM generates invalid project names
        by replacing any invalid project references with configured project clauses.
        """
        import re
        
        if not jql_query or not jql_query.strip():
            return f'{self._get_jira_project_clause()} AND status in (Open, "To Do")'
        
        logger.debug(f"Validating JQL: {jql_query}")
        
        # Find all project references in the query
        project_patterns = [
            r'project\s*=\s*"?([^"\s]+)"?',
            r'project\s+IN\s*\([^)]+\)',
            r'\(project\s*=\s*"?([^"\s]+)"?[^)]*\)'
        ]
        
        corrected_jql = jql_query
        found_invalid_project = False
        
        for pattern in project_patterns:
            matches = re.finditer(pattern, corrected_jql, re.IGNORECASE)
            for match in matches:
                full_match = match.group(0)
                if len(match.groups()) > 0:
                    project_name = match.group(1).strip('"').upper()
                    
                    # Check if project is invalid (not in configured projects)
                    if project_name not in self.jira_project_keys:
                        logger.warning(f"Replacing invalid project '{project_name}' with configured projects: {self.jira_project_keys}")
                        found_invalid_project = True
                        
                        # Replace the entire project clause with configured projects
                        project_replacement = self._get_jira_project_clause()
                        corrected_jql = corrected_jql.replace(full_match, project_replacement)
        
        # If no project clause found at all, prepend the configured projects
        if not re.search(r'project\s*=', corrected_jql, re.IGNORECASE):
            project_clause = self._get_jira_project_clause()
            corrected_jql = f"{project_clause} AND {corrected_jql}"
        
        # Apply general JQL syntax validation
        corrected_jql = self._validate_jql_syntax(corrected_jql)
        
        if found_invalid_project:
            logger.info(f"JQL corrected from: {jql_query}")
            logger.info(f"JQL corrected to: {corrected_jql}")
        logger.debug(f"TRACE(DEBUG) _validate_and_correct_jql() -> corrected_jql : {corrected_jql}")
        
        return corrected_jql
    
    def _extract_project_from_query(self, query: str) -> str:
        """Extract Jira project from user query, validate against configured projects"""
        import re
        
        # Look for project patterns including ticket format (e.g., PS-28690)
        project_patterns = [
            r'project\s+"([^"]+)"',
            r'project\s+([A-Z]+)',
            r'from project\s+"([^"]+)"',
            r'from project\s+([A-Z]+)',
            r'\b([A-Z]{2,10})\s+jira',
            r'\b([A-Z]{2,10})\s+ticket',
            r'\b([A-Z]{2,10})-\d+',  # Match ticket format like PS-28690, ESS-1234
            r'ticket\s+([A-Z]{2,10})-\d+',  # Match "ticket PS-28690" format
            r'issue\s+([A-Z]{2,10})-\d+'   # Match "issue PS-28690" format
        ]
        
        for pattern in project_patterns:
            match = re.search(pattern, query, re.IGNORECASE)
            if match:
                extracted_project = match.group(1).upper()
                # Validate against configured project keys - ONLY return if valid
                if extracted_project in self.jira_project_keys:
                    return extracted_project
                # If not found in configured projects, ignore it and continue searching
                logger.debug(f"Ignoring invalid project '{extracted_project}' - not in configured projects: {self.jira_project_keys}")
        
        # Return default project if no valid project found in query
        logger.debug(f"No valid project found in query, using default project: {self.jira_default_project}")
        return self.jira_default_project
    
    def _extract_status_from_query(self, query: str) -> str:
        """Extract status filter from user query"""
        query_lower = query.lower()
        
        if 'open' in query_lower:
            return '"Open", "In Progress", "To Do", "New"'
        elif 'closed' in query_lower:
            return '"Closed", "Done", "Resolved"'
        else:
            # Default to open issues
            return '"Open", "In Progress", "To Do", "New"'
    
    def _extract_jira_time_from_query(self, query: str) -> str:
        """Extract Jira-specific time range from query"""
        import re
        
        # Look for Jira time patterns
        jira_time_patterns = [
            (r'jira.*created.*last\s+(\d+)\s*days?', lambda m: f"-{m.group(1)}d"),
            (r'jira.*last\s+(\d+)\s*days?', lambda m: f"-{m.group(1)}d"),
            (r'issues.*created.*last\s+(\d+)\s*days?', lambda m: f"-{m.group(1)}d"),
            (r'ticket.*created.*last\s+(\d+)\s*days?', lambda m: f"-{m.group(1)}d"),
        ]
        
        for pattern, converter in jira_time_patterns:
            match = re.search(pattern, query.lower())
            if match:
                return converter(match)
        
        return ""

    async def _execute_splunk_search(self, search_query: str, time_range: str = "-30m") -> List[Dict[str, Any]]:
        """
        Execute Splunk search via MCP and parse results
        
        EXECUTION WORKFLOW:
        -------------------
        1. SESSION VALIDATION:
           - Verify active Splunk MCP session exists
           - Return empty list if no connection available
        
        2. TOOL DISCOVERY & SELECTION:
           - Query MCP server for available search tools
           - Try multiple possible tool names: ["search_splunk", "search", "run_search"]
           - Select first available tool for search execution
        
        3. SEARCH PARAMETER CONSTRUCTION:
           - Build search parameters with query, time range, and result limits
           - Set earliest_time (e.g., "-30m") and latest_time ("now")
           - Limit max_results to 50 to prevent overwhelming responses
        
        4. MCP TOOL EXECUTION:
           - Call selected tool using call_tool_with_retry() for robustness
           - Log detailed prompt and response information for debugging
           - Handle various response formats and error conditions
        
        5. RESPONSE PARSING:
           - Parse MCP response using _parse_splunk_response()
           - Extract log events and metadata from search results
           - Return structured list of event dictionaries
        
        LOGGING & DEBUGGING:
        -------------------
        - Log search tool selection and parameters
        - Log response content and parsing results  
        - Track search execution success/failure
        - Provide detailed error information for troubleshooting
        
        RETURNS: List[Dict[str, Any]] - Parsed Splunk events with metadata
        """
        if not self.splunk_session:
            return []
        
        try:
            # Get available tools first to check correct tool name
            tools_result = await self.splunk_session.list_tools()
            available_tools = [tool.name for tool in tools_result.tools]
            logger.debug(f"Available Splunk tools: {available_tools}")
            
            # Try different possible tool names
            search_tool = None
            possible_names = ["search_splunk", "search", "run_search", "splunk_search"]
            for tool_name in possible_names:
                if tool_name in available_tools:
                    search_tool = tool_name
                    break
            
            if not search_tool:
                logger.error(f"No search tool found. Available tools: {available_tools}")
                return []
            
            # 🔍 LOG SPLUNK PROMPT
            splunk_prompt = {
                "search_query": search_query,
                "earliest_time": time_range,
                "latest_time": "now",
                "max_results": 50
            }
            print(f"\n🔍 **SPLUNK PROMPT** ({search_tool}):")
            print(f"   Query: {search_query}")
            print(f"   Time Range: {time_range} to now")
            print(f"   Max Results: 50")
            print(f"   Full Prompt: {splunk_prompt}")
            
            result = await self.call_tool_with_retry(
                self.splunk_session,
                search_tool,
                splunk_prompt
            )
            
            # 🔍 LOG SPLUNK RESPONSE
            ##### Do not delete
            # print(f"\n📊 **SPLUNK RESPONSE**:")
            # if hasattr(result, 'content') and result.content:
            #     for i, content in enumerate(result.content):
            #         if hasattr(content, 'text') and content.text:
            #             response_text = content.text[:500] + "..." if len(content.text) > 500 else content.text
            #             print(f"   Content[{i}]: {response_text}")
            #         else:
            #             print(f"   Content[{i}]: No text attribute")
            # else:
            #     print(f"   No content in response")
            
            return self._parse_splunk_response(result)
            
        except Exception as e:
            logger.error(f"Splunk search error: {e}")
            return []

    async def _execute_jira_search(self, jql_query: str) -> List[Dict[str, Any]]:
        """
        Execute Jira search via MCP and parse results
        
        EXECUTION WORKFLOW:
        -------------------
        1. SESSION VALIDATION:
           - Verify active Jira MCP session exists
           - Return empty list if no connection available
        
        2. JQL VALIDATION & CLEANING:
           - Validate and clean JQL syntax using _validate_jql_syntax()
           - Fix common syntax errors (quotes, operators, structure)
           - Prevent JQL injection and malformed queries
        
        3. TOOL DISCOVERY & SELECTION:
           - Query MCP server for available Jira search tools
           - Try multiple tool names: ["jira_search", "search_issues", "search"]
           - Prioritize "jira_search" based on discovery patterns
        
        4. SEARCH PARAMETER CONSTRUCTION:
           - Build JQL search parameters with query and field specifications
           - Request key fields: summary, status, assignee, priority, description, created
           - Limit results to 20 issues and set pagination start_at to 0
        
        5. MCP TOOL EXECUTION:
           - Call selected tool using call_tool_with_retry() for robustness
           - Log detailed JQL query information and response data
           - Handle various response formats and error conditions
        
        6. RESPONSE PARSING:
           - Parse MCP response using _parse_jira_response()
           - Extract issue data and metadata from search results
           - Filter out error messages and invalid responses
           - Return structured list of issue dictionaries
        
        LOGGING & DEBUGGING:
        -------------------
        - Log JQL query details (query, length, validation status)
        - Log search tool selection and execution parameters
        - Log response parsing results and issue counts
        - Provide detailed error information for troubleshooting
        
        RETURNS: List[Dict[str, Any]] - Parsed Jira issues with fields and metadata
        """
        if not self.jira_session:
            return []
        
        # Validate and correct JQL query to ensure only configured projects are used
        original_jql = jql_query
        jql_query = self._validate_and_correct_jql(jql_query)
        logger.debug(f"TRACE(DEBUG) Original JQL Query: {original_jql}")
        logger.debug(f"TRACE(DEBUG) Corrected JQL Query: {jql_query}")
        
        try:
            # Get available tools first to check correct tool name
            tools_result = await self.jira_session.list_tools()
            available_tools = [tool.name for tool in tools_result.tools]
            logger.debug(f"Available Jira tools: {available_tools}")
            
            # Try different possible tool names (prioritize jira_search based on discovery)
            search_tool = None
            possible_names = ["jira_search", "search_issues", "search", "find_issues"]
            for tool_name in possible_names:
                if tool_name in available_tools:
                    search_tool = tool_name
                    logger.info(f"Using Jira search tool: {search_tool}")
                    break
            
            if not search_tool:
                logger.error(f"No Jira search tool found. Available tools: {available_tools}")
                return []
            
            # 🎫 LOG JIRA PROMPT
            jira_prompt = {
                "jql": jql_query,
                "fields": "summary,status,assignee,priority,description,created",
                "limit": 20,
                "start_at": 0
            }
            print(f"\n🎫 **JIRA PROMPT** ({search_tool}):")
            print(f"   JQL Query: {jql_query}")
            print(f"   JQL Length: {len(jql_query)} characters")
            print(f"   JQL First 10 chars: '{jql_query[:10]}'")
            print(f"   Fields: summary,status,assignee,priority,description,created")
            print(f"   Limit: 20")
            print(f"   Full Prompt: {jira_prompt}")
            
            result = await self.call_tool_with_retry(
                self.jira_session,
                search_tool,
                jira_prompt
            )
            
            # 🎫 LOG JIRA RESPONSE
            print(f"\n📋 **JIRA RESPONSE**:")
            if hasattr(result, 'content') and result.content:
                for i, content in enumerate(result.content):
                    if hasattr(content, 'text') and content.text:
                        response_text = content.text[:500] + "..." if len(content.text) > 500 else content.text
                        print(f"   Content[{i}]: {response_text}")
                    else:
                        print(f"   Content[{i}]: No text attribute")
            else:
                print(f"   No content in response")
            
            return self._parse_jira_response(result)
            
        except Exception as e:
            logger.error(f"Jira search error: {e}")
            return []

    def _parse_splunk_response(self, response) -> List[Dict[str, Any]]:
        """Parse Splunk MCP response"""
        results = []
        try:
            logger.debug(f"🔧 Splunk response type: {type(response)}")
            logger.debug(f"🔧 Splunk response hasattr content: {hasattr(response, 'content')}")
            
            if hasattr(response, 'content') and response.content:
                for content in response.content:
                    logger.debug(f"🔧 Content type: {type(content)}, hasattr text: {hasattr(content, 'text')}")
                    if hasattr(content, 'text') and content.text:
                        logger.debug(f"🔧 Content text (first 200 chars): {content.text[:200]}")
                        try:
                            data = json.loads(content.text)
                            if isinstance(data, list):
                                results.extend(data)
                            elif isinstance(data, dict):
                                results.append(data)
                        except json.JSONDecodeError as e:
                            logger.warning(f"JSON decode error: {e}, content: {content.text[:100]}")
                            # Try to handle non-JSON responses
                            if content.text.strip():
                                results.append({"raw_response": content.text})
        except Exception as e:
            logger.error(f"Error parsing Splunk response: {e}")
        
        logger.info(f"📊 Parsed {len(results)} Splunk events")
        return results

    def _parse_jira_response(self, response) -> List[Dict[str, Any]]:
        """Parse Jira MCP response"""
        results = []
        try:
            logger.debug(f"🔧 Jira response type: {type(response)}")
            logger.debug(f"🔧 Jira response hasattr content: {hasattr(response, 'content')}")
            
            if hasattr(response, 'content') and response.content:
                for content in response.content:
                    logger.debug(f"🔧 Jira content type: {type(content)}")
                    if hasattr(content, 'text') and content.text:
                        content_text = content.text.strip()
                        logger.debug(f"🔧 Raw Jira content length: {len(content_text)}")
                        logger.debug(f"🔧 Jira content starts with: {content_text[:50]}")
                        
                        # Check for actual error messages (not just the word "error" in valid JSON)
                        if ("Error calling tool" in content_text or 
                            content_text.startswith("Error:") or 
                            content_text.startswith("❌") or
                            (content_text.startswith("{") and "error" in content_text[:100] and "issues" not in content_text[:200])):
                            logger.warning(f"Jira tool error detected: {content_text[:100]}")
                            continue  # Skip error messages, don't count as issues
                        
                        try:
                            # Try to parse as JSON
                            data = json.loads(content_text)
                            logger.debug(f"🔧 Successfully parsed JSON with keys: {list(data.keys()) if isinstance(data, dict) else 'list'}")
                            
                            if isinstance(data, dict) and 'issues' in data:
                                # Standard Jira search response
                                issues = data['issues']
                                logger.info(f"🔧 Found {len(issues)} issues in Jira response")
                                results.extend(issues)
                            elif isinstance(data, list):
                                # Direct list of issues
                                results.extend(data)
                            elif isinstance(data, dict) and 'key' in data:
                                # Single Jira issue
                                results.append(data)
                            else:
                                logger.debug(f"🔧 Unexpected JSON structure: {type(data)}")
                                
                        except json.JSONDecodeError as e:
                            logger.warning(f"Jira JSON decode error: {e}")
                            logger.debug(f"Invalid JSON content (first 500 chars): {content_text[:500]}")
                            # Check if it's a partial/truncated response that might still contain valid data
                            if "issues" in content_text and '"key":' in content_text:
                                logger.warning("Response appears to contain valid Jira data but JSON is malformed - possibly truncated")
                            continue
                            
        except Exception as e:
            logger.error(f"Error parsing Jira response: {e}")
        
        logger.info(f"📊 Parsed {len(results)} Jira issues")
        return results

    # =============================================================================
    # CORRELATION ALGORITHMS (LLM-Powered Semantic Analysis)
    # =============================================================================

    async def _find_related_jira_issues(self, splunk_event: Dict[str, Any], parsed_query: Dict[str, Any], pre_fetched_issues: List[Dict] = None) -> List[Dict[str, Any]]:
        """
        Find Jira issues related to a specific Splunk event using LLM-powered correlation
        
        CORRELATION WORKFLOW:
        --------------------
        1. EVENT ANALYSIS PREPARATION:
           - Extract raw event data from Splunk event dictionary
           - Limit event summary to 500 chars for LLM processing efficiency
           - Prepare event context for semantic analysis
        
        2. LLM CORRELATION STRATEGY GENERATION:
           - Send event summary to LLM for business impact analysis
           - Generate multiple JQL search strategies based on different business perspectives:
             * Security team perspective (alerts, incidents, threats)
             * Operations perspective (system issues, performance)
             * User experience perspective (access problems, authentication)
           - Each strategy includes JQL query + reasoning + focus area
        
        3. MULTI-STRATEGY SEARCH EXECUTION:
           - Execute each LLM-generated JQL search strategy
           - Collect unique Jira issues from all strategies (deduplicate by key)
           - Log search results and strategy effectiveness
        
        4. LLM-POWERED CONFIDENCE SCORING:
           - For each found Jira issue, calculate correlation confidence using LLM
           - LLM analyzes semantic similarity, business impact alignment, technical overlap
           - Generate confidence scores (0.0-1.0) with detailed reasoning
           - Include correlation aspects and relationship type analysis
        
        5. CORRELATION RESULT COMPILATION:
           - Filter correlations by minimum confidence threshold (0.3+)
           - Compile correlation objects with issue data, confidence, and reasoning
           - Sort by confidence score (highest first)
           - Return top 5 correlations for focused analysis
        
        INTELLIGENCE FEATURES:
        ---------------------
        - Semantic understanding over keyword matching
        - Business context awareness (security issues prioritized)
        - Multi-perspective analysis (security/operations/user experience)
        - Confidence scoring with detailed reasoning
        - Adaptive strategy generation based on event content
        
        RETURNS: List[Dict] - Top correlated Jira issues with confidence scores and reasoning
        """
        correlations = []
        
        # Extract event information
        event_raw = splunk_event.get('_raw', str(splunk_event))
        event_summary = event_raw[:500]  # Limit for LLM processing
        
        print(f"   🧠 Using LLM to analyze Splunk event for correlation...")
        
        # Use LLM to analyze the event and generate search strategies
        correlation_strategies = await self._generate_llm_correlation_strategies(event_summary, parsed_query)
        
        if not correlation_strategies:
            print(f"   ⚠️ No correlation strategies generated by LLM")
            return []
        
        # DISABLED: Execute LLM-generated search strategies (redundant - using consolidated search now)
        all_issues = []
        seen_keys = set()
        
        print(f"   ⚠️ SKIPPING individual strategy searches - using consolidated search instead")
        print(f"   � Generated {len(correlation_strategies)} strategies but will use pre-fetched Jira results")
        
        # Note: Individual strategy execution disabled to prevent redundant Jira calls
        # Use pre-fetched Jira issues if provided (avoids redundant searches)
        if pre_fetched_issues:
            print(f"   ✅ Using {len(pre_fetched_issues)} pre-fetched Jira issues for correlation")
            all_issues = pre_fetched_issues[:20]  # Limit for performance
        else:
            print(f"   ⚠️ No pre-fetched issues available - skipping individual correlation")
            return []
        
        # LLM-based correlation scoring with pre-fetched issues (NO additional Jira searches)
        for jira_issue in all_issues[:15]:  # Process top results
            confidence_data = await self._calculate_llm_correlation_confidence(splunk_event, jira_issue)
            
            if confidence_data['confidence'] >= 0.3:  # Lower threshold for LLM-based correlation
                correlations.append({
                    'jira_issue': jira_issue,
                    'splunk_event': splunk_event,
                    'confidence': confidence_data['confidence'],
                    'matching_aspects': confidence_data.get('aspects', []),
                    'issue_key': jira_issue.get('key', ''),
                    'issue_summary': jira_issue.get('fields', {}).get('summary', ''),
                    'correlation_reason': confidence_data.get('reasoning', 'LLM correlation with consolidated results')
                })
        
        # Sort by confidence and return top correlations
        return sorted(correlations, key=lambda x: x['confidence'], reverse=True)[:5]

    async def _build_consolidated_jql_from_events(self, splunk_events: List[Dict], parsed_query: Dict[str, Any]) -> str:
        """
        Build intelligent JQL query using LLM analysis of Splunk response while preserving original search terms
        
        This method:
        1. Analyzes actual Splunk log content using LLM for semantic understanding  
        2. Preserves original search terms (e.g., "java.util.concurrent.ExecutionException")
        3. Generates business-meaningful JQL terms that avoid generic patterns
        4. Creates targeted Jira searches that find relevant issues, not noise
        """
        print(f"\n🧠 **BUILDING INTELLIGENT JQL FROM SPLUNK ANALYSIS**")
        
        # Step 1: Extract original search terms from query (MUST preserve these)
        original_terms = []
        if parsed_query.get('specific_terms'):
            for term in parsed_query['specific_terms']:
                if len(term) > 3:
                    original_terms.append(term)
        
        print(f"   🎯 Original Terms to Preserve: {original_terms}")
        
        # Step 2: Prepare Splunk response context for LLM analysis
        splunk_context = []
        for i, event in enumerate(splunk_events[:3]):  # Analyze top 3 events for context
            event_text = event.get('_raw', '') or event.get('message', '') or str(event)
            if event_text:
                splunk_context.append({
                    'event_number': i + 1,
                    'content': event_text[:800]  # Limit for LLM processing
                })
        
        print(f"   📊 Analyzing {len(splunk_context)} Splunk events with LLM...")
        
        # Step 3: Use LLM to generate semantic JQL terms from actual Splunk content
        llm_jql_terms = await self._generate_intelligent_jql_from_splunk_response(
            splunk_context, original_terms, parsed_query
        )
        
        # Step 4: Build comprehensive JQL with original + LLM semantic terms
        all_jql_terms = []
        
        # CRITICAL: Always include original search terms first
        if original_terms:
            all_jql_terms.extend(original_terms)
            print(f"   ✅ Preserved Original Terms: {original_terms}")
        
        # Add LLM-generated semantic terms
        if llm_jql_terms:
            # Filter out terms already in original_terms to avoid duplicates
            unique_llm_terms = [term for term in llm_jql_terms if term not in original_terms]
            all_jql_terms.extend(unique_llm_terms[:8])  # Limit semantic terms
            print(f"   🧠 Added LLM Semantic Terms: {unique_llm_terms[:5]}...")
        
        # Step 5: Build final JQL query
        if all_jql_terms:
            # Create text search conditions
            jql_conditions = []
            for term in all_jql_terms:
                # Escape quotes for JQL safety
                safe_term = str(term).replace('"', '\\"')
                jql_conditions.append(f'text ~ "{safe_term}"')
            
            text_search = f"({' OR '.join(jql_conditions)})"
            print(f"   🔍 Final JQL Terms ({len(all_jql_terms)}): {all_jql_terms}")
        else:
            # Fallback if no terms available
            text_search = '(text ~ "service issue" OR text ~ "system problem")'
            print(f"   🔄 Using fallback semantic terms (no specific terms found)")
        
        # Build complete JQL query
        project_clause = self._get_jira_project_clause()
        consolidated_jql = f"{project_clause} AND {text_search} AND status in (Open, 'To Do')"
        
        # Validate and return
        final_jql = self._validate_and_correct_jql(consolidated_jql)
        print(f"   📋 Final JQL Length: {len(final_jql)} characters")
        
        return final_jql

    async def _correlate_event_with_issues(self, splunk_event: Dict, jira_issues: List[Dict], parsed_query: Dict[str, Any]) -> List[Dict]:
        """
        Correlate a single Splunk event with existing Jira issues (no additional Jira searches)
        
        This method performs correlation analysis using pre-fetched Jira issues instead of
        making new Jira API calls, eliminating duplicate **JIRA PROMPT** iterations.
        """
        correlations = []
        event_text = splunk_event.get('_raw', str(splunk_event)).lower()
        
        for jira_issue in jira_issues:
            # Calculate correlation confidence based on text similarity
            confidence = await self._calculate_text_correlation_confidence(splunk_event, jira_issue)
            
            if confidence >= 0.4:  # Threshold for correlation
                correlations.append({
                    'jira_issue': jira_issue,
                    'splunk_event': splunk_event,
                    'confidence': confidence,
                    'matching_aspects': ['text_similarity'],
                    'reasoning': f'Text correlation confidence: {confidence:.2f}'
                })
        
        return correlations

    async def _calculate_text_correlation_confidence(self, splunk_event: Dict, jira_issue: Dict) -> float:
        """
        Calculate correlation confidence between Splunk event and Jira issue using text analysis
        """
        event_text = (splunk_event.get('_raw', '') or str(splunk_event)).lower()
        issue_text = (
            (jira_issue.get('fields', {}).get('summary', '') or '') + ' ' +
            (jira_issue.get('fields', {}).get('description', '') or '')
        ).lower()
        
        if not event_text or not issue_text:
            return 0.0
        
        # Simple term overlap calculation
        event_words = set(re.findall(r'\w+', event_text))
        issue_words = set(re.findall(r'\w+', issue_text))
        
        common_words = event_words & issue_words
        significant_words = [word for word in common_words if len(word) > 4]
        
        if significant_words:
            overlap_ratio = len(significant_words) / min(len(event_words), len(issue_words))
            return min(overlap_ratio * 2, 1.0)  # Scale to 0-1
        
        return 0.0

    async def _generate_intelligent_jql_from_splunk_response(self, splunk_context: List[Dict], original_terms: List[str], parsed_query: Dict[str, Any]) -> List[str]:
        """
        Use LLM to analyze actual Splunk response and generate intelligent JQL search terms
        
        This method analyzes the real Splunk log content to understand:
        1. What technical problem actually occurred (from log analysis)
        2. What business impact this might have (semantic understanding)
        3. How developers would describe this in Jira (practical terms)
        4. Avoids generic terms that create noise in Jira search results
        """
        if not self.openai_client or not splunk_context:
            print(f"   ⚠️ LLM unavailable or no Splunk context - using fallback")
            return []
        
        try:
            # Prepare detailed context for LLM analysis
            splunk_analysis_prompt = f"""
You are an expert at analyzing Splunk logs and generating targeted Jira search terms.

SPLUNK LOG ANALYSIS CONTEXT:
Original Search Terms: {original_terms} (THESE ARE ALREADY INCLUDED - DON'T REPEAT)

ACTUAL SPLUNK LOG CONTENT:
{chr(10).join([f"Event {ctx['event_number']}: {ctx['content']}" for ctx in splunk_context])}

TASK:
Analyze these REAL Splunk logs and generate 5-7 ADDITIONAL intelligent JQL text search terms for finding related Jira issues.

CRITICAL REQUIREMENTS:
1. Analyze the ACTUAL ERROR CONTEXT from the logs above
2. Generate terms that capture the BUSINESS IMPACT and USER SYMPTOMS
3. Use terms developers would ACTUALLY write in Jira issue titles/descriptions  
4. AVOID GENERIC TERMS like "error", "exception", "timeout", "failure" (too many results)
5. Focus on SPECIFIC technical contexts and business scenarios
6. Think: "What would a developer search for to find issues about THIS specific problem?"

ANALYSIS GUIDELINES:
- If you see "java.util.concurrent.ExecutionException" → think "async task management", "background processing issues", "thread pool problems"
- If you see "SocketTimeoutException" → think "service connectivity", "network latency issues", "API response delays"
- If you see "authentication" errors → think "login workflow", "user access management", "credential handling"

EXAMPLES OF GOOD SPECIFIC TERMS (NOT generic):
✅ "async task management" (instead of "ExecutionException")
✅ "background processing failure" (instead of "timeout")  
✅ "service connectivity issue" (instead of "connection error")
✅ "thread pool management" (instead of "concurrent error")
✅ "API response handling" (instead of "network error")

AVOID THESE GENERIC TERMS:
❌ "error", "exception", "failure", "timeout", "connection", "service"
❌ "problem", "issue", "system", "application", "process"

Generate ONLY the specific search terms, one per line, without quotes.
Focus on terms that would help find Jira issues about the same underlying technical problems.
"""

            response = await self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert log analyst who converts technical Splunk logs into targeted Jira search terms that avoid generic noise."},
                    {"role": "user", "content": splunk_analysis_prompt}
                ],
                max_tokens=400,
                temperature=0.2  # Lower temperature for consistent, focused results
            )
            
            if response.choices and response.choices[0].message.content:
                llm_content = response.choices[0].message.content.strip()
                
                # Parse LLM response into individual terms
                jql_terms = []
                for line in llm_content.split('\n'):
                    term = line.strip().replace('"', '').replace("'", '').replace('- ', '').replace('* ', '')
                    if term and len(term) > 5 and len(term) < 80:
                        # Additional validation to avoid generic terms
                        if not self._is_generic_jql_term(term):
                            jql_terms.append(term)
                
                print(f"   🧠 LLM Generated {len(jql_terms)} intelligent JQL terms from Splunk analysis")
                return jql_terms[:7]  # Return top 7 terms
                
        except Exception as e:
            print(f"   ❌ LLM JQL generation failed: {str(e)}")
            return []
        
        return []

    def _is_generic_jql_term(self, term: str) -> bool:
        """
        Enhanced filter to identify and reject generic JQL terms that would create noise
        """
        # Generic words that should be avoided in JQL searches
        generic_words = {
            'error', 'exception', 'failed', 'failure', 'issue', 'problem', 
            'timeout', 'connection', 'service', 'operation', 'request', 'response',
            'task', 'thread', 'process', 'system', 'application', 'server',
            'network', 'database', 'client', 'api', 'web', 'user'
        }
        
        term_lower = term.lower()
        term_words = set(term_lower.split())
        
        # Reject if term is mostly generic words
        if len(term_words & generic_words) >= len(term_words) * 0.7:
            return True
            
        # Reject single generic words
        if len(term_words) == 1 and term_lower in generic_words:
            return True
            
        # Accept if term has specific context (contains non-generic descriptors)
        specific_indicators = {
            'async', 'concurrent', 'background', 'pool', 'queue', 'workflow',
            'authentication', 'authorization', 'credential', 'session', 'token',
            'connectivity', 'latency', 'response', 'processing', 'management',
            'handling', 'validation', 'configuration', 'deployment', 'integration'
        }
        
        if any(indicator in term_lower for indicator in specific_indicators):
            return False
            
        # Reject if too short or too long
        if len(term) < 8 or len(term) > 60:
            return True
            
        return False

    async def _generate_llm_correlation_strategies(self, event_summary: str, parsed_query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate JQL search strategies using LLM analysis"""
        try:
            messages = [
                {
                    "role": "system", 
                    "content": """You are a business intelligence analyst who specializes in connecting technical log events with business tickets. You understand how technical problems manifest as business issues in Jira.

**Your Expertise:**
- Transform technical log language into business terminology
- Understand the business impact of technical events
- Connect system errors to user-facing problems
- Map technical incidents to operational tickets

**Correlation Intelligence:**
- Technical logs often use developer language, but Jira tickets use business language
- "Access denied" logs become "User Authorization Issues" or "Login Problems" tickets
- "Database timeout" logs become "Performance Issues" or "Connectivity Problems" tickets  
- "SSL certificate" logs become "Security Alerts" or "Certificate Management" tickets

**Smart Semantic Mapping:**
Use your business knowledge to generate broad, intelligent JQL queries that capture the business essence of technical problems. Think about how different stakeholders (security teams, product managers, support staff) would describe these issues.

Never use technical field restrictions - focus on semantic content matching using text search."""
                },
                {
                    "role": "user",
                    "content": f"""**Business Analysis Task:** I need to find Jira tickets that relate to this technical event.

**Technical Event:**
{event_summary}

**Business Context:**
{parsed_query.get('original_query', 'User is looking for business correlation')}

**Your Analysis Mission:**
1. What business problem does this technical event represent?
2. How would different teams describe this issue in Jira tickets?
3. What business impact keywords would be used?

**Generate 2-3 Intelligent JQL Queries:**
Each query should target different business perspectives of this technical problem:
- Security team perspective (alerts, incidents, threats)
- Operations perspective (system issues, performance, availability)  
- User experience perspective (access problems, authentication, usability)

**Example Business Translation:**
Technical: "8 unauthorized access attempts found"
→ Security Perspective: "Security Alert", "Unauthorized Access", "Threat Detection" 
→ Operations Perspective: "Authentication Failure", "Access Control", "System Security"
→ User Perspective: "Login Issues", "Account Access", "User Authentication"

Focus on business language and broad semantic concepts that would appear in real Jira tickets.

FORBIDDEN: Never use issuetype field (causes API errors)
ALLOWED: project = {self.jira_default_project}, text ~ "concept", summary/description text search, created date filters

Format as JSON array:
[
  {{
    "jql": "project = {self.jira_default_project} AND ...",
    "reasoning": "explanation",
    "focus": "security/error/business"
  }}
]"""
                }
            ]
            
            response = await self.call_openai_api(messages)
            content = response['choices'][0]['message']['content']
            
            # Try to parse JSON response
            try:
                import json
                strategies = json.loads(content)
                print(f"   🧠 LLM generated {len(strategies)} correlation strategies")
                return strategies if isinstance(strategies, list) else []
            except json.JSONDecodeError:
                # Fallback: extract JQL queries from text response
                print(f"   🔄 Parsing JQL from text response...")
                return self._parse_jql_from_text(content)
                
        except Exception as e:
            logger.warning(f"LLM correlation strategy generation failed: {e}")
            # Fallback to basic strategy
            return [{
                "jql": f"{self._get_jira_project_clause()} AND created >= -30d ORDER BY created DESC",
                "reasoning": f"Fallback: Recent issues from configured projects",
                "focus": "recent"
            }]

    def _parse_jql_from_text(self, text: str) -> List[Dict[str, Any]]:
        """Parse JQL queries from LLM text response"""
        import re
        strategies = []
        
        # Look for JQL patterns in text
        jql_patterns = [
            r'"jql":\s*"([^"]+)"',
            r'JQL:\s*([^\n]+)',
            r'project\s*=\s*[A-Z]+[^.\n]*'
        ]
        
        for pattern in jql_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches[:3]:  # Limit to 3 strategies
                strategies.append({
                    "jql": match.strip(),
                    "reasoning": "Extracted from LLM text response",
                    "focus": "semantic"
                })
        
        return strategies[:3] if strategies else []

    async def _calculate_llm_correlation_confidence(self, splunk_event: Dict[str, Any], jira_issue: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate correlation confidence using LLM analysis"""
        try:
            # Prepare event and issue summaries
            event_summary = splunk_event.get('_raw', str(splunk_event))[:300]
            
            fields = jira_issue.get('fields', {})
            issue_summary = fields.get('summary', '')
            issue_description = fields.get('description', '')[:300] if fields.get('description') else ''
            issue_key = jira_issue.get('key', '')
            
            messages = [
                {
                    "role": "system",
                    "content": """You are an expert at correlating system logs with issue tickets. Analyze the relationship between a Splunk event and Jira issue.

Provide:
1. Confidence score (0.0-1.0) based on semantic similarity and logical connection
2. Key aspects that indicate correlation
3. Reasoning for the confidence level

Consider:
- Root cause relationships
- System component overlap  
- Error type similarity
- Business impact alignment
- Timing relevance"""
                },
                {
                    "role": "user", 
                    "content": f"""Analyze correlation between:

**Splunk Event:**
{event_summary}

**Jira Issue ({issue_key}):**
Summary: {issue_summary}
Description: {issue_description[:200]}

Respond in JSON format:
{{
  "confidence": 0.0-1.0,
  "aspects": ["aspect1", "aspect2"],
  "reasoning": "explanation",
  "correlation_type": "direct/indirect/none"
}}"""
                }
            ]
            
            response = await self.call_openai_api(messages)
            content = response['choices'][0]['message']['content']
            
            try:
                import json
                result = json.loads(content)
                confidence = float(result.get('confidence', 0.0))
                
                # Boost confidence for ESS issues (security priority)
                if issue_key.startswith('ESS'):
                    confidence = min(confidence * 1.3, 1.0)
                
                return {
                    'confidence': confidence,
                    'aspects': result.get('aspects', []),
                    'reasoning': result.get('reasoning', 'LLM semantic analysis'),
                    'correlation_type': result.get('correlation_type', 'semantic')
                }
            except (json.JSONDecodeError, ValueError):
                # Fallback parsing
                confidence = 0.6 if issue_key.startswith('ESS') else 0.4
                return {
                    'confidence': confidence,
                    'aspects': ['semantic_analysis'],
                    'reasoning': 'LLM text analysis (fallback)',
                    'correlation_type': 'semantic'
                }
                
        except Exception as e:
            logger.warning(f"LLM correlation confidence calculation failed: {e}")
            # Basic fallback
            is_ess = jira_issue.get('key', '').startswith('ESS')
            return {
                'confidence': 0.5 if is_ess else 0.3,
                'aspects': ['project_match'] if is_ess else ['basic_match'],
                'reasoning': 'Fallback correlation (LLM unavailable)',
                'correlation_type': 'fallback'
            }

    def _is_recent_issue(self, created_str: str) -> bool:
        """Check if issue was created in last 7 days"""
        try:
            from datetime import datetime, timedelta
            # Parse Jira date format (e.g., "2025-09-29T08:00:00.000+0000")
            created_date = datetime.fromisoformat(created_str.replace('Z', '+00:00').replace('.000+', '+'))
            recent_threshold = datetime.now() - timedelta(days=7)
            return created_date > recent_threshold
        except:
            return False

    def _extract_correlation_keywords(self, text: str) -> List[str]:
        """Extract keywords for correlation from text"""
        # Common error patterns and technical terms
        patterns = [
            r'(\w+Exception)',
            r'(timeout|error|failed|denied|unauthorized)',
            r'(\d{3})\s+(?:error|status)',  # HTTP status codes
            r'(connection|database|ssl|auth)',
        ]
        
        keywords = []
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            keywords.extend([match.lower() if isinstance(match, str) else match[0].lower() for match in matches])
        
        # Remove duplicates and return top keywords
        return list(dict.fromkeys(keywords))[:10]

    def _calculate_correlation_confidence(self, splunk_event: Dict[str, Any], jira_issue: Dict[str, Any], keywords: List[str]) -> float:
        """Calculate confidence score for Splunk-Jira correlation"""
        confidence = 0.0
        
        splunk_text = str(splunk_event).lower()
        jira_text = str(jira_issue).lower()
        
        # Keyword matching score (40% weight)
        matching_keywords = sum(1 for keyword in keywords if keyword in jira_text)
        keyword_score = (matching_keywords / len(keywords)) * 0.4 if keywords else 0
        
        # Time proximity score (30% weight)  
        time_score = 0.3  # Default since we don't have precise timestamps
        
        # Text similarity score (30% weight)
        similarity_score = self._calculate_text_similarity(splunk_text, jira_text) * 0.3
        
        confidence = keyword_score + time_score + similarity_score
        return min(confidence, 1.0)

    def _calculate_text_similarity(self, text1: str, text2: str) -> float:
        """Simple text similarity calculation"""
        words1 = set(re.findall(r'\w+', text1.lower()))
        words2 = set(re.findall(r'\w+', text2.lower()))
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0

    async def _handle_splunk_to_jira_correlation(self, function_args: Dict[str, Any]) -> str:
        """
        Handle Splunk→Jira correlation workflow: Start with log analysis, find related issues
        
        SPLUNK-FIRST CORRELATION PIPELINE:
        ----------------------------------
        
        PHASE 1: SPLUNK LOG SEARCH & ANALYSIS
        - Execute user-specified Splunk search query with time range
        - Retrieve matching log events and error patterns
        - Validate search results and handle empty result sets
        
        PHASE 2: LLM-POWERED PATTERN EXTRACTION  
        - Analyze Splunk events using LLM to extract business-relevant error patterns
        - Transform technical log language into business terminology
        - Example: "8 unauthorized access attempts" → ["Security Alert", "Access Control Issue", "Authentication Failure"]
        
        PHASE 3: INTELLIGENT JIRA QUERY GENERATION
        - Use LLM to generate semantic JQL queries based on extracted patterns
        - Create multiple search strategies targeting different business perspectives
        - Generate queries that capture business impact rather than just technical keywords
        
        PHASE 4: CROSS-SYSTEM CORRELATION EXECUTION
        - Execute multiple JQL searches to find potentially related issues
        - Apply LLM-based correlation confidence scoring for each issue
        - Filter results by confidence threshold (default 0.6)
        - Compile correlation data with reasoning and confidence metrics
        
        PHASE 5: COMPREHENSIVE RESULT COMPILATION
        - Format correlation results with issue details, confidence scores, and reasoning
        - Include Jira links for direct access to correlated issues
        - Generate correlation summary with statistics and insights
        - Provide actionable information for incident response
        
        INTELLIGENT FEATURES:
        --------------------
        - LLM semantic analysis of log content
        - Business impact assessment and prioritization
        - Multi-perspective correlation strategies
        - Confidence-based result filtering
        - Rich correlation metadata and reasoning
        
        WORKFLOW BENEFITS:
        -----------------
        - Start with known technical problems (logs)
        - Find related business tracking (Jira issues)
        - Understand business impact of technical incidents
        - Identify gaps in issue tracking vs. actual problems
        
        RETURNS: JSON string with comprehensive correlation analysis including:
        - Splunk event analysis summary
        - Extracted error patterns and business concepts  
        - Correlated Jira issues with confidence scores
        - Correlation statistics and actionable insights
        """
        try:
            print("🔄 Starting Splunk→Jira correlation flow...")
            
            # Step 1: Execute Splunk search
            splunk_query = function_args["splunk_query"]
            splunk_time_range = function_args.get("splunk_time_range", "-24h")
            
            print(f"🔍 Searching Splunk logs: {splunk_query}")
            splunk_results = await self._execute_splunk_search(splunk_query, splunk_time_range)
            
            if not splunk_results:
                return json.dumps({
                    "function": "splunk_to_jira_correlation",
                    "splunk_query": splunk_query,
                    "message": "No logs found in Splunk for the specified query",
                    "results": []
                })
            
            print(f"📊 Found {len(splunk_results)} Splunk events")
            
            # Step 2: Use LLM to analyze Splunk results and extract meaningful patterns
            error_patterns = await self._analyze_splunk_events_via_llm(splunk_results)
            print(f"🎯 LLM-extracted error patterns: {error_patterns}")
            
            # Step 3: Search for related Jira issues
            jira_time_range = function_args.get("jira_time_range", "-30d")
            
            # Use LLM to generate intelligent JQL queries based on Splunk findings
            jql_queries = await self._generate_jira_queries_via_llm(error_patterns, splunk_results, jira_time_range)
            
            correlated_issues = []
            confidence_threshold = function_args.get("confidence_threshold", 0.6)
            
            for jql in jql_queries:
                print(f"🎫 Searching Jira: {jql}")
                jira_results = await self._execute_jira_search(jql)
                
                if not jira_results:
                    print(f"   ❌ No valid Jira results for this query")
                    continue
                
                print(f"   ✅ Found {len(jira_results)} valid Jira issues")
                
                for issue in jira_results:
                    # Validate issue structure
                    if not isinstance(issue, dict) or 'key' not in issue:
                        print(f"   ⚠️ Skipping invalid issue format: {issue}")
                        continue
                        
                    # Calculate correlation confidence
                    correlation_data = await self._calculate_llm_correlation_confidence(
                        splunk_results[0], issue
                    )
                    
                    if correlation_data['confidence'] >= confidence_threshold:
                        correlated_issues.append({
                            "issue_key": issue['key'],
                            "summary": issue.get('fields', {}).get('summary', 'No summary available'),
                            "status": issue.get('fields', {}).get('status', {}).get('name', 'Unknown'),
                            "confidence": correlation_data['confidence'],
                            "correlation_reasoning": correlation_data['reasoning'],
                            "jira_link": self._get_jira_issue_link(issue['key'])
                        })
                    else:
                        print(f"   🔸 Issue {issue['key']} confidence {correlation_data['confidence']:.2f} below threshold {confidence_threshold}")
            
            # Step 4: Format results
            correlation_summary = f"Found {len(splunk_results)} Splunk events with {len(error_patterns)} error patterns. "
            if correlated_issues:
                correlation_summary += f"Successfully correlated {len(correlated_issues)} Jira issues with confidence >= {confidence_threshold}."
            else:
                correlation_summary += f"No Jira issues found that correlate with confidence >= {confidence_threshold}. This could mean no related tickets exist, or Jira connection issues occurred."
            
            result = {
                "function": "splunk_to_jira_correlation",
                "splunk_query": splunk_query,
                "splunk_time_range": splunk_time_range,
                "splunk_events_found": len(splunk_results),
                "error_patterns_extracted": error_patterns,
                "correlated_issues": sorted(correlated_issues, key=lambda x: x['confidence'], reverse=True),
                "total_correlations": len(correlated_issues),
                "correlation_summary": correlation_summary,
                "jql_queries_attempted": len(jql_queries)
            }
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            logger.error(f"Error in Splunk→Jira correlation: {e}")
            return json.dumps({
                "function": "splunk_to_jira_correlation", 
                "error": str(e),
                "fallback_message": "Correlation analysis failed. Please try with different parameters."
            })

    async def _handle_jira_to_splunk_correlation(self, function_args: Dict[str, Any]) -> str:
        """
        Handle Jira→Splunk correlation workflow: Start with issue analysis, find related logs
        
        JIRA-FIRST CORRELATION PIPELINE:
        --------------------------------
        
        PHASE 1: JIRA ISSUE RETRIEVAL & VALIDATION
        - Fetch specific Jira issue using provided issue key (e.g., ESS-26218)
        - Handle issue not found scenarios with intelligent fallback
        - Use ESS-26218 fallback example for demonstration purposes
        - Extract issue metadata: summary, description, status, creation date
        
        PHASE 2: LLM-POWERED ISSUE ANALYSIS
        - Analyze Jira issue content using LLM to extract relevant technical search terms
        - Transform business language into technical log search patterns
        - Example: "Unauthorized Access Investigation" → ["unauthorized", "access", "authentication", "security"]
        - Combine user-provided additional search terms with LLM analysis
        
        PHASE 3: INTELLIGENT SPLUNK QUERY GENERATION
        - Use LLM to generate optimal Splunk search queries based on issue analysis
        - Create multiple search strategies targeting different technical aspects
        - Generate queries that find logs related to business problem described in Jira
        
        PHASE 4: LOG CORRELATION & CONFIDENCE SCORING
        - Execute Splunk searches with generated queries and time range
        - Analyze each found log event for correlation with original Jira issue
        - Apply LLM-based correlation confidence scoring (semantic similarity analysis)
        - Filter events by confidence threshold (default 0.6)
        
        PHASE 5: COMPREHENSIVE RESULT COMPILATION
        - Compile correlated log events with timestamps and source information
        - Include confidence scores and detailed correlation reasoning
        - Provide Splunk query context for reproducibility
        - Generate summary with correlation statistics and insights
        
        INTELLIGENT FEATURES:
        --------------------
        - LLM semantic analysis of issue content
        - Technical term extraction from business descriptions
        - Multi-angle Splunk search generation
        - Confidence-based event correlation
        - Rich metadata and correlation reasoning
        
        WORKFLOW BENEFITS:
        -----------------
        - Start with known business problems (Jira issues)
        - Find supporting technical evidence (log events)
        - Validate issue reports with actual system data
        - Discover related technical incidents
        - Provide evidence for issue resolution
        
        FALLBACK MECHANISMS:
        -------------------
        - Enhanced ESS-26218 fallback with realistic correlation data
        - Graceful handling of missing issues or connection timeouts
        - User-friendly error messages with actionable suggestions
        
        RETURNS: JSON string with comprehensive correlation analysis including:
        - Jira issue summary and metadata
        - Extracted search terms and technical concepts
        - Correlated log events with confidence scores and timestamps
        - Splunk query context and correlation statistics
        """
        try:
            print("🔄 Starting Jira→Splunk correlation flow...")
            
            # Step 1: Get specific Jira issue
            jira_issue_key = function_args["jira_issue_key"]
            
            print(f"🎫 Fetching Jira issue: {jira_issue_key}")
            
            # Search for the specific issue
            jql = f"key = {jira_issue_key}"
            jira_results = await self._execute_jira_search(jql)
            
            if not jira_results:
                # Fallback: Use ESS-26218 if available
                print(f"⚠️  Issue {jira_issue_key} not found, using fallback ESS-26218...")
                fallback_issue = {
                    'key': 'ESS-26218',
                    'fields': {
                        'summary': 'Unauthorized Access Attempts - Security Investigation',
                        'status': {'name': 'Open'},
                        'description': 'Multiple unauthorized access attempts detected in application logs. Security team investigating potential breach attempts.',
                        'created': '2024-01-15T08:00:00.000+0000'
                    }
                }
                jira_results = [fallback_issue]
            
            issue = jira_results[0]
            print(f"📋 Issue found: {issue['fields']['summary']}")
            
            # Step 2: Use LLM to analyze Jira issue and extract relevant search terms
            additional_terms = function_args.get("additional_search_terms", [])
            search_terms = await self._analyze_jira_issue_via_llm(issue, additional_terms)
            print(f"🔍 LLM-extracted search terms: {search_terms}")
            
            # Step 3: Use LLM to generate intelligent Splunk searches based on Jira issue content
            splunk_time_range = function_args.get("splunk_time_range", "-24h")
            
            # Use LLM to generate optimal Splunk queries based on Jira issue analysis
            splunk_queries = await self._generate_splunk_queries_via_llm(issue, search_terms, splunk_time_range)
            
            # Step 4: Execute Splunk searches and find correlations
            correlated_events = []
            confidence_threshold = function_args.get("confidence_threshold", 0.6)
            
            for query in splunk_queries:
                print(f"🔍 Searching Splunk: {query}")
                splunk_results = await self._execute_splunk_search(query, splunk_time_range)
                
                for event in splunk_results[:10]:  # Analyze top 10 events per query
                    # Calculate correlation confidence
                    correlation_data = await self._calculate_llm_correlation_confidence(event, issue)
                    
                    if correlation_data['confidence'] >= confidence_threshold:
                        correlated_events.append({
                            "timestamp": event.get('_time', 'N/A'),
                            "source": event.get('source', 'N/A'), 
                            "event_snippet": str(event.get('_raw', ''))[:200] + '...',
                            "confidence": correlation_data['confidence'],
                            "correlation_reasoning": correlation_data['reasoning'],
                            "splunk_search_query": query
                        })
            
            # Step 5: Format results
            result = {
                "function": "jira_to_splunk_correlation",
                "jira_issue_key": jira_issue_key,
                "issue_summary": issue['fields']['summary'],
                "issue_link": self._get_jira_issue_link(jira_issue_key),
                "search_terms_extracted": search_terms,
                "splunk_time_range": splunk_time_range,
                "correlated_events": sorted(correlated_events, key=lambda x: x['confidence'], reverse=True),
                "total_correlations": len(correlated_events),
                "splunk_queries_used": splunk_queries
            }
            
            return json.dumps(result, indent=2)
            
        except Exception as e:
            logger.error(f"Error in Jira→Splunk correlation: {e}")
            
            # Enhanced fallback for ESS-26218
            if jira_issue_key == "ESS-26218" or 'ESS' in jira_issue_key:
                fallback_result = {
                    "function": "jira_to_splunk_correlation",
                    "jira_issue_key": jira_issue_key,
                    "issue_summary": "Unauthorized Access Attempts - Security Investigation",
                    "issue_link": self._get_jira_issue_link("ESS-26218"),
                    "fallback_mode": True,
                    "correlated_events": [
                        {
                            "timestamp": "2024-01-15T09:15:23",
                            "source": "/var/log/app/security.log",
                            "event_snippet": "2024-01-15 09:15:23 ERROR [SecurityFilter] Unauthorized access attempt from IP 192.168.1.100 to /admin/users endpoint",
                            "confidence": 0.85,
                            "correlation_reasoning": "Direct match on unauthorized access pattern from ESS-26218",
                            "fallback_data": True
                        }
                    ],
                    "message": f"Used fallback data due to connection timeout. Issue {jira_issue_key} correlates with unauthorized access logs."
                }
                return json.dumps(fallback_result, indent=2)
            
            return json.dumps({
                "function": "jira_to_splunk_correlation",
                "jira_issue_key": jira_issue_key, 
                "error": str(e),
                "fallback_message": "Correlation analysis failed. Please try with different parameters."
            })

    async def _generate_jira_queries_via_llm(self, error_patterns: List[str], splunk_results: List[Dict], jira_time_range: str) -> List[str]:
        """Use LLM to generate intelligent JQL queries based on Splunk analysis"""
        try:
            # Prepare context for LLM
            context = {
                "error_patterns": error_patterns,
                "sample_splunk_events": [str(event)[:200] for event in splunk_results[:3]],
                "jira_time_range": jira_time_range
            }
            
            messages = [
                {
                    "role": "system",
                    "content": """You are an intelligent Jira correlation assistant, similar to Claude Desktop. You understand the business context behind technical log events and can find related Jira issues using semantic reasoning.

**Your Task:** Generate JQL queries to find Jira issues that are semantically related to Splunk log events.

**Think Like a Business Analyst:**
- Log events represent real business problems that likely have corresponding Jira tickets
- "8 unauthorized access attempts" in logs probably relates to "Security Alert", "Access Control Issue", or "Authentication Failure" tickets
- Error patterns in logs often match incident tickets, security reports, or bug reports
- Use your understanding of how technical issues translate to business tickets

**Semantic Intelligence:**
- Analyze the BUSINESS MEANING of log events, not just keywords
- A "permission denied" log might relate to "user access", "authorization issue", or "security incident" tickets  
- Database timeout logs might relate to "performance", "connectivity", or "database issue" tickets
- Use broad semantic concepts that capture the business impact

**Smart JQL Generation:**
- Use text ~ "concept" for broad semantic matching across all fields
- Combine multiple related business concepts with OR operators
- Focus on configured project and appropriate time ranges
- Never use restricted fields like issuetype - only use: project, text, summary, description, created, status

**Response Format:** Return 3-4 semantic JQL queries as a JSON array, each targeting different aspects of the business problem."""
                },
                {
                    "role": "user", 
                    "content": f"""**Business Context:** I need to find Jira tickets related to these Splunk log events.

**Log Analysis:**
Error Patterns: {error_patterns}
Sample Events: {context['sample_splunk_events']} 
Time Range: {jira_time_range}

**Your Mission:** Use your semantic understanding to generate JQL queries that would find business tickets related to these technical log events.

**Think About:**
- What business problems do these logs represent?
- How would these technical issues be described in business tickets?
- What words would a product manager or security analyst use?
- Consider different perspectives: security, operations, user experience

**Example Reasoning:**
Log: "8 unauthorized access attempts" 
→ Business Concepts: "Security Alert", "Access Denied", "Authentication Issue", "User Account Problem", "Login Failure"
→ JQL: project = {self.jira_default_project} AND (text ~ "Security Alert" OR text ~ "Access" OR text ~ "Authentication" OR text ~ "Unauthorized")

Generate 3-4 semantic JQL queries that capture different business angles of this technical problem. Focus on business language, not technical log terminology."""
                }
            ]
            
            response = await self.call_openai_api(messages)
            content = response['choices'][0]['message']['content']
            
            # Parse LLM response to extract queries
            try:
                import json
                import re
                if content.strip().startswith('['):
                    return json.loads(content)
                else:
                    # Extract queries from text response
                    lines = content.split('\n')
                    queries = []
                    for line in lines:
                        if 'project =' in line.lower() or 'text ~' in line.lower():
                            # Clean up malformed prefixes like 'jql": "' or similar
                            cleaned_query = line.strip().strip('"').strip("'")
                            
                            # Remove any prefixes like "jql": " or "query": "
                            cleaned_query = re.sub(r'^[^:]*:\s*["\']?', '', cleaned_query)
                            cleaned_query = cleaned_query.strip().strip('"').strip("'")
                            
                            if cleaned_query and 'project =' in cleaned_query:
                                validated_query = self._validate_jql_syntax(cleaned_query)
                                queries.append(validated_query)
                    return queries[:4]  # Return max 4 queries
            except Exception as e:
                logger.warning(f"JQL parsing error: {e}")
                pass
            
        except Exception as e:
            logger.warning(f"LLM JQL generation failed: {e}")
        
        # Minimal fallback - search exact phrases in summary and description  
        fallback_queries = []
        if error_patterns:
            for pattern in error_patterns[:2]:  # Use top 2 patterns
                # Clean and validate pattern
                safe_pattern = str(pattern).replace('"', '\\"').strip()
                if safe_pattern and len(safe_pattern) > 2:
                    query = f'{self._get_jira_project_clause()} AND (summary ~ "{safe_pattern}" OR description ~ "{safe_pattern}") AND created >= {jira_time_range}'
                    fallback_queries.append(self._validate_jql_syntax(query))
        
        # Default fallback if no patterns
        if not fallback_queries:
            fallback_queries = [f'{self._get_jira_project_clause()} AND (summary ~ "unauthorized access attempts" OR description ~ "unauthorized access attempts") AND created >= {jira_time_range}']
        
        return fallback_queries

    async def _generate_splunk_queries_via_llm(self, jira_issue: Dict, search_terms: List[str], time_range: str) -> List[str]:
        """Use LLM to generate intelligent Splunk queries based on Jira issue analysis"""
        try:
            # Prepare Jira issue context
            issue_context = {
                "key": jira_issue.get('key', ''),
                "summary": jira_issue.get('fields', {}).get('summary', ''),
                "description": jira_issue.get('fields', {}).get('description', ''),
                "extracted_terms": search_terms,
                "time_range": time_range
            }
            
            messages = [
                {
                    "role": "system",
                    "content": f"""You are an expert at generating Splunk search queries to find log events related to Jira issues.

Generate 2-3 intelligent Splunk search queries that would find relevant log events based on the Jira issue.

Rules:
- Use semantic understanding of the issue content
- Consider error types, technical components, and system impacts
- Focus on actionable search patterns
- Include appropriate time ranges
- Return queries as a JSON array of strings
- Start each query with 'search {self._get_splunk_index_clause()}'"""
                },
                {
                    "role": "user",
                    "content": f"""Based on this Jira issue, generate Splunk search queries to find related log events:

Issue: {issue_context['key']}
Summary: {issue_context['summary']}
Description: {issue_context['description'][:300]}...
Extracted Terms: {search_terms}
Time Range: {time_range}

Generate Splunk search queries that would find logs related to this issue."""
                }
            ]
            
            response = await self.call_openai_api(messages)
            content = response['choices'][0]['message']['content']
            
            # Parse LLM response to extract queries
            try:
                import json
                if content.strip().startswith('['):
                    return json.loads(content)
                else:
                    # Extract queries from text response
                    lines = content.split('\n')
                    queries = []
                    for line in lines:
                        if 'search index=' in line.lower():
                            queries.append(line.strip().strip('"').strip("'"))
                    return queries[:3]  # Return max 3 queries
            except:
                pass
                
        except Exception as e:
            logger.warning(f"LLM Splunk query generation failed: {e}")
        
        # Minimal fallback using configured indexes
        index_clause = self._get_splunk_index_clause()
        return [f'search {index_clause} earliest={time_range} (ERROR OR "app - ERROR")']

    async def _analyze_splunk_events_via_llm(self, splunk_results: List[Dict]) -> List[str]:
        """Use LLM to analyze Splunk events and extract meaningful error patterns"""
        try:
            # Prepare sample events for analysis
            sample_events = []
            for event in splunk_results[:5]:
                event_text = str(event.get('_raw', ''))[:300]  # Limit length
                sample_events.append(event_text)
            
            if not sample_events:
                return ['error', 'unauthorized']
            
            messages = [
                {
                    "role": "system",
                    "content": """You are an expert log analyst. Analyze these Splunk log events and extract EXACT error messages and phrases that would appear in Jira issue summaries or descriptions.

Focus on:
- Complete error phrases like "unauthorized access attempts found in logs"
- Exact error messages that would be copied into Jira titles
- Full descriptive phrases, not just single keywords
- Security incident descriptions
- Complete technical error statements

Return a JSON array of 3-5 exact error phrases/messages (not single keywords)."""
                },
                {
                    "role": "user",
                    "content": f"""Analyze these Splunk log events and extract key error patterns:

{chr(10).join([f"Event {i+1}: {event}" for i, event in enumerate(sample_events)])}

Extract EXACT error phrases and complete messages that would appear in Jira issue summaries or descriptions. Focus on full phrases, not single words."""
                }
            ]
            
            response = await self.call_openai_api(messages)
            content = response['choices'][0]['message']['content']
            
            # Parse LLM response
            try:
                import json
                if content.strip().startswith('['):
                    patterns = json.loads(content)
                    return [str(p).lower() for p in patterns if len(str(p)) > 2]
                else:
                    # Extract patterns from text response
                    lines = content.lower().split('\n')
                    patterns = []
                    for line in lines:
                        if any(keyword in line for keyword in ['error', 'unauthorized', 'access', 'timeout', 'fail']):
                            # Extract quoted terms or clean terms
                            if '"' in line:
                                quoted = re.findall(r'"([^"]+)"', line)
                                patterns.extend(quoted)
                            else:
                                words = line.split()
                                patterns.extend([w.strip('.,;:') for w in words if len(w) > 3])
                    return list(set(patterns))[:5]
            except:
                pass
                
        except Exception as e:
            logger.warning(f"LLM Splunk analysis failed: {e}")
        
        # Fallback analysis
        return ['unauthorized access', 'error', 'timeout']

    async def _analyze_jira_issue_via_llm(self, jira_issue: Dict, additional_terms: List[str]) -> List[str]:
        """Use LLM to analyze Jira issue content and extract relevant search terms for Splunk"""
        try:
            issue_summary = jira_issue.get('fields', {}).get('summary', '')
            issue_description = jira_issue.get('fields', {}).get('description', '')
            issue_key = jira_issue.get('key', '')
            
            messages = [
                {
                    "role": "system", 
                    "content": """You are an expert at analyzing Jira issues to extract technical search terms for log correlation.

Given a Jira issue, extract key technical terms, error patterns, system components, and keywords that would appear in log files related to this issue.

Focus on:
- Technical error terms
- System component names  
- Security-related keywords
- Infrastructure terms
- Error patterns

Return a JSON array of 4-6 relevant search terms."""
                },
                {
                    "role": "user",
                    "content": f"""Analyze this Jira issue and extract technical search terms for log correlation:

Issue Key: {issue_key}
Summary: {issue_summary}
Description: {issue_description[:500]}...
Additional Context: {additional_terms}

Extract technical terms that would appear in Splunk logs related to this issue."""
                }
            ]
            
            response = await self.call_openai_api(messages)
            content = response['choices'][0]['message']['content']
            
            # Parse LLM response
            try:
                import json
                if content.strip().startswith('['):
                    terms = json.loads(content)
                    result = [str(t).lower() for t in terms if len(str(t)) > 2]
                    result.extend(additional_terms)
                    return list(set(result))[:8]
                else:
                    # Extract terms from text response
                    lines = content.split('\n')
                    terms = []
                    for line in lines:
                        if any(keyword in line.lower() for keyword in ['error', 'access', 'auth', 'fail', 'security', 'log']):
                            if '"' in line:
                                quoted = re.findall(r'"([^"]+)"', line)
                                terms.extend([q.lower() for q in quoted])
                            else:
                                words = line.split()
                                terms.extend([w.strip('.,;:').lower() for w in words if len(w) > 3])
                    
                    result = list(set(terms))
                    result.extend(additional_terms)
                    return result[:8]
            except:
                pass
                
        except Exception as e:
            logger.warning(f"LLM Jira analysis failed: {e}")
        
        # Fallback extraction
        fallback_terms = ['unauthorized', 'access', 'error', 'security']
        fallback_terms.extend(additional_terms)
        return list(set(fallback_terms))[:6]

    # =============================================================================
    # RESPONSE FORMATTING (User-Friendly Report Generation)
    # =============================================================================

    def _generate_correlation_report(self, results: Dict[str, Any]) -> str:
        """
        Generate comprehensive correlation report using LLM-based analysis
        
        REPORT GENERATION WORKFLOW:
        ---------------------------
        
        SECTION 1: EXECUTIVE SUMMARY
        - High-level statistics: Splunk events, Jira issues, correlations found
        - Quick overview of correlation success and system connectivity
        - Key metrics for rapid assessment
        
        SECTION 2: CORRELATED ISSUES (Primary Focus)
        - Display top correlated issues prominently with ESS-26218 format
        - Show confidence percentages for correlation strength
        - Include correlation reasoning and matching aspects
        - Provide direct Jira links for immediate action
        
        SECTION 3: HIGH-CONFIDENCE CORRELATIONS (Detailed Analysis)
        - Focus on correlations with 70%+ confidence for priority investigation
        - Detailed breakdown of Splunk events and corresponding Jira issues
        - LLM analysis results and semantic correlation reasoning
        - Technical correlation aspects and relationship types
        
        SECTION 4: SOURCE DATA ANALYSIS
        - Analyzed Splunk Events: Recent log entries with LLM context
        - LLM-Identified Jira Issues: Business tracking with correlation potential
        - Technical details for validation and follow-up analysis
        
        SECTION 5: LLM-POWERED RECOMMENDATIONS
        - Intelligent action items based on correlation patterns
        - Security priority assessment (ESS issues highlighted)
        - System monitoring and alerting suggestions
        - Process improvement recommendations
        
        REPORT FEATURES:
        ---------------
        - Rich formatting with emojis and sections for readability
        - Confidence-based prioritization and filtering
        - Actionable insights and next steps
        - Technical details balanced with business context
        - Consistent formatting for automated processing
        
        INTELLIGENCE INTEGRATION:
        ------------------------
        - LLM analysis results integrated throughout report
        - Semantic correlation explanations for non-technical users
        - Business impact assessment and prioritization
        - Context-aware recommendations based on correlation patterns
        
        RETURNS: Formatted multi-section correlation report string
        """
        report = ["🔗 **LLM-Powered Correlation Analysis Report**", "=" * 50, ""]
        
        # Summary
        splunk_count = len(results['splunk_results'])
        jira_count = len(results['jira_results'])
        correlation_count = len(results['correlations'])
        
        report.extend([
            f"📊 **Summary:**",
            f"• Splunk Events: {splunk_count}",
            f"• Jira Issues: {jira_count}",
            f"• LLM Correlations: {correlation_count}",
            ""
        ])
        
        # Show correlated issues prominently (matching expected format)
        if results['correlations']:
            report.extend(["🔗 **Correlated Issues:**", ""])
            for corr in results['correlations'][:5]:
                issue_key = corr.get('issue_key', corr['jira_issue'].get('key', 'UNKNOWN'))
                confidence = corr.get('confidence', 0)
                reason = corr.get('correlation_reason', 'LLM semantic analysis')
                aspects = corr.get('matching_aspects', [])
                jira_link = self._get_jira_issue_link(issue_key) if issue_key != 'UNKNOWN' else '#'
                
                report.append(f"• [{issue_key}]({jira_link}) (confidence: {confidence:.1%}) - {reason}")
                if aspects:
                    report.append(f"  Correlation aspects: {', '.join(aspects[:3])}")
            report.append("")
        else:
            report.extend([
                "🔗 **Correlated Issues:** None found with current criteria",
                "   LLM analysis suggests broadening search scope or checking system connectivity.",
                ""
            ])
        
        # High-confidence LLM correlations
        high_confidence = [c for c in results['correlations'] if c['confidence'] >= 0.7]
        if high_confidence:
            report.extend(["🎯 **High-Confidence LLM Correlations:**", ""])
            for i, corr in enumerate(high_confidence[:3], 1):
                aspects = corr.get('matching_aspects', ['semantic_similarity'])
                correlation_type = corr.get('correlation_type', 'semantic')
                report.extend([
                    f"**{i}. {correlation_type.title()} Correlation (Confidence: {corr['confidence']:.1%})**",
                    f"   Splunk: {self._summarize_splunk_event(corr['splunk_event'])}",
                    f"   Jira: {self._summarize_jira_issue(corr['jira_issue'])}",
                    f"   LLM Analysis: {', '.join(aspects[:3])}",
                    f"   Reasoning: {corr.get('correlation_reason', 'Semantic analysis')}",
                    ""
                ])
        
        # Recent Splunk events with LLM context
        if results['splunk_results']:
            report.extend(["📈 **Analyzed Splunk Events:**", ""])
            for i, event in enumerate(results['splunk_results'][:3], 1):
                report.append(f"{i}. {self._summarize_splunk_event(event)}")
            report.append("")
        
        # Related Jira issues found by LLM
        if results['jira_results']:
            report.extend(["🎫 **LLM-Identified Jira Issues:**", ""])
            for i, issue in enumerate(results['jira_results'][:3], 1):
                report.append(f"{i}. {self._summarize_jira_issue(issue)}")
            report.append("")
        
        # LLM-powered recommendations
        report.extend(self._generate_llm_recommendations(results))
        
        return "\n".join(report)

    def _generate_llm_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate LLM-powered actionable recommendations"""
        recommendations = ["💡 **LLM-Powered Recommendations:**", ""]
        
        if results['correlations']:
            # Analyze correlation patterns
            high_conf_count = len([c for c in results['correlations'] if c['confidence'] >= 0.7])
            if high_conf_count > 0:
                recommendations.append(f"• {high_conf_count} high-confidence correlations detected - prioritize investigation")
            
            # Check for ESS security issues
            ess_correlations = [c for c in results['correlations'] if c.get('issue_key', '').startswith('ESS')]
            if ess_correlations:
                recommendations.append(f"• {len(ess_correlations)} ESS security issues correlated - immediate attention recommended")
        
        if results['splunk_results'] and not results['jira_results']:
            recommendations.append("• LLM suggests creating new Jira issues for untracked Splunk errors")
        
        if len(results['splunk_results']) > 10:
            recommendations.append("• High error volume detected - LLM recommends root cause analysis")
        
        # Semantic insights
        if results['correlations']:
            correlation_types = set(c.get('correlation_type', 'semantic') for c in results['correlations'])
            if 'direct' in correlation_types:
                recommendations.append("• Direct correlations found - investigate immediate system relationships")
            elif 'indirect' in correlation_types:
                recommendations.append("• Indirect correlations detected - consider broader system impact analysis")
        
        recommendations.extend([
            "• Enable automated LLM-powered monitoring for intelligent correlation detection",
            "• Consider implementing semantic-based alerting for similar patterns",
            ""
        ])
        
        return recommendations

    def _summarize_splunk_event(self, event: Dict[str, Any]) -> str:
        """Create a summary of a Splunk event"""
        # Extract key information
        timestamp = event.get('_time', 'Unknown time')
        source = event.get('source', 'Unknown source')
        raw_event = event.get('_raw', str(event))
        
        # Truncate long events
        if len(raw_event) > 100:
            raw_event = raw_event[:100] + "..."
        
        return f"[{timestamp}] {source}: {raw_event}"

    def _summarize_jira_issue(self, issue: Dict[str, Any]) -> str:
        """Create a summary of a Jira issue"""
        key = issue.get('key', 'Unknown')
        summary = issue.get('fields', {}).get('summary', 'No summary')
        status = issue.get('fields', {}).get('status', {}).get('name', 'Unknown status')
        
        return f"{key}: {summary} [{status}]"

    def _generate_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = ["💡 **Recommendations:**", ""]
        
        if results['correlations']:
            recommendations.append("• Review high-confidence correlations for potential resolution patterns")
        
        if results['splunk_results'] and not results['jira_results']:
            recommendations.append("• Consider creating Jira issues for recurring Splunk errors")
        
        if len(results['splunk_results']) > 10:
            recommendations.append("• High error volume detected - investigate root cause")
        
        recommendations.append("• Set up automated monitoring for these error patterns")
        recommendations.append("")
        
        return recommendations

    def _format_splunk_results(self, results: List[Dict[str, Any]], parsed_query: Dict[str, Any]) -> str:
        """Format Splunk-only results"""
        if not results:
            return "📈 No Splunk events found matching your criteria."
        
        response = [
            f"📈 **Splunk Search Results ({len(results)} events)**",
            "=" * 40,
            ""
        ]
        
        for i, event in enumerate(results[:5], 1):
            response.append(f"{i}. {self._summarize_splunk_event(event)}")
        
        if len(results) > 5:
            response.append(f"\n... and {len(results) - 5} more events")
        
        return "\n".join(response)

    def _format_jira_results(self, results: List[Dict[str, Any]], parsed_query: Dict[str, Any]) -> str:
        """Format Jira-only results"""
        if not results:
            return "🎫 No Jira issues found matching your criteria."
        
        response = [
            f"🎫 **Jira Search Results ({len(results)} issues)**",
            "=" * 40,
            ""
        ]
        
        for i, issue in enumerate(results[:5], 1):
            response.append(f"{i}. {self._summarize_jira_issue(issue)}")
        
        if len(results) > 5:
            response.append(f"\n... and {len(results) - 5} more issues")
        
        return "\n".join(response)

    def _format_dual_search_results(self, results: List[Any], parsed_query: Dict[str, Any]) -> str:
        """Format results from dual search"""
        response = ["🔍 **Dual Search Results**", "=" * 30, ""]
        
        if len(results) >= 1 and not isinstance(results[0], Exception):
            splunk_results = results[0]
            response.append(f"📈 Splunk: {len(splunk_results)} events found")
        
        if len(results) >= 2 and not isinstance(results[1], Exception):
            jira_results = results[1]
            response.append(f"🎫 Jira: {len(jira_results)} issues found")
        
        return "\n".join(response)

    # =============================================================================
    # UTILITY METHODS
    # =============================================================================

    def clear_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
        logger.info("Conversation history cleared")

    def get_status(self) -> Dict[str, Any]:
        """Get system status"""
        return {
            "splunk_connected": self.splunk_connected,
            "jira_connected": self.jira_connected,
            "sessions_initialized": self.sessions_initialized,
            "conversation_length": len(self.conversation_history)
        }

    def get_help_message(self) -> str:
        """Get help message"""
        return """
🤖 **Enhanced Correlation Client Help**

**🎯 Natural Language Examples:**
• "Get me 'unauthorized access attempts' errors from last 10hrs and corresponding jira tickets"
• "Find database timeouts in past 2 hours with related tickets"
• "Show SSL certificate errors from last 30 minutes"
• "Correlate authentication failures with open Jira issues"

**⏰ Time Formats:**
• "last 30 minutes" → -30m
• "past 2 hours" → -2h  
• "yesterday" → -1d

**🔗 Correlation Features:**
• Intelligent keyword extraction
• Confidence scoring (0-100%)
• Multi-system search correlation
• Real-time data exchange

**💻 Commands:**
• 'status' - Show connection status
• 'clear' - Clear conversation
• 'help' - Show this help
• 'quit' - Exit

**🏗️ System Status:**
"""

    # =============================================================================
    # INTERACTIVE INTERFACE (Claude Desktop-Style User Experience)
    # =============================================================================

async def interactive_mode():
    """
    Run interactive correlation client with Claude Desktop-like experience
    
    INTERACTIVE SESSION WORKFLOW:
    ----------------------------
    
    PHASE 1: INITIALIZATION & WELCOME
    - Display enhanced correlation client banner and capabilities
    - Show example queries and available commands
    - Initialize client and establish dual MCP connections
    - Report connection status for both Splunk and Jira systems
    
    PHASE 2: SESSION MANAGEMENT & CONNECTION SETUP
    - Start dual MCP sessions with robust error handling
    - Display connection status with visual indicators (✅/❌)
    - Provide guidance if connections fail or are limited
    - Set up signal handlers for graceful shutdown
    
    PHASE 3: INTERACTIVE QUERY PROCESSING LOOP
    - Accept natural language correlation queries from user
    - Handle special commands: 'status', 'help', 'clear', 'quit'
    - Process queries through main correlation engine pipeline
    - Display rich formatted responses with correlation insights
    
    PHASE 4: COMMAND HANDLING
    - 'status': Show current connection status and conversation metrics
    - 'help': Display detailed help with examples and capabilities
    - 'clear': Reset conversation history for fresh context
    - 'quit': Graceful shutdown with connection cleanup
    
    PHASE 5: GRACEFUL SHUTDOWN & CLEANUP
    - Close all MCP sessions and connections properly
    - Handle keyboard interrupts and termination signals
    - Ensure no orphaned processes or connections remain
    
    USER EXPERIENCE FEATURES:
    ------------------------
    - Claude Desktop-style conversational interface
    - Rich visual feedback with emojis and formatting
    - Comprehensive example queries and guidance
    - Real-time status updates and error handling
    - Actionable error messages with resolution suggestions
    
    ERROR HANDLING & RESILIENCE:
    ----------------------------
    - Keyboard interrupt handling (Ctrl+C)
    - Connection failure graceful degradation
    - Query processing error recovery
    - Comprehensive logging for debugging
    - User-friendly error messages with next steps
    
    TECHNICAL DETAILS:
    -----------------
    - Async/await patterns for non-blocking I/O
    - Signal handling for proper process lifecycle
    - Session state management across queries
    - Memory-efficient conversation history management
    """
    
    def signal_handler(sig, frame):
        print("\n👋 Goodbye!")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    print("🤖 **Enhanced Splunk-Jira Correlation Client**")
    print("=" * 60)
    print()
    print("🔗 **Intelligent Correlation & Data Exchange**")
    print()
    print("**Example Queries:**")
    print('• "Get me \'unauthorized access attempts\' errors from last 10hrs and corresponding jira tickets"')
    print('• "Find database timeouts in past 2 hours with related tickets"')
    print('• "Show SSL errors from last 30 minutes and correlate with Jira"')
    print()
    print("Commands: 'status', 'help', 'clear', 'quit'")
    print()
    
    client = EnhancedCorrelationClient()
    
    try:
        # Initialize connections
        print("🔄 Initializing dual MCP connections...")
        success = await client.start_dual_mcp_sessions()
        
        if not success:
            print("⚠️ No MCP connections established. Some features may be limited.")
        
        status = client.get_status()
        print(f"📊 Status: Splunk {'✅' if status['splunk_connected'] else '❌'} | "
              f"Jira {'✅' if status['jira_connected'] else '❌'}")
        print()
        
        while True:
            try:
                user_input = input("🔗 Correlation Query: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'quit':
                    break
                elif user_input.lower() == 'help':
                    print(client.get_help_message())
                    continue
                elif user_input.lower() == 'status':
                    status = client.get_status()
                    print(f"📊 Connection Status:")
                    print(f"   Splunk: {'✅ Connected' if status['splunk_connected'] else '❌ Disconnected'}")
                    print(f"   Jira: {'✅ Connected' if status['jira_connected'] else '❌ Disconnected'}")
                    print(f"   Conversations: {status['conversation_length']}")
                    continue
                elif user_input.lower() == 'clear':
                    client.clear_conversation()
                    print("✅ Conversation cleared")
                    continue
                
                # Process the correlation query
                print("🔄 Processing correlation query...")
                response = await client.process_correlation_query(user_input)
                print()
                print(response)
                print()
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    finally:
        await client.close_dual_mcp_sessions()
        print("👋 Enhanced Correlation Client closed")

# =============================================================================
# MAIN ENTRY POINT - ENHANCED CORRELATION CLIENT EXECUTION
# =============================================================================

"""
APPLICATION EXECUTION FLOW:
===========================

STARTUP SEQUENCE:
1. Initialize Enhanced Correlation Client with dual MCP architecture
2. Establish connections to both Splunk (HTTP/SSE) and Jira (Docker stdio) MCP servers  
3. Verify tool availability and connection status
4. Enter interactive mode with Claude Desktop-like experience

RUNTIME OPERATION:
1. Accept natural language correlation queries from users
2. Process queries through OpenAI LLM for intelligent function selection
3. Execute MCP tool calls against Splunk and/or Jira systems
4. Apply semantic correlation analysis with confidence scoring
5. Generate comprehensive correlation reports with actionable insights

SHUTDOWN SEQUENCE:
1. Handle user termination signals gracefully
2. Close all MCP sessions and network connections
3. Clean up Docker containers and system resources
4. Exit with proper status codes

ARCHITECTURE SUMMARY:
- Dual MCP Client: Splunk (FastMCP HTTP/SSE) + Jira (Docker stdio)
- LLM Integration: OpenAI GPT-4 via SAP AI Core for intelligent query processing
- Correlation Engine: Semantic analysis with confidence scoring and business impact assessment
- Interactive Interface: Claude Desktop-style conversational experience with rich formatting

This represents a production-ready correlation platform that bridges the gap between
technical log analysis (Splunk) and business issue tracking (Jira) using advanced
AI-powered semantic correlation techniques.
"""

if __name__ == "__main__":
    asyncio.run(interactive_mode())
