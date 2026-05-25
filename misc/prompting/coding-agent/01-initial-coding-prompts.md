You are my AI pair programmer. I have a technical guide with example code and requirements. 
Goal: Generate the optimal project directory structure and a development plan, then implement the project step by step, starting from phase 1.
Context:
• Technical guide describes: Refer COMPREHENSIVE_TECHNICAL_GUIDE.md

Expectations:
1. Analyze the technical guide and design the complete high-level project structure (folders, main modules, config, README,requirements.txt etc.).
2. Present the proposed folder/file architecture.
3. For phase1:
step 1: Given a project, go through all the floder/files parse and build AST Tree  
Step 2: use Open grok indexer to search
Step 3:  code graph with call chains
4. Generate implementation code for this step only, including any necessary setup and tests.
5. After each step, wait for confirmation before continuing.
6. Use best practices for code style, documentation, and testing.
7. Prompt for feedback, clarify requirements, or list any assumptions made.
Output format:
- [Project Structure Tree]
- [Stepwise task list for this phase]
- [Code snippets with explanations]
- [Setup or instructions if any]
Proceed to project planning and wait for review after presenting the plan.