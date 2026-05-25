![[Pasted image 20260202130524.png]]
## Measure Before We Optimize

Our intuition about performance bottlenecks is usually wrong. We might spend days optimizing a function we think is slow, only to discover through profiling that some completely different part of the code is the actual problem.

This is why the main rule of performance optimization is to measure first and optimize second. Modern programming languages and platforms provide excellent profiling tools that show us exactly where our program spends its time. These tools track CPU usage, memory allocations, I/O operations, and lock contention in multi-threaded programs.

The basic profiling approach is straightforward.

- First, we run our program under a profiler using realistic workloads, not toy examples. The profile shows us which functions consume the most time.
    
- Sometimes, however, we encounter what’s called a flat profile. This is when no single function dominates the runtime. Instead, many functions each contribute a small percentage. This situation is actually common in mature codebases where the obvious bottlenecks have already been fixed. When facing a flat profile, our strategy shifts. We look for patterns across multiple functions, consider structural changes higher up in the call chain, or focus on accumulating many small improvements rather than one big win.
    

The key point is that we should let data guide our optimization decisions.

## Algorithmic Wins

The most important performance improvements almost always come from choosing better algorithms and data structures. A better algorithm can provide a 10x or 100x speedup, dwarfing any micro-optimization we make.

Consider a common scenario: we have two lists and need to find which items from the first list exist in the second. The naive approach uses nested loops. For each item in list A, we scan through all of list B looking for a match. If each list has 1000 items, that’s potentially one million comparisons. This is an O(N²) algorithm, meaning the work grows with the square of the input size.​​
## Memory Matters

Modern CPUs are incredibly fast, but they can only work on data that’s in their small, ultra-fast caches. When the data they need isn’t in cache, they have to fetch it from main memory, which is much slower. This difference is so significant that the layout of our data in memory often matters more than the algorithmic complexity of our code.

See the diagram below:
![[Pasted image 20260202130833.png]]
The fundamental principle here is locality: data that is accessed together should be stored together in memory. When the CPU fetches data from memory, it doesn’t fetch just one byte. It fetches an entire cache line, typically 64 bytes. If our related data is scattered across memory, we waste cache lines and constantly fetch new data. If it’s packed together, we get multiple pieces of related data in each cache line.

Consider two ways to store a list of user records:

- We could have an array of pointers, where each pointer points to a user object allocated somewhere else in memory.
    
- Or we could have a single contiguous array where all user objects are stored sequentially.
    

The first approach means that accessing each user requires chasing a pointer, and each user object might be on a different cache line. The second approach means that once we fetch the first user, the next several users are likely already in cache.

This is why arrays and vectors typically outperform linked lists for most operations, even though linked lists have theoretical advantages for insertions and deletions. The cache efficiency of sequential access usually dominates.

Reducing the memory footprint also helps. Smaller data structures mean more fit in cache. If we’re using a 64-bit integer to store values that never exceed 255, we’re wasting memory. Using an 8-bit type instead means we can fit eight times as many values in the same cache line. Similarly, removing unnecessary fields from frequently accessed objects can have a measurable impact.

The access pattern matters too. Sequential access through an array is much faster than random access. If we’re summing a million numbers stored in an array, it’s fast because we access them sequentially and the CPU can predict what we’ll need next. If those same numbers are in a linked list, each access requires chasing a pointer to an unpredictable location, destroying cache efficiency.

The practical takeaway is to prefer contiguous storage (arrays, vectors) over scattered storage (linked lists, maps) when performance matters. Keep related data together, and access it sequentially when possible.

## Avoid Unnecessary Work

The fastest code is code that never runs. Before we optimize how we do something, we should ask whether we need to do it at all or whether we can do it less frequently.

Some common strategies for the same are as follows:

- Creating fast paths for common cases is a powerful technique. In many systems, 80% of cases follow a simple pattern while 20% require complex handling. If we can identify the common case and create an optimized path for it, most operations become faster even though the complex case remains unchanged. For example, if most strings in our system are short, we can optimize specifically for short strings while keeping the general implementation for longer ones.
    
- Precomputation and caching exploit the idea that calculating something once is cheaper than calculating it repeatedly. If we have a value that doesn’t change during a loop, we should calculate it before the loop, not on every iteration. If we have an expensive calculation whose result might be needed multiple times, we should cache it after computing it the first time.
    
- Lazy evaluation defers work until we know it’s actually needed. If we’re building a complex report that the user might never request, we shouldn’t generate it eagerly during initialization. Similarly, if we’re processing a sequence of items and might exit early based on the first few items, we shouldn’t process all items upfront.
    
- Bailing out early means checking cheap conditions before expensive ones and returning as soon as we have an answer. If we’re validating user input and the first validation check fails, we shouldn’t proceed with expensive downstream processing. This simple principle can eliminate huge amounts of unnecessary work.
    
- Finally, there’s the choice between general and specialized code. General-purpose libraries handle all possible cases, which often makes them slower than code written for one specific case. If we’re in a performance-critical section and using a heavyweight general solution, we should consider whether a lightweight specialized implementation would suffice.
    