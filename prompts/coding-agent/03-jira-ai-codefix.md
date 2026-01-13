Here’s a well-structured prompt you can use to get detailed process, technical guidelines, and architecture recommendations from an LLM for building a tool that generates code fixes for Jira issues in a large, monolithic codebase:

---

**Prompt:**

I want to build an automated tool that generates code fixes for Jira issues in a large, monolithic codebase. The tool should:

- Parse Jira issue descriptions (including title, description, comments, and attachments like logs or screenshots)
- Analyze the relevant parts of the codebase to identify the root cause
- Generate a code fix (or suggest multiple possible fixes)
- Provide explanations for the suggested changes
- Integrate with version control (e.g., Git) and CI/CD pipelines

**Please provide:**

1. **Process Flow:**
    
    - Step-by-step workflow from Jira issue creation to code fix generation and validation.
    - How to handle edge cases (e.g., ambiguous issue descriptions, multiple possible fixes, or lack of context).
2. **Technical Guidelines:**
    
    - Recommended technologies and libraries for:
        - Jira API integration
        - Code analysis (static/dynamic)
        - Code generation (LLMs, rule-based, or hybrid approaches)
        - Version control integration
    - Best practices for security, performance, and maintainability.
3. **Architecture Details:**
    
    - High-level architecture diagram (components and their interactions).
    - Data flow between Jira, codebase, and the fix generation tool.
    - Scalability considerations for large codebases.
4. **Challenges & Mitigations:**
    
    - Common pitfalls in automating code fixes for monolithic codebases.
    - How to ensure the generated fixes are reliable and safe to merge.
5. **Evaluation Metrics:**
    
    - How to measure the tool’s effectiveness (e.g., fix success rate, developer acceptance, time saved).

**Assumptions:**

- The codebase is in [specify language, e.g., Java/Python/JavaScript].
- The tool should support both simple bug fixes and complex logic changes.
- The tool should minimize false positives and false negatives.

**Output Format:**

- Use clear headings and bullet points for easy readability.
- Include code snippets or pseudo-code where relevant.

---

**Why this prompt works:**

- It’s specific about the problem and constraints.
- It asks for actionable, structured output.
- It covers process, tech stack, architecture, and evaluation—everything you need to start building.
