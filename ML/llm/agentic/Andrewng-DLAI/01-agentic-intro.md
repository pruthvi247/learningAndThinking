![[Screenshot 2025-10-30 at 7.28.55 PM.png]]
[image-source](https://www.youtube.com/watch?v=kqB_xML1SfA)

# Intro
![[Pasted image 20251031082141.png]]

> One of the question with agentic workflow is how autonomous are they ??

![[Pasted image 20251031082932.png]]
![[Pasted image 20251031083128.png]]
> Agentic workflow is slower than non agentic workflow  since, Agentic worlflow think and plan,.. this can be over come by parallelization, and still can be faster than human

![[Pasted image 20251031083624.png]]
# Task Decomposition
![[Pasted image 20251031084547.png]]
1. Extract order details → (LLM)
2. Query the database → (tool/function)
3. Draft and send the reply → (LLM + API)
# Evaluating Agentic Ai (evals)
![[Pasted image 20251031091232.png]]

- can evaluate using code (Objective evals), or LLM-as judge (Subjective evals)
- Two types of evals : end-to-end and component-level


![[Pasted image 20251031091918.png]]

# Agentic Design Pattern 
- Reflection
- ToolUse
- Planning
- Multi-agent collaboration

**1. Reflection  
**This is the agent’s ability to perform self-evaluation after each action. It’s not just post-hoc logging, it’s part of the control loop.

Agents ask:

- Was the subtask successful?
- Did the tool/API return the expected structure or value?
- Is the plan still valid given current memory state?

Techniques include:

- Internal scoring functions.
- Critic models trained on trajectory outcomes.
- Reasoning chains that validate step outputs.

Without reflection, agents remain brittle, but with it, they become self-correcting systems.

**2. Tool-Use  
**LLMs alone can’t interface with the world. Tools enables agents to execute code, perform retrieval, query databases, call APIs, and trigger external workflows. Tool-use design involves:

- Function calling or JSON schema execution (OpenAI, LangChain, etc.)
- Grounding outputs into structured results (e.g., SQL, Python, REST)
- Chaining results into subsequent reasoning steps

This is how you move from “text generators” to capability-driven agents.

**3. Planning  
**Planning is the core of long-horizon task execution. Let the agent decide the sequence of steps instead of hard-coding them. Agents must:

- Decompose high-level goals into atomic steps.
- Sequence tasks based on constraints and dependencies.
- Update plans reactively when intermediate states deviate.

Design patterns here include:

- Chain-of-thought with memory rehydration.
- Execution DAGs or LangGraph flows.
- Priority queues and re-entrant agents.

Planning separates short-term LLM chains from persistent agentic workflows.

**4. Multi-Agent Collaboration  
**As task complexity grows, specialization becomes essential. Multi-agent systems allow modularity, separation of concerns, and distributed execution. This involves:

- Specialized agents: planner, retriever, executor and validator.
- Communication protocols: Model Context Protocol (MCP), A2A messaging, etc.
- Shared context: via centralized memory, vector DBs, or message buses.

This mirrors multi-threaded systems in software, except now the “threads” are intelligent and autonomous.