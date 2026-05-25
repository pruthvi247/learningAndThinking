[source-fcc](https://www.youtube.com/watch?v=66hDgWottdA)

Dynamic Programming (DP) is one of those topics that feels mysterious at first—but once you see the **pattern**, it becomes a powerful, practical tool. I’ll explain it **step-by-step**, starting simple, then going deep enough that you can **apply it confidently in interviews and real systems work**.

---

# 1️⃣ Dynamic Programming — AM-5 explanation

Imagine you’re climbing stairs 🪜.

- You can climb **1 step or 2 steps at a time**
    
- You want to know: _How many ways can I reach the top?_
    

Instead of re-thinking every path again and again, you:

- **Remember answers you already figured out**
    
- **Reuse them**
    

👉 **Dynamic Programming = remembering past results to avoid repeating work**

---

# 2️⃣ Why DP exists (the core problem it solves)

Many problems:

- Have **overlapping subproblems**
    
- Have **exponential brute-force solutions**
    

Example (bad approach):

```text
Ways(10) = Ways(9) + Ways(8)
Ways(9)  = Ways(8) + Ways(7)
Ways(8)  = Ways(7) + Ways(6)
```

You can see:

- `Ways(8)` is computed **multiple times**
    

DP avoids this by:

- Computing once
    
- Storing the result
    
- Reusing it
    

---

# 3️⃣ Formal definition (important)

> **Dynamic Programming is an optimization technique used to solve problems by breaking them into overlapping subproblems and storing their solutions.**

Two required properties:

1. **Optimal substructure**
    
2. **Overlapping subproblems**
    

If a problem does NOT have both → DP won’t work.

---

# 4️⃣ The two properties (non-negotiable)

## 1️⃣ Optimal Substructure

A problem’s solution can be built from **solutions to smaller subproblems**.

Example:

- Shortest path to node C
    
- Depends on shortest path to node B
    

## 2️⃣ Overlapping Subproblems

The same subproblem appears **again and again**.

Example:

- Fibonacci
    
- Knapsack
    
- String matching
    

---

# 5️⃣ DP vs Recursion vs Greedy

|Technique|Key idea|When it fails|
|---|---|---|
|Recursion|Solve smaller problems|Repeats work|
|Greedy|Pick best local choice|Not always optimal|
|**DP**|Store + reuse results|Memory/time tradeoff|

DP is **recursion + memory**.

---

# 6️⃣ Two main DP approaches (very important)

## 1️⃣ Top-Down (Memoization)

- Write recursive solution
    
- Store results in cache
    

Example (Fibonacci):

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

✅ Easy to write  
❌ Recursive stack overhead

---

## 2️⃣ Bottom-Up (Tabulation)

- Build solution from smallest cases
    
- Use loops
    

```python
def fib(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

✅ Faster  
✅ No recursion  
❌ Sometimes harder to think

---

# 7️⃣ How to recognize a DP problem (interview gold)

Ask yourself:

✔ “Can I break this into smaller versions?”  
✔ “Do I recompute the same thing?”  
✔ “Is brute force exponential?”  
✔ “Is the question asking for max/min/count?”

If **yes** → likely DP.

Common DP keywords:

- Maximum / Minimum
    
- Count number of ways
    
- Longest / Shortest
    
- Optimal
    

---

# 8️⃣ DP problem categories (memorize this)

## 1️⃣ 1D DP

- Fibonacci
    
- Climbing stairs
    
- House robber
    

## 2️⃣ 2D DP

- Grid paths
    
- Edit distance
    
- LCS (Longest Common Subsequence)
    

## 3️⃣ Knapsack family

- 0/1 knapsack
    
- Subset sum
    
- Partition problems
    

## 4️⃣ String DP

- Palindromes
    
- Pattern matching
    
- Word break
    

## 5️⃣ Interval DP

- Matrix chain multiplication
    
- Burst balloons
    

---

# 9️⃣ Step-by-step DP problem-solving framework

This is the **most important section**.

### Step 1: Define the state

👉 What does `dp[i]` mean?

Example:

```
dp[i] = max money robbed till house i
```

---

### Step 2: Write the recurrence

👉 How does current state depend on previous?

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

---

### Step 3: Base cases

👉 Smallest inputs

```
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
```

---

### Step 4: Order of computation

- Bottom-up loop
    
- Ensure dependencies are computed first
    

---

### Step 5: Optimize space (optional)

If `dp[i]` depends only on last 2 states → use variables

---

# 🔟 Time & space complexity

|Approach|Time|Space|
|---|---|---|
|Brute force|Exponential|Stack|
|DP|Polynomial|Table|
|Optimized DP|Polynomial|O(1) or O(n)|

DP trades **space for time**.

---

# 1️⃣1️⃣ Common DP mistakes (learn these early)

❌ Wrong state definition  
❌ Missing base cases  
❌ Wrong iteration order  
❌ Using DP when greedy works  
❌ Overcomplicating with recursion

---

# 1️⃣2️⃣ Real-world uses of DP

DP is NOT just interviews.

- Compiler optimization
    
- DNA sequence matching
    
- Speech recognition
    
- Route optimization
    
- Resource allocation
    
- Finance (portfolio optimization)
    

---

# 1️⃣3️⃣ DP vs Divide & Conquer

|Divide & Conquer|Dynamic Programming|
|---|---|
|Independent subproblems|Overlapping subproblems|
|No caching|Caching required|
|Merge step|Recurrence step|

---

# 1️⃣4️⃣ Mental model to remember DP

> **DP is about turning exponential problems into polynomial ones by remembering the past.**

If you forget everything else, remember this.

---

# 1️⃣5️⃣ How I recommend YOU learn DP (practical plan)

Given you’re an experienced engineer:

1. Master **1D DP**
    
2. Move to **2D grid problems**
    
3. Learn **knapsack patterns**
    
4. Learn **string DP**
    
5. Practice **state definition writing**
    

Focus on **patterns**, not memorizing solutions.

---
Perfect. Let’s do this **properly and end-to-end**, the way strong engineers actually learn DP — not memorizing, but **seeing the pattern repeat**.

I’ll split this into **two clear parts**:

---

# PART 1 — Walkthrough of a 1D DP problem (end-to-end)

We’ll use a **canonical** 1D DP problem:

## 🔹 Problem: _Climbing Stairs_

### Problem statement

You’re climbing a staircase with `n` steps.

- You can climb **1 or 2 steps at a time**
    
- How many **distinct ways** can you reach the top?
    

---

## Step 0: Brute force thinking (important first step)

From step `n`, you could have come from:

- `n - 1`
    
- `n - 2`
    

So:

```
ways(n) = ways(n-1) + ways(n-2)
```

But recursion will **repeat work**.

---

## Step 1: Identify DP signals

✔ Count number of ways  
✔ Overlapping subproblems  
✔ Optimal substructure

👉 **Yes, DP problem**

---

## Step 2: Define the DP state (MOST important step)

Ask:

> “What exactly does dp[i] represent?”

### State definition

```
dp[i] = number of ways to reach step i
```

Be very explicit. If this step is wrong, everything breaks.

---

## Step 3: Write the recurrence relation

From step `i`:

- You can come from `i-1`
    
- Or `i-2`
    

So:

```
dp[i] = dp[i-1] + dp[i-2]
```

This is the heart of the solution.

---

## Step 4: Define base cases

Smallest valid problems:

```
dp[0] = 1   # One way to stand still
dp[1] = 1   # One way: 1 step
```

(These are chosen to make recurrence clean.)

---

## Step 5: Decide top-down or bottom-up

We’ll do **bottom-up** (recommended in production code).

---

## Step 6: Implement bottom-up DP

```python
def climbStairs(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

---

## Step 7: Analyze complexity

- **Time:** O(n)
    
- **Space:** O(n)
    

But we can do better.

---

## Step 8: Space optimization (classic DP move)

We only need last **two** values.

```python
def climbStairs(n):
    if n <= 1:
        return 1

    prev2 = 1
    prev1 = 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1
```

✔ Same result  
✔ **O(1) space**

---

## Final mental model

> “At each step, the answer depends only on the last two answers.”

That’s **1D DP in its purest form**.

---

# PART 2 — 1D DP PATTERNS CHEAT SHEET 🧠

This is what you should memorize **by pattern**, not problem.

---

## 🔹 Pattern 1: Fibonacci-like DP

### When you see:

- Ways to reach
    
- Counting paths
    
- Jump 1 or 2 steps
    

### Template:

```
dp[i] = dp[i-1] + dp[i-2]
```

### Examples:

- Climbing stairs
    
- Fibonacci
    
- Tiling problems
    

---

## 🔹 Pattern 2: Take or Skip (House Robber)

### Problem:

Max money, cannot take adjacent elements

### State:

```
dp[i] = max money till index i
```

### Recurrence:

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

### Key idea:

> At every index: **take it or skip it**

---

## 🔹 Pattern 3: Minimum Cost / Minimum Steps

### When you see:

- Min cost
    
- Min jumps
    
- Min operations
    

### Template:

```
dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
```

### Examples:

- Min cost climbing stairs
    
- Coin change (min coins)
    
- Jump game (min jumps)
    

---

## 🔹 Pattern 4: Prefix Decision DP

### When:

- Decisions depend on previous prefix
    
- Linear scan
    

### Template:

```
dp[i] = decision using dp[0..i-1]
```

### Examples:

- Word break
    
- Decode ways
    

---

## 🔹 Pattern 5: Kadane / Subarray DP

### When:

- Max subarray
- Contiguous segment
### State:

```
dp[i] = max subarray ending at i
```

### Recurrence:

```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

### Example:

- Maximum subarray sum
    

---

## 🔹 Pattern 6: Count Ways with Constraints

### Template:

```
dp[i] = sum(dp[i - valid_steps])
```

### Examples:

- Dice roll sum
- Ways to reach score
- Stair variants
   
   ---

# 1D DP MASTER CHECKLIST ✅

Before coding, ask:

1. What does `dp[i] represent`?
2. Is this **max / min / count**?
3. From where can state `i` come?
4. Base cases?
5. Can space be optimized?
If you answer these → you can solve **any 1D DP problem**.

---

