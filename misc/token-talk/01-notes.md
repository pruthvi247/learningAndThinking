- [eco-system-openspec](https://github.tools.sap/CloudNativeCulture/Ecosystem/blob/main/Sessions/PastSessions/2026/OpenSpec.md)
- [eco-Harness-engineering](https://github.tools.sap/CloudNativeCulture/Ecosystem/blob/main/Sessions/PastSessions/2026/StateAIHarnessEngineering.md)
- [eco-enterprise-skills](https://github.tools.sap/CloudNativeCulture/Ecosystem/blob/main/Sessions/PastSessions/2026/EnterpriseSkills.md)
- [eco-codifying-good-practices](https://github.tools.sap/CloudNativeCulture/Ecosystem/blob/main/Sessions/PastSessions/2026/CodifyingGoodPractices.md)
- 



[Six habits](https://ashy-dune-0b4215a0f.7.azurestaticapps.net/index.html#scene-2)

https://ashy-dune-0b4215a0f.7.azurestaticapps.net/index.html#scene-2
![[Pasted image 20260720155022.png]]


![[Pasted image 20260720155447.png]]


![[Pasted image 20260720155742.png]]

### hands on guide 
### https://code.visualstudio.com/docs/agents/guides/customize-copilot-guide
/Users/I562107/.vscode/extensions/github.copilot-chat-0.48.1/assets/prompts/skills/agent-customization/SKILL.md


---------

### Custom / command in copilot

```
You can create a custom slash command in VS Code Copilot using **Prompt Files** (`.prompt.md`), which allow you to turn repeated chat requests into reusable shortcuts. [[1](https://dev.to/petermilovcik/vs-code-prompt-files-custom-slash-commands-for-github-copilot-1m4f)]

Step 1: Create the Prompt File

- Open the **Command Palette** by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS). [[1](https://www.youtube.com/watch?v=QkmPe68UePg&t=540)]

- Search for and select **`Chat: New Prompt File`**. [[1](https://code.visualstudio.com/docs/agent-customization/prompt-files), [2](https://dev.to/petermilovcik/vs-code-prompt-files-custom-slash-commands-for-github-copilot-1m4f)]

- Choose the scope for your command:
    - **User**: Available across all of your projects and workspaces.
    - **Workspace**: Available only within your current open project folder. [[1](https://code.visualstudio.com/docs/agent-customization/prompt-files), [2](https://dev.to/petermilovcik/vs-code-prompt-files-custom-slash-commands-for-github-copilot-1m4f), [3](https://www.telefonica.com/en/communication-room/blog/github-copilot-android-studio-customization/)]

- Name the file. **The exact filename you choose determines your slash command name**. For example, naming the file `review.prompt.md` will create the `/review` command. [[1](https://dev.to/petermilovcik/vs-code-prompt-files-custom-slash-commands-for-github-copilot-1m4f), [2](https://goatreview.com/automate-ai-prompts-claude-code-custom-commands/)]

_Alternatively, you can type **`/create-prompt`** directly into the Copilot Chat window to have AI scaffold the file for you._ [[1](https://code.visualstudio.com/docs/agent-customization/overview)]

Step 2: Write your Custom Instructions

Your prompt file uses standard Markdown formatting along with a YAML frontmatter section at the very top to define its behavior. Open your new file and structure it like this: [[1](https://code.visualstudio.com/docs/agent-customization/prompt-files)]

markdown

```
---
description: Analyzes the highlighted code for security vulnerabilities.
---

You are an expert security auditor. Review the selected code or active file for vulnerabilities. 
List any potential risks, categorize them by severity (High/Medium/Low), and provide secure code alternatives.
```

Use code with caution.

Step 3: Use your New Command

- Open the VS Code **Chat View** (`Ctrl+Cmd+I` or `Ctrl+Alt+I`) or open **Inline Chat** (`Ctrl+I`).

- Highlight a block of code in your editor.

- Type a forward slash followed by your file's name (e.g., **/review**).

- Press **Enter** to execute the command. [[1](https://code.visualstudio.com/docs/agents/reference/ai-features-cheat-sheet), [2](https://code.visualstudio.com/docs/chat/chat-overview), [3](https://www.youtube.com/watch?v=pXSCfpnC1hQ&t=920), [4](https://www.youtube.com/watch?v=nNiDplJqU6w&t=289), [5](https://dev.to/petermilovcik/vs-code-prompt-files-custom-slash-commands-for-github-copilot-1m4f)]
```
========

### Custom agents

How it Changes the Chat Experience

When you activate your `bug-fix-architect` agent:

- **Scope Isolation**: It stops acting like a general-purpose AI and strictly enforces the formatting, workflows, and code rules written inside that file. [[1](https://github.com/orgs/community/discussions/178690), [2](https://www.morphllm.com/agents-md-guide), [3](https://www.linkedin.com/pulse/introducing-codex-openais-cloud-based-ai-coding-agent-chumc)]
- **Automatic Tools**: If the markdown file lists specialized build, linting, or testing commands (like `npm run test`), the agent will know exactly how to execute or verify them without you typing out the exact terminal flags. [[1](https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9), [2](https://www.morphllm.com/agents-md-guide)]
- **Targeted Context**: It looks specifically at architectural constraints outlined in the file to make sure its suggested bug fixes don't accidentally break other parts of your app. [[1](https://www.morphllm.com/agents-md-guide), [2](https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9)]

If your agent isn't showing up in the chat window, share the **first few lines of text** inside your `bug-fix-architect.agent.md` file, and I can check if it is missing the required configuration metadata. [[1](https://github.com/github/copilot-cli-for-beginners/blob/main/04-agents-custom-instructions/README.md)]
=============
### Concise is key [source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

The [context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) is a public good. Your Skill shares the context window with everything else Claude needs to know, including:

- The system prompt
- Conversation history
- Other Skills' metadata
- Your actual request


Harness eng: optimise the env of agent

Token harder vs token smarter

make it run 
make it right
make it fast

AI Slop 

[real-world analogy: context window](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/02-context-and-conversations/#-real-world-analogy-working-with-a-colleague)

https://awesome-copilot.github.com/images/learning-hub/copilot-cli-for-beginners/02/colleague-context-analogy.png

-> see in action video


![[Pasted image 20260720143431.png]]

![[Pasted image 20260720143638.png]]


### 1. **What is Context Engineering?**

Context Engineering is the **art and science of giving the AI the right information, at the right time, in the right format** to get the best possible output.

**Goal**: Maximize intelligence while minimizing token usage and noise.


### 2. **Context Management Strategies**

#### **A. Project-Level Context (Most Important)**

Create a file in your repository root:

**Recommended filename**: skills.md or project-guidelines.md or COPILOT.md

**What to include:**

```md
# Project Guidelines for AI Coding Assistants

## Tech Stack
- Backend: Node.js 20, Express
- Database: PostgreSQL
- Styling: Tailwind CSS

## Coding Standards
- Use functional programming where possible
- Prefer early returns
- Error handling: Use custom AppError class
- Naming: camelCase for variables, PascalCase for components

## Architecture Preferences
- Feature-based folder structure
- Clean Architecture principles
- Repository pattern for data access

## Performance Rules
- Avoid N+1 queries
- Implement caching for expensive operations

## Common Patterns to Follow
- ...
```
**How to use it:**

- **Copilot**: It automatically picks up skills.md, README.md, etc.



### 3. **Token Saving Techniques** (Very Practical)

|Technique|Token Savings|How to Use|
|---|---|---|
|**Use References**|High|Instead of pasting full code, say @file: src/utils/auth.ts|
|**Summarize First**|High|"Summarize this file first, then suggest improvements"|
|**Specific Scope**|Medium-High|@folder: src/services instead of whole project|
|**Custom Instructions**|High|Persistent rules in Copilot/ChatGPT/Claude|
|**Iterative Approach**|High|Small focused requests instead of one big prompt|
|**Remove Comments**|Medium|Ask AI to ignore comments when not needed|
|**Use Shorter Aliases**|Low-Medium|Define abbreviations in project guidelines|

**Pro Tip**: Always start with:

> "Keep response concise. Focus only on..."

### 4. **Powerful Prompt Templates** (Ready to Use)

#### **Template 1: General Task**
```md
You are a senior [language] developer.

Project context: [paste key points from skills.md or summarize]

Task: [what you want]

Requirements:
- Follow our coding standards in skills.md
- Use modern best practices
- Add clear comments
- Consider performance and edge cases

Return the code + brief explanation.
```

```md

#### **Template 3: New Feature**
```text
Create a new feature with the following requirements:

User Story: [description]

Technical Constraints:
- Use existing patterns from the project
- Follow guidelines in skills.md
- Must be testable

Deliver:
1. Component/Service code
2. Unit tests
3. Any necessary types/interfaces
```
#### Template: debugging
```md

I have this error:

[Error message]

Help me:

1. Identify root cause
2. Suggest fix
3. Prevent similar issues in future

Code:
```[language]
[paste relevant code]
```

```md
### 5. **Advanced Context Engineering Tips**

1. **Layered Context** - Level 1: `skills.md` (always active) - Level 2: Recent files - Level 3: Specific files mentioned with `@`

2. **Context Refresh** - Periodically ask: "Update your understanding of the project based on skills.md"

3. **Claude Projects Advantage** - Create a Project per repository - Upload `skills.md`, architecture diagrams, API specs

4. **Copilot Workspace / Claude Artifacts** - Use for multi-step complex tasks

---

### Hands-on Exercises for the Session (Recommended)

1. **Create `skills.md`** together (10 mins) 2. **Rewrite a bad prompt** → good prompt (group activity) 3. **Live Refactoring** using project context 4. **Challenge**: Implement a small feature using only references, no copy-pasting large code
```



### copilot


[session-autosave](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/02-context-and-conversations/#sessions-auto-save)

```md
copilot --continue
# Pick from a list of sessions interactively

copilot --resume

# Or resume a specific session by ID

copilot --resume abc123
```

![[Pasted image 20260720143847.png]]

### [Developer workflow](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/03-development-workflows/)

![[Pasted image 20260720144004.png]]


![[Pasted image 20260720144038.png]]

```

> I'm getting this error:
> AttributeError: 'NoneType' object has no attribute 'title'
>     at show_books (book_app.py:19)
>
> @samples/book-app-project/book_app.py Explain why and how to fix it
```


Quick Tip: Research Before You Plan or Code

```

claude

> /deep-research What are the best Python libraries for validating user input in CLI apps?
```

#### [bugfix-flow](https://awesome-copilot.github.com/learning-hub/cli-for-
beginners/03-development-workflows/#putting-it-all-together-bug-fix-workflow)


```md
copilot

> Users report: 'Finding books by author name doesn't work for partial names'
> @samples/book-app-project/books.py Analyze and identify the likely cause
> Based on the analysis, show me the find_by_author function and explain the issue

> Fix the find_by_author function to handle partial name matches
> @samples/book-app-project/books.py Generate pytest tests specifically for:
> - Full author name match
> - Partial author name match
> - Case-insensitive matching
> - Author name not found
copilot -p "Generate commit message for: $(git diff --staged)"
```

_vs_

```md
copilot

> @samples/book-app-buggy/books_buggy.py
>
> Users report: "Finding books by author name doesn't work for partial names"
> Debug why this happens
```


- **Start with `/plan`** for anything non-trivial. Refine the plan before execution - a good plan leads to better results.
- - **Save prompts that work well.** When Copilot CLI makes a mistake, note what went wrong. Over time, this becomes your personal playbook.


#### [Add your agents](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/04-agents-and-custom-instructions/#%EF%B8%8F-add-your-agents)
.agent.md

```
---
name: my-reviewer
description: Code reviewer focused on bugs and security issues
---

# Code Reviewer

You are a code reviewer focused on finding bugs and security issues.

When reviewing code, always check for:
- SQL injection vulnerabilities
- Missing error handling
- Hardcoded secrets
```

## Where to put agent files

| Location             | Scope                 | Best For                                    |
| -------------------- | --------------------- | ------------------------------------------- |
| `.github/agents/`    | Project-specific      | Team-shared agents with project conventions |
| `~/.copilot/agents/` | Global (all projects) | Personal agents you use everywhere          |


| Resource                                                                                           | Description                                                 | Browse                                                                |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
| 🤖 [Agents](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md)             | Specialized Copilot agents that integrate with MCP servers  | [All agents →](https://awesome-copilot.github.com/agents)             |
| 📋 [Instructions](https://github.com/github/awesome-copilot/blob/main/docs/README.instructions.md) | Coding standards applied automatically by file pattern      | [All instructions →](https://awesome-copilot.github.com/instructions) |
| 🎯 [Skills](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)             | Self-contained folders with instructions and bundled assets | [All skills →](https://awesome-copilot.github.com/skills)             |
| 🔌 [Plugins](https://github.com/github/awesome-copilot/blob/main/docs/README.plugins.md)           | Curated bundles of agents and skills for specific workflows | [All plugins →](https://awesome-copilot.github.com/plugins)           |
| 🍳 [Cookbook](https://github.com/github/awesome-copilot/blob/main/cookbook/README.md)              | Copy-paste-ready recipes for working with Copilot APIs      | —                                                                     |


| Aspect                  | **Instructions**                                    | **Skills**                       | **Agents**                         | **Plugins**                              |
| ----------------------- | --------------------------------------------------- | -------------------------------- | ---------------------------------- | ---------------------------------------- |
| **Purpose**             | Persistent rules & style guidelines                 | Reusable, focused tasks          | Full autonomous persona + workflow | Extend functionality with external tools |
| **Scope**               | Passive, always-on                                  | On-demand, task-specific         | Active, goal-oriented              | Feature extenders                        |
| **File Type**           | `AGENTS.md`, `copilot-instructions.md`, `CLAUDE.md` | `SKILL.md` files in folders      | `*.agent.md`                       | Separate packages / extensions           |
| **When it loads**       | At session start                                    | When triggered (name or keyword) | When explicitly selected           | When installed & enabled                 |
| **Complexity**          | Low                                                 | Medium                           | High                               | Medium-High                              |
| **Best For**            | Coding standards, preferences                       | Common repeatable tasks          | Complex, multi-step projects       | New capabilities (tools, integrations)   |
| **Token Impact**        | Medium (always present)                             | Low (loaded only when needed)    | High                               | Varies                                   |
| **Copilot Support**     | Excellent                                           | Excellent                        | Very Strong (Custom Agents)        | Good                                     |
| **Claude Code Support** | Excellent (`CLAUDE.md`)                             | Strong                           | Strong (Sub-agents)                | Strong (Skills + MCP)                    |


### 1. **Instructions** (The Foundation)

**What they are**: Persistent, always-active guidelines that shape how the AI behaves.

**Examples**:

- Coding style, naming conventions, architecture preferences
- Tech stack rules, error handling standards
- "Always use TypeScript strict mode", "Prefer functional patterns"

**Strengths**:

- Simple to maintain
- Ensures consistency across all interactions

**Weaknesses**:

- Takes up context tokens permanently
- Not suitable for complex logic

**Best Practice**: Keep skills.md / AGENTS.md / CLAUDE.md focused and under 200–300 lines.

---

### 2. **Skills** (The Sweet Spot for Most Teams)

**What they are**: Self-contained, reusable mini-programs or task templates.

**Structure**: Usually a folder with SKILL.md + supporting files.

**Examples**:

- draft-blog-post/SKILL.md
- security-review/SKILL.md
- refactor-component/SKILL.md

**Strengths**:

- Excellent **token efficiency** (loaded only when needed)
- Reusable across team
- Can include examples, steps, and test logic

**When to use**: For any repeatable task you do more than once.

---

### 3. **Agents** (The Power User / Autonomous Option)

**What they are**: Specialized AI personas with defined roles, tools, and workflows.

**Key Difference**: Agents are **active** — they can plan, use tools, make decisions, and execute multi-step tasks.

**Examples**:

- "Senior Backend Architect Agent"
- "Code Reviewer Agent"
- "Full-Stack Feature Builder Agent"

**Strengths**:

- Can handle complex, long-running tasks
- Has memory of its role and expertise
- Best for autonomous work

**Weaknesses**:

- Higher token consumption
- More complex to design well

---

### 4. **Plugins** (Extensibility Layer)

**What they are**: Add new capabilities, tools, or integrations.

**Examples**:

- Browser automation plugin
- Database query plugin
- Design system integration
- Memory / RAG plugins

**Current Trend (2026)**: Many things that used to be plugins are evolving into **Skills** or being replaced by **MCP (Model Control Protocol)** servers.

### Practical Comparison & Recommendations

**Use this decision framework**:

1. **Is it a rule or preference?** → **Instructions**
2. **Is it a repeatable task?** → **Skills** (Recommended for most teams)
3. **Is it a complex, multi-step workflow or role?** → **Agents**
4. **Do I need new tools or external integrations?** → **Plugins** / MCP

**Recommended Setup for Teams** (Best Practice 2026):

- AGENTS.md or project-guidelines.md → Core Instructions
- .agents/skills/ folder → Collection of team Skills
- Custom Agents for specialized roles (Architecture, Testing, Security)
- A few high-value Plugins (e.g., testing, documentation)

**Token Efficiency Ranking** (Best to Worst):

1. Skills (Best)
2. Instructions (when kept lean)
3. Plugins
4. Agents (Highest usage)
--------


**Excellent request!** Here's a clear, real-world comparison using the **same DevOps / Platform Engineering task**:

### **Task**:  
**"Add monitoring, logging, and alerting for a new microservice"**

---

### 1. **Instructions** (Passive Rules)

**File**: `AGENTS.md` or `CLAUDE.md` or `.github/copilot-instructions.md`

```markdown
# Platform Engineering Guidelines

## Monitoring & Observability Standards
- All services must use OpenTelemetry for tracing
- Logs must be structured JSON and sent to Loki
- Metrics must be exposed on /metrics endpoint (Prometheus format)
- Use our standard Grafana dashboards as base
- Alerting rules:
  - Error rate > 1% for 5 minutes → P1
  - Latency p95 > 800ms → P2
  - CPU > 85% for 10 minutes → Warning
- Always add service.name label
```

**How it works**:  
These rules are **always loaded**. The AI will try to follow them whenever relevant, but it won’t proactively do the full task unless you ask.

**Best for**: Consistency and standards enforcement.

---

### 2. **Skill** (Recommended for most cases)

**Folder**: `.agents/skills/add-monitoring/SKILL.md`

```markdown
# SKILL: Add Monitoring & Alerting

## Description
Adds full observability (logs, metrics, traces, dashboards, alerts) for a new or existing microservice following platform standards.

## Trigger Keywords
add monitoring, setup observability, add alerting, monitoring setup

## Steps to Execute
1. Analyze the service (language, framework, deployment method)
2. Add OpenTelemetry instrumentation if missing
3. Add /metrics endpoint + Prometheus client
4. Update Kubernetes deployment with annotations
5. Create Loki logging configuration
6. Create Grafana dashboard JSON
7. Add AlertManager rules (error rate, latency, resource usage)
8. Update service catalog / documentation

## Standards (from AGENTS.md)
- Use OpenTelemetry
- Structured JSON logs
- Standard alert severity levels
- Add `service.name` and `team` labels

## Output Format
- List of files to create/modify
- Code changes with diff
- Verification commands
- Dashboard preview link (if applicable)

## Example Usage
User: "Add monitoring for the payment service"
```

**How to use**:  
You type: `"Add monitoring for user-service"` → The Skill activates automatically.

**Strengths**: Focused, reusable, token-efficient, consistent output.

---

### 3. **Agent** (For Complex/Autonomous Work)

**File**: `platform-observability.agent.md`

```markdown
# Agent: Platform Observability Engineer

## Persona
You are an experienced Senior Platform Engineer (ex-Google SRE) specializing in observability, reliability, and production readiness.

## Expertise
- OpenTelemetry, Prometheus, Grafana, Loki, AlertManager, Jaeger
- Kubernetes, Helm, Terraform
- Service Level Objectives (SLOs)
- On-call best practices

## Tools Available
- File system read/write
- Run terminal commands (kubectl, helm, etc.)
- Test observability setup
- Search service catalog

## Working Style
1. Always start with a plan and ask for confirmation
2. Follow company Platform Golden Paths
3. Prioritize zero-downtime and backward compatibility
4. Add proper tests and validation steps
5. Document everything in the service README

## Special Instructions
- Never skip adding SLO definitions
- Always create both technical + business metrics
- Follow our "Observability Maturity Model Level 2" requirements
```

**How to use**:  
You activate the agent explicitly:  
`"@PlatformObservabilityEngineer Add monitoring for the new payment-service"`

**Strengths**: Can handle the entire end-to-end process autonomously, make decisions, run validations, and iterate.

---

### Summary: Which One Should You Use?

| Use Case                                 | Best Choice                 | Reason                     |
| ---------------------------------------- | --------------------------- | -------------------------- |
| Enforce standards                        | **Instructions**            | Always active              |
| Common repeatable task                   | **Skill**                   | Best balance (Recommended) |
| Complex, multi-step, decision-heavy task | **Agent**                   | Maximum intelligence       |
| One-time or very unique task             | Plain prompt + Instructions | No need for overhead       |
|                                          |                             |                            |

**My Recommendation for Team**:
- Use **Instructions** for global standards
- Build 8–12 high-quality **Skills** for common DevOps tasks (this is the highest ROI)
- Create 2–3 powerful **Agents** for senior platform engineers


| Human Equivalent      | AI Equivalent |
| --------------------- | ------------- |
| Company Policy        | Instructions  |
| Professional Training | Skills        |
| Employee              | Agent         |
|                       |               |
|                       |               |
|                       |               |

--------------
---------------
=======
chat-gpt
============
# The Evolution

Let's first understand how coding assistants evolved.

```md

LLM
 │
 ├── Prompt
 │
 ├── Instructions
 │
 ├── Skills
 │
 ├── Tools
 │
 ├── Memory
 │
 ├── Planning
 │
 └── Agents
```


Since you're building **agentic AI systems** (Autofix, MCP servers, multiple agents, memory, A2A communication), understanding the difference between **Instructions**, **Skills**, and **Agents** is one of the most important concepts. Many people mix them together, but they solve completely different problems.

Think of it this way:

| Human Equivalent      | AI Equivalent |
| --------------------- | ------------- |
| Company Policy        | Instructions  |
| Professional Training | Skills        |
| Employee              | Agent         |
|                       |               |

Everything else is built on top of these three.

---

# The Evolution

Let's first understand how coding assistants evolved.

```
LLM
 │
 ├── Prompt
 │
 ├── Instructions
 │
 ├── Skills
 │
 ├── Tools
 │
 ├── Memory
 │
 ├── Planning
 │
 └── Agent
```

The more we move downward, the more autonomous the system becomes.

---

# Level 1 : Instructions

Instructions tell an LLM **HOW TO BEHAVE**.

They do **not** teach the model new knowledge.

They simply constrain behavior.

Examples

```
Always write Python.

Never delete files.

Use snake_case.

Write tests first.

Think step by step.

Do not hallucinate.

Always ask before making changes.
```

Notice...

Nothing here performs work.

They're just behavioral rules.

Think of instructions as company policies.

Example:

```
Company Policy

- Wear ID card
- Come before 9 AM
- Don't share customer data
- Use Jira
```

Policies don't make you an engineer.

They only guide how engineers work.

Exactly the same.

---

## Coding Example

Bad

```
User:
Create REST API.
```

Better

```
Instructions

- Use FastAPI
- Python 3.12
- Async only
- Add logging
- Type hints mandatory
- Use dependency injection
- Write tests
```

Now every response follows these rules.

---

## Where Instructions Live

OpenAI

```
System Prompt
```

Claude

```
System Prompt
```

Cursor

```
.cursor/rules
```

Windsurf

```
rules.md
```

GitHub Copilot

```
copilot-instructions.md
```

Codex

```
AGENTS.md
```

These files don't contain code.

They contain guidance.

Example

```
Never use print()

Always use logger

Prefer pathlib over os.path

Write Google docstrings

Don't modify generated files
```

---

# Good Instruction Characteristics

Instructions should be

- Short
    
- Stable
    
- High level
    
- Universal
    

Good

```
Always write unit tests.
```

Bad

```
Open utils.py
Go to line 28
Replace foo() with bar()
```

That's a task, not an instruction.

---

# Level 2 : Skills

This is where many people become confused.

A skill is **reusable expertise**.

It teaches the model **HOW TO DO SOMETHING SPECIFIC.**

Think about a human.

Instructions

```
Be polite.
```

Skill

```
Perform heart surgery.
```

Huge difference.

---

Skills contain knowledge.

Example

```
Create Kubernetes Deployment

Step 1

Validate namespace

Step 2

Generate Deployment YAML

Step 3

Generate Service

Step 4

Validate probes

Step 5

Apply manifests
```

Now the AI knows the process.

---

## Coding Skill Example

Skill

```
Code Review

1 Read changed files

2 Find bugs

3 Find security issues

4 Check naming

5 Check complexity

6 Suggest fixes

7 Produce summary
```

Now every time code review happens...

the AI already knows the workflow.

---

Skills are Modular

```
Skill

REST API

Skill

Docker

Skill

Terraform

Skill

Kubernetes

Skill

React

Skill

Security Audit
```

Each one is independent.

---

## Skills Can Call Tools

Example

```
Skill

Fix Build Failure

↓

Read CI logs

↓

Search repo

↓

Run tests

↓

Generate patch

↓

Verify
```

This is more than instructions.

It's a workflow.

---

Think of Skills as Functions.

```
Instructions

↓

Global Configuration

Skills

↓

Reusable Functions
```

---

# Level 3 : Tools

Before agents, understand tools.

LLMs cannot

- read files
    
- execute code
    
- call APIs
    
- browse repositories
    

They need tools.

Example

```
Git Tool

↓

git status

↓

git diff

↓

git commit
```

Another

```
Filesystem

↓

Read file

↓

Write file
```

Another

```
Jira

↓

Search issue

↓

Create issue
```

Tools give abilities.

Skills know when to use them.

---

# Level 4 : Agent

Now comes the big concept.

An agent is

> An LLM that can reason, plan, use tools, remember context, and execute multi-step goals with minimal supervision.

Notice...

Agent is NOT just an LLM.

It is

```
LLM
+
Instructions
+
Skills
+
Tools
+
Memory
+
Planning
+
Execution
```

---

Think of a Software Engineer.

They have

Company Policy

↓

Instructions

Knowledge

↓

Skills

Laptop

↓

Tools

Experience

↓

Memory

Ability to plan

↓

Planning

Ability to work independently

↓

Agent

---

# Anatomy of an Agent

```
            Goal
              │
              ▼
        Planner
              │
              ▼
     Task Decomposition
              │
              ▼
      Select Skill
              │
              ▼
      Use Required Tool
              │
              ▼
 Execute
              │
              ▼
Validate
              │
              ▼
Store Memory
              │
              ▼
Return Result
```

---

Suppose user asks

```
Fix failing CI pipeline.
```

A normal LLM

```
Explains possible fixes.
```

Agent

```
Read CI logs

↓

Read Git diff

↓

Identify failure

↓

Generate patch

↓

Run tests

↓

Run linter

↓

Run build

↓

Commit changes

↓

Create PR

↓

Notify Slack
```

Entire workflow.

---

# Relationship Between Them

```
                Agent
               /  |  \
              /   |   \
             /    |    \
     Instructions Skills Tools
```

Instructions

↓

Behavior

Skills

↓

Expertise

Tools

↓

Capabilities

Agent

↓

Coordinates everything.

---

# Coding Agent Architecture

```
                   User

                     │

                     ▼

              Coding Agent

         ┌───────────────┐

         │ Planner        │

         │ Memory         │

         │ Instructions   │

         │ Skill Library  │

         │ Tool Manager   │

         │ Validator      │

         └───────────────┘

              │

     ┌────────┴────────┐

Filesystem     Git

Docker          Jira

IDE             MCP

GitHub          Kubernetes

Database        Browser
```

---

# Real Example

User

```
Implement JWT Authentication.
```

Instructions

```
Use FastAPI

Never break APIs

Write tests

Use clean architecture
```

Skill Selected

```
Authentication Skill

↓

Generate JWT

↓

Middleware

↓

Refresh token

↓

Hash password

↓

RBAC

↓

Tests
```

Tools

```
Filesystem

Git

Docker

Pytest
```

Agent Execution

```
Read project

↓

Understand architecture

↓

Find auth module

↓

Generate code

↓

Run tests

↓

Fix failures

↓

Commit

↓

Create PR
```

---

# Where MCP Fits

Since you've been working with **MCP (Model Context Protocol)**, it's useful to place it in the architecture.

```
                Agent

                  │

          Skill Selection

                  │

           MCP Tool Layer

       ┌──────────┼──────────┐

      GitHub     Neo4j     Milvus

      OpenGrok   Splunk    Jira

      Confluence Kubernetes

                  │

           External Systems
```

MCP is **not an agent** and **not a skill**. It is a standardized way for agents to discover and use external tools and resources. Your skills can invoke MCP tools, and your agent orchestrates those skills.

---

# Multi-Agent Systems

Complex engineering tasks are often split across specialized agents.

```
                    User

                      │

                Orchestrator

        ┌─────────┼─────────┐

        │         │         │

 Code Agent  Test Agent  Security Agent

        │         │         │

   Git Tool   Pytest    SAST Scanner

        └─────────┼─────────┘

                  │

           Reviewer Agent

                  │

              Final Output
```

Each agent can have:

- Shared organizational instructions (coding standards, security rules)
    
- Its own specialized skills (e.g., testing, reviewing, performance tuning)
    
- Access to a tailored set of tools
    

---

# Best Practices

For production-grade coding agents, keep these concerns separate:

|Component|Purpose|Should contain|
|---|---|---|
|Instructions|Behavioral guardrails|Coding standards, style, safety rules|
|Skills|Domain workflows|API development, debugging, migrations, reviews|
|Tools|External capabilities|Git, filesystem, Docker, Kubernetes, Jira, MCP servers|
|Memory|Persistent context|Project conventions, previous decisions, user preferences|
|Planner|Decision making|Task decomposition, skill selection, sequencing|
|Agent|Orchestrator|Coordinates everything to achieve the user's goal|

## Applying this to your Autofix platform

For the architecture you've described previously, a clean separation would look like:

- **Instructions:** Organization-wide engineering standards (branch naming, testing requirements, logging conventions, architectural constraints).
    
- **Skills:** Root-cause analysis, stack-trace investigation, dependency upgrades, code generation, security review, PR review, documentation generation.
    
- **Tools (via MCP):** OpenGrok, Neo4j, Milvus, GitHub, Jira, Splunk, Dynatrace, Confluence, Kubernetes.
    
- **Memory:** Previous incidents, successful fixes, project-specific conventions, architectural decisions.
    
- **Planner:** Break an issue into retrieval, diagnosis, code modification, validation, and PR creation.
    
- **Agent:** Orchestrate the entire workflow from receiving a Jira ticket to producing a validated pull request.
    

This separation makes the system easier to extend, test, and maintain. Adding support for a new capability—such as analyzing Dynatrace traces—typically means adding a new tool and perhaps a new diagnostic skill, without rewriting the agent's core logic or changing its global instructions.

--------

Files like:

```
python-mcp-expert.agent.md
```

sit somewhere **between Instructions and Skills**, depending on what is inside them.

This is where many AI frameworks become confusing because different vendors use different names:

|Framework|Name|
|---|---|
|OpenAI Codex|AGENTS.md|
|Claude Code|agent.md|
|Cursor|.cursor/rules|
|Windsurf|rules.md|
|CrewAI|Agent Definition|
|LangGraph|Agent Prompt|
|AutoGen|Agent Profile|

The filename doesn't tell you what it is.

The **content** does.

---

# Example 1: Agent File Acting Like Instructions

Suppose `python-mcp-expert.agent.md` contains:

```
You are a Python expert.

Always use type hints.

Follow PEP8.

Prefer pathlib.

Never use print().

Write unit tests.

Use async when possible.
```

This is basically:

```
Instructions
```

because it only changes behavior.

It doesn't teach a workflow.

---

# Example 2: Agent File Acting Like a Skill

Suppose it contains:

```
When debugging Python:

1. Read stack trace
2. Identify root cause
3. Search related files
4. Generate fix
5. Run tests
6. Verify no regressions
7. Create summary
```

Now it is a:

```
Skill
```

because it describes a reusable procedure.

---

# Example 3: Agent Persona

Many frameworks use `.agent.md` for defining an agent.

Example:

```
Agent Name:
Python MCP Expert

Responsibilities:
- Python development
- Dependency management
- Packaging
- Testing
- MCP integration

Available Tools:
- Filesystem
- Git
- Python Executor
- MCP Server Registry

Escalation:
- Ask Security Agent for vulnerabilities
- Ask DevOps Agent for deployment
```

Now it becomes:

```
Agent Definition
```

which contains:

- Instructions
- Skills
- Tool access
- Responsibilities

all together.

---

# Agent Definition Anatomy

Most modern coding agents actually look like:

```
python-mcp-expert.agent.md

├── Identity
├── Instructions
├── Skills
├── Tool Permissions
├── Constraints
├── Examples
└── Output Format
```

Example:

```
# Identity

You are Python MCP Expert.

# Instructions

Use Python 3.12.
Use type hints.

# Skills

- Build MCP Servers
- Debug MCP Connections
- Create FastAPI APIs

# Tools

Filesystem
Git
Docker

# Constraints

Never modify secrets.

# Output

Always provide patch.
```

This is no longer a pure instruction file.

It's a mini-agent specification.

---

# How Claude Code Uses agent.md

In Claude Code, a typical agent file might look like:

```
---
name: python-mcp-expert
description: Expert in Python MCP server development
tools:
  - Read
  - Write
  - Bash
---

You are an expert in:

- MCP
- FastAPI
- Asyncio
- uv

When asked to create an MCP server:

1. Design tools
2. Design resources
3. Implement transport
4. Add tests
5. Validate protocol
```

Notice what's happening:

```
Agent
 ├── Instructions
 ├── Skills
 ├── Tool Access
 └── Expertise
```

This is why the file is called:

```
agent.md
```

not

```
instructions.md
```

---

# In Your Autofix Architecture

Let's say you create:

```
agents/

├── java-debugger.agent.md
├── splunk-investigator.agent.md
├── neo4j-expert.agent.md
├── kubernetes-expert.agent.md
├── security-reviewer.agent.md
```

Example:

### kubernetes-expert.agent.md

```
# Identity

Kubernetes Production Expert

# Instructions

Prefer immutable deployments.
Never delete namespaces.

# Skills

- Deployment Debugging
- Resource Optimization
- HPA Analysis
- Network Troubleshooting

# Tools

Kubernetes MCP
GitHub MCP
Splunk MCP

# Output

Provide YAML patches.
```

When the orchestrator receives:

```
Investigate why checkout service is failing.
```

it may select:

```
splunk-investigator.agent.md

+
kubernetes-expert.agent.md

+
java-debugger.agent.md
```

Each specialized agent brings its own instructions, skills, and tools.

---

# A More Accurate Mental Model

Most people think:

```
Instructions
Skills
Agents
```

But in modern coding systems it's closer to:

```
Agent
 │
 ├── Instructions
 ├── Skills
 ├── Tools
 ├── Memory
 ├── Examples
 └── Constraints
```

So a file named:

```
python-mcp-expert.agent.md
```

is usually **not just instructions** and **not just a skill**.

It's typically a **packaged specialist agent definition** that bundles:

- Who the agent is
- What it knows
- How it should behave
- Which tools it can use
- What workflows it follows

Think of it as the AI equivalent of a job description plus operating handbook for a specialist engineer.

---------

Yes — python-mcp-expert.agent.md is part of a newer pattern used in coding agent systems (Claude Code, Codex, Cursor workflows, Roo Code, OpenHands, custom agent frameworks, etc.) where a file defines an agent persona with specific expertise and working methods. It sits somewhere between instructions and skills, but is closer to an agent configuration.

The confusion comes because modern agent frameworks package multiple concepts into one file.

### The Short Answer

|Concept|Purpose|
|---|---|
|instructions.md / AGENTS.md|Global behavior rules|
|skill.md|Reusable workflow or expertise|
|python-mcp-expert.agent.md|A specialized agent definition that includes role, instructions, tools, and often embedded skills|

### What is an *.agent.md file?

An agent.md file defines who the AI is, what it is good at, how it should behave, what tools it can use, and the process it follows.

It is effectively a packaged specialist.

![Agent Skills: Progressive Disclosure as a System Design Pattern](https://images.openai.com/static-rsc-4/5rXp-FTafDMkwKoaECeem1LfHLdsF5L4SKWf4myFy-S3J3tkUt8wvj5JsHWTdRrpBhWMvreT1IKpcIGQZeSGlSTh1svbU7tvost7tb9BKiwnpCkREh2k1RqKGtoO4QCb-hGqol7JJ9pvMgL9WqCbbUXjdVpdChxm7jDhJ1KXnND8CCsGN_AB4PVN1Tbgo0ya?purpose=fullsize)

### Example: python-mcp-expert.agent.md

Imagine you have an agent whose job is to build Python MCP servers and integrations.

A python-mcp-expert.agent.md file might contain:

Markdown

```
# Python MCP Expert

## Role
You are a senior Python engineer specializing in Model Context Protocol (MCP), agentic systems, and developer tools.

## Mission
Design, implement, test, and maintain production-grade MCP servers and clients.

## Expertise
- Python 3.12+
- FastAPI
- AsyncIO
- MCP protocol
- JSON-RPC
- Pydantic
- Docker
- uv package manager
- Testing with pytest

## Working Rules
- Use type hints everywhere.
- Prefer async code.
- Follow clean architecture.
- Write tests for all functionality.
- Use structured logging.
- Never hardcode secrets.

## Available Tools
- Filesystem
- Git
- Terminal
- Docker
- Pytest
- MCP Inspector

## Standard Workflow
1. Understand the existing codebase.
2. Identify MCP resources, tools, and prompts.
3. Design interfaces before implementation.
4. Implement incrementally.
5. Run tests.
6. Run linting and formatting.
7. Update documentation.
8. Provide example usage.

## Output Format
- Explain design decisions.
- Show file-by-file changes.
- Include commands to run locally.
- List risks and assumptions.
```

### Breakdown of the File

### 1. Role (Agent Identity)

Defines who the model is.

Markdown

```
You are a Python MCP expert focused on building reliable MCP servers.
```

### 2. Instructions (Behavior)

Defines how the model should behave.

Markdown

```
- Use async code.
- Write tests.
- Do not break existing APIs.
```

### 3. Skills (Reusable Processes)

Defines how to perform recurring tasks.

Markdown

```
## MCP Server Creation Skill
1. Define tool schemas.
2. Implement handlers.
3. Add validation.
4. Add tests.
5. Create examples.
```

### 4. Tool Preferences

Defines what capabilities the agent should use.

Markdown

```
Use:
- Filesystem tool for reading/writing files
- Terminal for tests
- Git for commits
```

### 5. Output Contract

Defines how results are presented.

Markdown

```
Always include:
- Summary
- Files changed
- Test results
- Next steps
```

### Where It Fits in the Stack

![Agent Skills - Yet Another Tool Standard?](https://images.openai.com/static-rsc-4/bvd2vhTUlzxlI7ri4-y_WhVKCyQMPHeAb601y5rl8WHg3jopI_9I3oeZL8fdYXquY9ybbWSuACMKqx3H1-V3UfdtpSzIdEODoic0utSDG1qzbzM-sDDIhQwf2XOKl_BWkuZb46HvoZPxNWKtO31GhqoKKHl7_FKPhlDZveqKdiBgd41ACBdwOQFDZMu-lmiR?purpose=fullsize)

### Mental Model

|Artifact|Think of it as|
|---|---|
|instructions.md|Company policies|
|skill.md|Training manual / SOP|
|tool definitions|Laptop, IDE, Git, terminal|
|agent.md|A hired specialist employee who comes with policies, training, and a way of working|

### Why This Pattern Exists

As coding agents became more autonomous, people discovered that a single AGENTS.md file became too large and generic. Splitting the system into specialized *.agent.md files provides:

- Separation of concerns — one agent for Python, one for Kubernetes, one for security, one for testing.
    
- Better tool usage — each agent can have a preferred set of tools.
    
- Higher quality outputs — the agent carries domain-specific workflows.
    
- Multi-agent orchestration — an orchestrator can delegate tasks to the right specialist.
    

### How This Applies to Your Autofix System

For your Autofix platform, you could have:

### root-cause-investigator.agent.md

- Query Splunk and Dynatrace
    
- Traverse Neo4j dependency graph
    
- Search code via OpenGrok
    
- Produce probable root causes
    

### java-autofix.agent.md

- Apply fixes using project conventions
    
- Generate tests
    
- Run builds
    
- Create patch sets
    

### security-review.agent.md

- Run SAST checks
    
- Detect secrets and injection risks
    
- Validate dependency upgrades
    
- Produce security report
    

### pr-reviewer.agent.md

- Review code changes
    
- Check architecture constraints
    
- Verify tests
    
- Approve or request changes
    

### Final Mental Model

### A coding agent ecosystem

### AGENTS.md

Global rules for the repository

- Architecture constraints
    
- Testing requirements
    
- Coding standards
    

### *.agent.md

Specialized workers

- Python MCP Expert
    
- Java Autofix Engineer
    
- Kubernetes SRE
    
- Security Auditor
    

### skill.md

Reusable procedures

- Debug a failing build
    
- Create an MCP server
    
- Perform root-cause analysis
    
- Write a migration
    

### Tools

Execution capabilities

- OpenGrok
    
- Neo4j
    
- Milvus
    
- Splunk
    
- Jira
    
- GitHub
    
- Kubernetes
    

So the most accurate statement is:

Instructions tell the model how to behave.

Skills tell the model how to perform a task.

Tools give the model capabilities.

An agent combines role + instructions + skills + tools + output contracts into a specialized worker.

That is why a file like python-mcp-expert.agent.md feels similar to instructions and skills: it contains them, but also adds identity, scope, workflows, and tool preferences. It is a deployment unit for expertise, not just a rule file.



--------


**Here’s a comprehensive set of examples** for DevOps / Platform Engineering tasks, along with the **recommended folder structure**.

---

### **Full Recommended Folder Structure**

```bash
.github/
├── copilot-instructions.md          # ← Global Instructions (Copilot)
├── AGENTS.md                        # ← Main Instructions (Shared)
├── CLAUDE.md                        # ← Claude-specific (can @import AGENTS.md)

.agents/                             # ← Main folder for AI customizations
├── instructions/
│   └── platform-standards.md
│
├── skills/                          # ← Reusable Skills
│   ├── setup-cicd/
│   │   └── SKILL.md
│   ├── review-iac/
│   │   └── SKILL.md
│   ├── provision-environment/
│   │   └── SKILL.md
│   ├── add-monitoring/
│   │   └── SKILL.md
│   └── ...
│
└── agents/                          # ← Custom Agents
    ├── platform-engineer.agent.md
    ├── cicd-specialist.agent.md
    └── observability-expert.agent.md
```

---

### **1. Instructions** (Global Standards)

**File**: `.github/AGENTS.md` (or `CLAUDE.md`)

```markdown
# Platform Engineering Standards

## General Rules
- Use Terraform for IaC
- All pipelines must use GitHub Actions
- Follow GitOps principles
- Services must be deployed to Kubernetes
- Security scanning is mandatory

## CI/CD Standards
- Always include linting, unit tests, security scan, and container scan
- Use semantic versioning
- Deploy to staging → production with manual approval for prod

## IaC Best Practices
- Modular Terraform structure
- Use data sources instead of hardcoding
- Enforce least privilege

## Monitoring Standards
- OpenTelemetry + Prometheus + Grafana + Loki
- SLOs must be defined
```

---

### **2. Skills Examples**

#### **Skill 1: Setup CI/CD Pipeline**

**Folder**: `.agents/skills/setup-cicd/SKILL.md`

```markdown
# SKILL: Setup CI/CD Pipeline

## Description
Creates or updates a complete GitHub Actions CI/CD pipeline following platform standards.

## Trigger Words
setup cicd, create pipeline, github actions pipeline, ci/cd setup

## Steps
1. Analyze project (language, framework, Dockerfile presence)
2. Create `.github/workflows/ci-cd.yml`
3. Include: lint → test → build → security scan → push to registry → deploy to staging
4. Add environment secrets handling
5. Add manual approval gate for production

## Standards to Follow
- Use our standard matrix for testing
- Include Trivy security scan
- Use semantic versioning
- Follow AGENTS.md CI/CD rules

## Output
- Full pipeline file with explanation
- Required secrets list
- Testing commands
```

---

#### **Skill 2: IaC Review**

**Folder**: `.agents/skills/review-iac/SKILL.md`

```markdown
# SKILL: Review IaC (Terraform)

## Description
Performs a thorough review of Terraform code with security, best practices, and cost optimization focus.

## Trigger Words
review terraform, iac review, terraform review

## Review Checklist
- Security (IAM permissions, public exposure)
- Cost optimization
- Modularity and reusability
- State management best practices
- Provider pinning
- Input validation
- Error handling

## Output Format
1. Summary (Good / Needs Improvement)
2. Critical Issues (with fixes)
3. Recommendations
4. Refactored code suggestions (if applicable)
```

---

#### **Skill 3: Environment Provisioning**

**Folder**: `.agents/skills/provision-environment/SKILL.md`

```markdown
# SKILL: Provision New Environment

## Description
Provisions a new environment (dev/staging/pre-prod) using Terraform + GitOps.

## Trigger Words
provision environment, create namespace, new environment

## Steps
1. Create Terraform module for namespace
2. Setup RBAC, Network Policies, Resource Quotas
3. Provision monitoring stack (if requested)
4. Create GitHub repository environment + secrets
5. Update ArgoCD / Flux configuration

## Standards
- Follow least privilege
- Use sealed secrets
- Add proper labels and annotations
```

---

### **3. Agent Examples**

#### **Agent: Platform Engineer**

**File**: `.agents/agents/platform-engineer.agent.md`

```markdown
# Agent: Senior Platform Engineer

## Persona
You are a Principal Platform Engineer with 12+ years experience in Kubernetes, GitOps, and SRE practices.

## Core Responsibilities
- Design and implement scalable platform solutions
- Enforce platform golden paths
- Improve developer experience
- Maintain high reliability and security standards

## Tools & Capabilities
- Terraform, Helm, Kubernetes, GitHub Actions, ArgoCD
- Can read/write files, run commands, validate deployments

## Working Style
1. Always create a detailed plan first and get approval
2. Consider cost, security, scalability, and observability
3. Document decisions and trade-offs
4. Follow AGENTS.md standards strictly

## Specialties
- CI/CD pipelines
- IaC (Terraform)
- Environment provisioning
- Observability & SRE practices
```

---

### How to Use Them Together (Best Flow)

1. Keep global rules in **AGENTS.md** (Instructions)
2. Use **Skills** for 80% of day-to-day tasks (most efficient)
3. Activate **Agents** when working on complex, multi-step projects

**Example Command**:
- Skill: `"Use setup-cicd skill for the payment service"`
- Agent: `"@PlatformEngineer design and implement CI/CD + monitoring for the new recommendation service"`

---
### Custom instruction.md


```
==GitHub Copilot instruction files are injected into the AI's prompt as invisible system rules==. While `.github/copilot-instructions.md` acts as a repository-wide baseline, `.github/instructions/*.md` files provide granular, **task-specific guidelines** that are triggered contextually by the files or directories you are working on. [[1](https://www.reddit.com/r/GithubCopilot/comments/1rdn29i/does_copilotinstructionsmd_get_injected_into/), [2](https://github.com/orgs/community/discussions/170581), [3](https://www.reddit.com/r/GithubCopilot/comments/1kvtrms/how_do_you_setup_your_copilotinstructionsmd/), [4](https://nivedv.medium.com/before-the-agent-starts-how-github-copilots-customization-layer-actually-works-a7db689c795e), [5](https://github.blog/ai-and-ml/github-copilot/how-githubs-agentic-security-principles-make-our-ai-agents-as-secure-as-possible/)]

How They Work

- **Scope definition (`applyTo`):** Task-specific instructions use YAML frontmatter to declare which files they apply to (e.g., `applyTo: "/**/*.py"` for Python files). [[1](https://gist.github.com/0xdevalias/f40bc5a6f84c4c5ad862e314894b2fa6), [2](https://nivedv.medium.com/before-the-agent-starts-how-github-copilots-customization-layer-actually-works-a7db689c795e)]

- **Dynamic loading:** When you invoke Copilot in chat or ask for code generation, Copilot evaluates your currently opened files or the files you've explicitly added as references. It merges all relevant `.instructions.md` files together with your global `copilot-instructions.md` file. [[1](https://github.com/microsoft/copilot-for-eclipse/issues/62), [2](https://nivedv.medium.com/before-the-agent-starts-how-github-copilots-customization-layer-actually-works-a7db689c795e), [3](https://github.com/orgs/community/discussions/170581), [4](https://github.com/orgs/community/discussions/178108), [5](https://awesome-copilot.github.com/learning-hub/understanding-copilot-context/)]

- **Behavior adjustment:** Copilot dynamically obeys these appended rules for formatting, framework constraints, and architectural guidelines. [[1](https://www.reddit.com/r/GithubCopilot/comments/1kvtrms/how_do_you_setup_your_copilotinstructionsmd/), [2](https://www.reddit.com/r/GithubCopilot/comments/1rdn29i/does_copilotinstructionsmd_get_injected_into/)]

When the LLM Uses Them in Chat

Copilot uses these instructions in chat and code generation under the following conditions:

- **Automatic Context Matching:** The LLM reads the instruction file during your chat session if you are actively editing or working in the files covered by the `applyTo` rule. [[1](https://nivedv.medium.com/before-the-agent-starts-how-github-copilots-customization-layer-actually-works-a7db689c795e), [2](https://github.com/microsoft/vscode-copilot-release/issues/12878)]

- **Explicit Context Attachment:** Even if an instruction file doesn't auto-apply to your current file, the LLM will use it in chat if you manually mention or attach the file using an `#` reference (e.g., `#file:.github/instructions/your-task.md`). [[1](https://github.com/orgs/community/discussions/162201), [2](https://github.com/microsoft/vscode/issues/279045)]

- **Pre-prompt Injections:** Once activated, these files are embedded into the AI's "system prompt" before it responds to your query, ensuring it respects your defined goals,
```