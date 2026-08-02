## Three different things people call “token saving”

### A. Context-window efficiency

Keeping enough working-memory space available for the model to reason and respond.

### B. Cost efficiency

Reducing chargeable input, cached-input, output, tool-call, or premium-request consumption. The exact billing mechanism depends on the model and product.

### C. Quality efficiency

Preventing useful information from being buried under irrelevant files, duplicated instructions, old conversations, and verbose tool output.

The most important objective for a coding session is usually **quality efficiency**.

# Part 1: Scope the request before adding context

## Tip 1: Define the outcome, not just the activity

A vague request causes the model to explore, infer, generate, and explain more than necessary.

### Token-wasteful request
```text
Review the project and improve the authentication code.
```
This leaves many questions unanswered:

- Which part of authentication?
- Is the task a bug fix, redesign, or security review?
- Which files matter?
- Should the model modify code?
- What output is expected?
- How much of the repository should be explored?
### Token-smart request
```
Review the refresh-token validation flow
Goal:

Identify why expired refresh tokens are sometimes accepted.

Return:

1. Root cause
2. Evidence with file and function references
3. Smallest safe fix
4. Tests that should be added
Do not modify files yet.
```

### Why this saves tokens

The second prompt reduces:

- Repository exploration
- Unnecessary file retrieval
- Speculative analysis
- Unrelated recommendations
- Premature code generation
- Follow-up correction messages
### Reusable formula

Use this structure:
```
Goal:

[What outcome is required?]

Context:

[What happened, and what should happen?]

Scope:

[Which files, functions, or services are relevant?]

Constraints:

[What must not change?]
Deliverable:

[What should the response contain?]
Execution boundary:

[Analyze only, create a plan, or implement and verify?]
```

## Tip 2: Use the smallest sufficient scope

Do not give the model the entire repository when one function and one test file are enough.

### Too broad
```
Review @src/ and fix the problem.
```
### Better
```
Inspect @src/catalog/books.py and @tests/test_books.py.

///The Context funnel Start narrow and expand only when evidence requires expansion:
Start with:
- books.py
- test_books.py
- The reported error

If these are insufficient to establish the root cause:

1. Identify the next file needed.
2. Explain why it is needed.
3. Inspect no more than two additional files at a time.
```
GitHub Copilot CLI supports using `@` references for specific files and directories, while VS Code chat supports attaching and referencing relevant context.
This is particularly useful for:

- Large monorepositories
- Microservice systems
- Legacy applications
- Incidents containing large amounts of log data
- Agents with repository search tools

## Tip 4: Send the relevant error slice, not every log line

Long logs often contain repeated stack traces, timestamps, health checks, and unrelated events.

### Wasteful
```
Analyze this 20,000-line production log.
```
### Better
```
Investigate the checkout failure.

Use:

- The first occurrence of ERROR-421
- 50 lines before and after the error
- The associated request ID
- The relevant stack trace
- Deployment changes from the preceding 30 minutes

Ignore:

- Health-check traffic
- Duplicate retries
- Unrelated request IDs
```
### First reduce logs deterministically

Before asking an AI to reason about logs, use conventional tools to:

- Filter by correlation or request ID
- Remove duplicate exceptions
- Limit the time range
- Extract warning and error severity
- Select the first failure, not every downstream failure
- Group repeated messages
- Remove routine health-check events

AI should analyze the evidence, not perform avoidable text cleanup.

# Part 2: Keep permanent context lean

## Tip 5: Put only stable rules in always-on instructions

Repository instructions may be included in many or all requests, depending on their scope. Every unnecessary paragraph can therefore become repeated context.

### Good permanent instructions
```
## Runtime
- Use Python 3.12.
- Use type hints on public functions.

## Architecture

- Domain code must not import infrastructure adapters.
- Preserve public API compatibility.
- Use the existing logger instead of prin

## Error handling

- Use the existing AppError hierarchy.
- Never expose internal exception messages to clients.

## Verification

- Run focused tests before the full test suite.
- Use pytest for tests.
- Report actual commands and results.
```

### Token advantage

Python rules do not need to accompany a Terraform-only task, and Terraform rules do not need to accompany a React component request.
### Terraform-specific instructions
```
---

applyTo: "**/*.tf"

---
- Pin provider versions.
- Do not hardcode account IDs or regions.
- Use existing modules before creating new resources.
- Run terraform fmt and terraform validate.
```
VS Code supports targeted `*.instructions.md` files with `applyTo` patterns so instructions can apply to specific files, languages, frameworks, or folders

## Tip 8: Remove duplicated and contradictory instructions

```
- Follow docs/api-standards.md when modifying public API handlers.

- For this task, inspect only the sections on error responses and pagination.
```

>However, do not assume the model will automatically retrieve the referenced document. Explicitly attach or reference the source when it is relevant:

### prompt
```
Review #file:docs/api-standards.md sections:

- Error responses
- Pagination

Then apply those rules to #file:src/api/orders.ts.
```

# Part 3: Choose the right customization layer

## Tip 9: Do not make everything an always-on instruction

Use the correct storage layer:
1. Use instructions for stable policy
2. Use a prompt file for a manually invoked, repeatable request
	Examples:
	- `/review-api`
	- `/prepare-pr`
	- `/debug-test`
	- `/generate-migration-plan`
3. Use a skill for reusable expertise
	Examples:
	- Diagnose a failed CI pipeline
	- Review Terraform for security and cost
	- Create a database migration
	- Add service observability
4. Use a custom agent for a specialist role
	Examples:
	- Security reviewer
	- Platform engineer
	- Read-only architecture planner
	- Production incident investigat
5. Use tools or MCP for external capabilities
	Examples:
	- Query Jira
	- Read Kubernetes resources
	- Search logs
	- Inspect GitHub issues
	- Retrieve service-catalog data
6. dafafa
7. dafa

VS Code distinguishes instructions, prompt files, agent skills, custom agents, MCP servers, hooks, and plugins because they solve different customization needs.

### Why this is token-smart

The primary advantage is not that the saved text magically disappears. The advantages are:

- Less repeated manual prompting
- More consistent scope
- Fewer correction turns
- Fewer forgotten constraints
- Better team-wide reuse
- Easier maintenance of the workflow in one place

# Part 4: Manage conversation history

## Tip 13: Use one session for one coherent goal

A chat session accumulates history. Keeping unrelated tasks in the same session may make old decisions and irrelevant files compete with the new problem.

### Continue a session when

- You are still solving the same defect
- The earlier design decision remains relevant
- The model needs the current patch
- The next action depends directly on prior analysis

### Start a new session when

- You switch to an unrelated feature
- You move to another repository
- Old assumptions are no longer valid
- The model keeps referring to abandoned approaches
- A debugging session has accumulated excessive logs
- The current goal can be explained more cleanly from scratch

VS Code supports chat history, separate sessions, and parallel sessions, allowing developers to isolate unrelated work without losing prior conversations

## Tip 14: Create a compact handoff before resetting

When the session becomes long, ask the model to produce a verified handoff.
```
Create a compact handoff for continuing this task in a clean session.

Include only:
- Original goal
- Confirmed facts
- Root cause
- Decisions made
- Files changed
- Current test status
- Remaining risks
- Next action

Exclude:
- Abandoned approaches
- Repeated discussion
- Speculation that was disproved
- Full source-code copies
  
For each fact in the handoff, label it as:
- Verified in code
- Verified by test
- User-provided requirement
- Unverified assumption
```

Before relying on the summary, inspect it for accuracy. A compact but incorrect summary is worse than a long correct history.

# Part 5: Control model output

## Tip 16: Ask for bounded deliverables

Output tokens also matter. A request such as “explain everything in detail” invites unnecessary generation.
### Useful output controls

- “Return at most five findings.”
- “Show only changed functions.”
- “Do not repeat unchanged code.”
- “Provide a unified diff rather than the full file.”
- “Limit the explanation to the root cause and trade-offs.”
- “Do not explain standard language syntax.”
- “List only assumptions that affect implementation.”
- “Report passing tests as a one-line summary.”
- “Expand only failed checks.”

# Part 6: Optimize tool use

## Tip 20: Give agents only relevant tools

Tool schemas and tool results may consume context. Too many available tools can also increase decision complexity.

### Security-review agent might need

- Repository read
- Git diff
- Test execution
- Dependency scanner
- Static analysis

### Security-review agent probably does not need

- Production deployment
- Database mutation
- Namespace deletion
- Ticket creation
- Browser automation

# Part 9: Common myths and mistakes

## Myth 1: “A shorter prompt is always better”

A short but ambiguous prompt may cause large repository searches, excessive explanations, wrong implementations, and several correction turns.

Better principle:

> **Be concise, but include every constraint that changes the answer.**

---

## Myth 2: “Attach the entire repository so the AI understands everything”

Large context may bury the target evidence and consume working memory. Start from the failing behaviour and direct code path, then expand selectively. More context does not guarantee better performance. [[platform.claude.com]](https://platform.claude.com/docs/en/build-with-claude/context-windows), [[awesome-co...github.com]](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/02-context-and-conversations/)

---

## Myth 3: “Summarize every file before doing anything”

Summaries are useful for discovery, but unnecessary when the target function, expected behaviour, and relevant test are already known.

---

## Myth 4: “Put every best practice into repository instructions”

Always-on instructions should contain stable, high-value project rules. Detailed repeatable procedures belong in prompts or skills.

---

## Myth 5: “One giant prompt saves tokens because it is only one request”

A giant request may mix analysis, planning, implementation, testing, documentation, and optimization. If an early assumption is wrong, most generated work is wasted.

---

## Myth 6: “Skills always use fewer tokens than agents”

There is no universal ranking. Actual usage depends on:

- Product implementation
- Loaded metadata
- Skill size
- Agent instructions
- Available tool definitions
- Retrieved resources
- Conversation history
- Tool-call results
- Generated output

A more reliable rule is:

> **Keep always-on material lean and load detailed expertise only when relevant.**

---

## Myth 7: “Ask the AI to ignore irrelevant content”

If possible, do not send irrelevant content in the first place. Telling the model to ignore 5,000 lines still means the content occupies context.

# Part 10: A token-efficiency checklist

## Before sending

- Is the outcome explicit?
- Is current versus expected behaviour clear?
- Have I identified the smallest relevant scope?
- Can I reference files instead of pasting them?
- Have I filtered logs and tool results?
- Have I stated what must not change?
- Is the current task analysis, planning, implementation, or verification?
- Is the requested output bounded?

## During execution

- Is the agent exploring unrelated files?
- Is the same document being repeatedly attached?
- Are tools returning unfiltered output?
- Is the conversation mixing unrelated goals?
- Is the agent generating code before confirming the root cause?
- Can deterministic tools perform part of the work?
- Should the context be expanded only one or two files at a time?

## After execution

- Were actual tests run?
- Can passing output be summarized?
- Should the workflow become a prompt file or skill?
- Can duplicated instructions be removed?
- Is the session now carrying obsolete investigation history?
- Should a compact handoff be created?
- Are unverified assumptions clearly separated from confirmed facts?


