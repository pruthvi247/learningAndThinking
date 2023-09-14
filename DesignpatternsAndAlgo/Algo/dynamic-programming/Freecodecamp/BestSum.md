[Source](https://www.youtube.com/watch?v=oBt53YbR9Kk)
**Problem

Write a function `bestSum` that takes in a targetSum and an array of numbers as arguments.The function should return an array containing the shortest combination of numbers that add up to exactly the target sum. `If there is a tie for the shortest combination,you may return any one of the shortest`

![[Pasted image 20230207194520.png]]
![[Pasted image 20230207194729.png]]
>From above image we need to take shortest path

Best sum-javascript-Recursive
![[Pasted image 20230207195705.png]]
Javascript- memoization
![[Pasted image 20230207200016.png]]

**Dynamic programming**
canSum  -> can you do it ? yes/no (Decision)
howSum -> How willyou do it (Combination)
bestSum -> What is the best way to do it ? (Optimization problem)

**BestSum - Tabulation**
![[Pasted image 20230207200442.png]]
![[Pasted image 20230207200546.png]]
>From above image [5] is shorter path than [2,3]
![[Pasted image 20230207200718.png]]

**Javascript - Tabulation**
![[Pasted image 20230207201017.png]]



