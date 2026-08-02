![[Screenshot 2026-07-21 at 10.31.51 PM.png]]

**Why this session matters ?**
![[1784090182313.jpeg]]

✅ You define the business requirement.  
✅ You provide the context.  
✅ You review the output.  
✅ You make the final decision.

But without clear instructions, it's just a very fast assistant.  
  
**Remember:**
👉 AI follows prompts.  
👉 AI follows rules.  
👉 AI follows business logic.


_By the end of the session, team should be able to:_

- Structure coding requests before asking for code
- Supply only the context that affects the decision
- Distinguish between **instructions, prompt files, skills, agents, tools, and MCP**
- Reduce noise, repetition, and unnecessary tool use
- Create one reusable Copilot customisation
- Validate AI-generated code instead of accepting “AI slop”
- **Leave with a practical adoption plan**


> Resources : https://wiki.one.int.sap/wiki/x/oUV3dgE
# Chapter 1: Your question is the smallest piece


![[Pasted image 20260721224203.png]]

>**Implication:** shrinking your own message saves almost nothing. The leverage is in the other five segments.

==Prompt-Engieering==
The user prompt is only one component of the full model request.

```text
FULL MODEL REQUEST

│
├── 1. System and platform layer
│   ├── System instructions
│   ├── Safety and operational constraints
│   ├── General product behaviour
│   └── Response and formatting rules
│
├── 2. Customization layer
│   ├── Organization instructions
│   ├── Repository instructions
│   ├── File-specific instructions
│   ├── Custom-agent instructions
│   ├── Prompt-file instructions
│   └── Relevant skill metadata or body
│
├── 3. Capability layer
│   ├── Available tools
│   ├── Tool schemas
│   ├── MCP tools and resources
│   ├── Tool-use instructions
│   ├── Permissions
│   └── Execution constraints
│
├── 4. Working-context layer
│   ├── Conversation history
│   ├── Retrieved files
│   ├── Search results
│   ├── Editor context
│   ├── Selected code
│   ├── Open files
│   ├── Terminal output
│   ├── Diagnostics
│   └── Git diff
│
├── 5. Immediate user request
│   ├── Goal
│   ├── Requirements
│   ├── Constraints
│   └── Expected deliverable
│
└── 6. Generated work
    ├── Reasoning and planning
    ├── Tool calls
    ├── Tool results
    └── Final response
```

## 1. System instructions/prompt

System instructions define the highest-level behaviour of the model inside an application.

`CMD+SHiFT+P > show chat debug view `


![[Pasted image 20260721225932.png]]
![[Pasted image 20260722024908.png]]
## Tool definitions

Agents need descriptions of the tools they can call.
`open chat > top right three dots > show agent debug logs`

----
# Question 

 When you hear the phrase **token saving,** what thoughts occur to you?
## Answer
### Three different things people call “token saving”

 **A. Context-window efficiency**

Keeping enough working-memory space available for the model to reason and respond.

**B. Cost efficiency**

Reducing chargeable input, cached-input, output, tool-call, or premium-request consumption. The exact billing mechanism depends on the model and product.

**C. Quality efficiency**

Preventing useful information from being buried under irrelevant files, duplicated instructions, old conversations, and verbose tool output.

The most important objective for a coding session is usually **quality efficiency**.
 -----
 



---------

# Chapter 2: Context engineering

_Context engineering_ is the practice of giving an AI the right information, at the right time, in a form it can use, while excluding information that does not affect the task.

## The colleague analogy

> Imagine calling a colleague and saying, “The application is broken.”
> 
> The colleague will ask:
> 
> - Which application?
> - What action failed?
> - What error appeared?
> - Which file is involved?
> - What should have happened?
> - What changed recently?

AI needs the same task-relevant context

Layered context (Instructions → Skills → Agents)

------------

# ➪ 🛠️DEMO🙅🏼‍♂️🚧



-----------------


# Chapter 3: Instructions, Prompts,Skills, Agents

## The Evolution

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
 └── Agent
```

_The more we move downward, the more autonomous the system becomes._
### 0. **Prompt** (Basic)
Use a prompt file for a manually invoked, repeatable request
Prompt files in _VS Code_use the `.prompt.md` extension, can be invoked as slash commands

`Role + Task + Context + Constraints + Output Format`

**Examples**:
```
- /review-api
- /prepare-pr
- /debug-test
- /generate-migration-plan
```
**Strengths**
- Less repeated manual prompting
- More consistent scope
- Easier maintenance of the workflow in one place

==Hands-on Exercises==

_wiki_: https://wiki.one.int.sap/wiki/spaces/CentralQuality/pages/6282495393/Brow+Bag-+artifacts#BrowBagartifacts-Prompts.md

_VScode:_ `/create-prompt`

![[Screenshot 2026-07-22 at 1.10.27 AM.png]]
### 1. **Instructions** (The Foundation)

**What they are**: Persistent, always-active guidelines that shape how the AI behaves. `Coding standards applied automatically by file pattern (*.instructions.md)`
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

==Hands-on Exercises==
_VScode:_ `/create-instructions`
![[Screenshot 2026-07-22 at 12.44.15 AM.png]]

### 2. **Skills** (The Sweet Spot for Most Teams)

**What they are**: Self-contained, reusable mini-programs or bundled assets.

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

**VScode** : `cmd+shift+p > show settings > skills`
**VScode** : `cmd+shift+p > show chat debug view`

==Hands-on Exercises==

_VScode:_ `/create-skills`
_Wiki_: https://wiki.one.int.sap/wiki/x/oUV3dgE
_Awesome-copilot_: https://awesome-copilot.github.com/skills/

![[Screenshot 2026-07-22 at 1.34.43 AM.png]]



# Skills vs Prompts


### 3. **Agents** (The Power User / Autonomous Option)

**What they are**: Specialized AI personas with defined roles, tools, and workflows.

**Key Difference**: Agents are **active** — they can plan, use tools, make decisions, and execute multi-step tasks.
```
                Agent
               /  |  \
              /   |   \
             /    |    \
     Instructions Skills Tools
```

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

==Hands-on Exercises==

_VScode:_ `/create-agents`
_Awesome-copilot_: https://awesome-copilot.github.com/agent/linkedin-post-writer/
![[Screenshot 2026-07-22 at 2.07.25 AM.png]]

# 4. **Tools** (MCP)

LLMs cannot
- read files
- execute code
- call APIs
- browse repositories

They need tools.

**Example**
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

>Tools give abilities. Skills know when to use them.
### 5. **Plugins** (Extensibility Layer)

**What they are**: Add new capabilities, tools, or integrations.

**Examples**:

- Browser automation plugin
- Database query plugin
- Design system integration
- Memory / RAG plugins

**Current Trend (2026)**: Many things that used to be plugins are evolving into **Skills** or being replaced by **MCP (Model Control Protocol)** servers.

**Comparison table**

| Aspect                  | **Instructions**                                    | **Skills**                       | **Agents**                         |
| ----------------------- | --------------------------------------------------- | -------------------------------- | ---------------------------------- |
| **Purpose**             | Persistent rules & style guidelines                 | Reusable, focused tasks          | Full autonomous persona + workflow |
| **Scope**               | Passive, always-on                                  | On-demand, task-specific         | Active, goal-oriented              |
| **File Type**           | `AGENTS.md`, `copilot-instructions.md`, `CLAUDE.md` | `SKILL.md` files in folders      | `*.agent.md`                       |
| **When it loads**       | At session start                                    | When triggered (name or keyword) | When explicitly selected           |
| **Complexity**          | Low                                                 | Medium                           | High                               |
| **Best For**            | Coding standards, preferences                       | Common repeatable tasks          | Complex, multi-step projects       |
| **Token Impact**        | Medium (always present)                             | Low (loaded only when needed)    | High                               |
| **Copilot Support**     | Excellent                                           | Excellent                        | Very Strong (Custom Agents)        |
| **Claude Code Support** | Excellent (`CLAUDE.md`)                             | Strong                           | Strong (Sub-agents)                |


**Use this decision framework**:

1. **Is it a rule or preference?** → **Instructions**
2. **Is it a repeatable task?** → **Skills** (Recommended for most teams)
3. **Is it a complex, multi-step workflow or role?** → **Agents**
4. **Do I need new tools or external integrations?** → **Plugins** / MCP

# Chapter 4: Tips
## Optimise tool use

**Give agents only relevant tools**

Tool schemas and tool results may consume context. Too many available tools can also increase decision complexity.
#### Security-review agent might need

- Repository read
- Git diff
- Test execution
- Dependency scanner
- Static analysis
#### Security-review agent probably does not need

- Production deployment
- Database mutation
- Namespace deletion
- Ticket creation
- Browser automation

## A token-efficiency checklist

#### Before sending

- Is the outcome explicit?
- Is current versus expected behaviour clear?
- Have I identified the smallest relevant scope?
- Can I reference files instead of pasting them?
- Have I filtered logs and tool results?
- Have I stated what must not change?
- Is the current task analysis, planning, implementation, or verification?
- Is the requested output bounded?

#### During execution

- Is the agent exploring unrelated files?
- Is the same document being repeatedly attached?
- Are tools returning unfiltered output?
- Is the conversation mixing unrelated goals?
- Is the agent generating code before confirming the root cause?
- Can deterministic tools perform part of the work?
- Should the context be expanded only one or two files at a time?

#### After execution

- Were actual tests run?
- Can passing output be summarized?
- Should the workflow become a prompt file or skill?
- Can duplicated instructions be removed?
- Is the session now carrying obsolete investigation history?
- Should a compact handoff be created?
- Are unverified assumptions clearly separated from confirmed facts?

## Coding assistants structure
Many AI frameworks become confusing because different vendors use different names:

**Where Instructions Live**

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

# Summary:

| Use Case                                 | Best Choice                 | Reason                     |
| ---------------------------------------- | --------------------------- | -------------------------- |
| Enforce standards                        | **Instructions**            | Always active              |
| Common repeatable task                   | **Skill**                   | Best balance (Recommended) |
| Complex, multi-step, decision-heavy task | **Agent**                   | Maximum intelligence       |
| One-time or very unique task             | Plain prompt + Instructions | No need for overhead       |

**Human-to-AI analogy**

|In an engineering organization|AI customization|
|---|---|
|Company policy|Instructions|
|Checklist or runbook|Prompt file|
|Professional training and SOP|Skill|
|Laptop, terminal, Git, Jira|Tools and MCP|
|Specialist employee|Custom agent|
|Working notes and past decisions|Memory|
|Engineering manager|Planner or orchestrator|

**Full Recommended Folder Structure**
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
![[Pasted image 20260722023302.png]]



# Resources 

- [Token-optimizer-playbook](https://ashy-dune-0b4215a0f.7.azurestaticapps.net/detailed/index.html#/playbook)
- [AI Engineering Fluency](https://marketplace.visualstudio.com/items?itemName=RobBos.ai-engineering-fluency)
- [Awesome GitHub Copilot](https://awesome-copilot.github.com/)
- [CLI workflows](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/03-development-workflows/)
- [Customize-copilot-guide](https://code.visualstudio.com/docs/agents/guides/customize-copilot-guide)



==Which new Skills should we create as a team?==

# Thank You ! 🙏🏻 
Let’s keep sharing what works!" 