[source](https://www.youtube.com/watch?v=oBt53YbR9Kk)

**Problem:**
Say that you are traveller on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.
In  how many ways can you travel to the goal on a grid with dimentsions m * n
![[Pasted image 20230206171634.png]]
![[Pasted image 20230206171948.png]] ![[Pasted image 20230206172032.png]]
![[Pasted image 20230206172102.png]]
![[Pasted image 20230206173729.png]]

Python program - recursive way
```python
# Python program to count all possible paths
# from top left to bottom right

# function to return count of possible paths
# to reach cell at row number m and column
# number n from the topmost leftmost
# cell (cell at 1, 1)
def numberOfPaths(m, n):
	# If either given row number is first
	# or given column number is first
	if(m == 1 or n == 1):
		return 1
# If diagonal movements are allowed
# then the last addition
# is required.
	return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)
# Driver program to test above function
if __name__ == '__main__':
m = 3
n = 3
print(numberOfPaths(m, n))
```
Time complexity: O(2^n+m) -> 2 because n and m are two different set
Space complexity: O(n+m)
![[Pasted image 20230206223632.png]]
From below image (1,2) is duplicate, we can optimize it
![[Pasted image 20230206223848.png]]
Python program - Memoization
```python  
def numberOfPaths(m, n,memo):  
   key = str(m)+','+str(n)  
   if(key in memo):  
      return memo[key]  
   if (m == 0 or n == 0):  
      return 0  
   if(m == 1 or n == 1):  
      return 1  
  
   memo[key] = numberOfPaths(m-1, n,memo) + numberOfPaths(m, n-1,memo)  
   return memo[key]  
  
memo={}  
if __name__ == '__main__':  
   m = 18  
   n = 18  
   print(numberOfPaths(m, n,memo))
```

Time complexity : O(m * n)
Space complexity : O(n+m)

**Gridtraveller - Tabulation
![[Pasted image 20230207000624.png]]
![[Pasted image 20230207000724.png]] ![[Pasted image 20230207000746.png]]
![[Pasted image 20230207000759.png]]  ![[Pasted image 20230207000812.png]]
![[Pasted image 20230207000828.png]]  ![[Pasted image 20230207000904.png]]
![[Pasted image 20230207000943.png]]

`**** Tabulation Recipe ****`

1. Visualize the problem as a table
2. Size the table based on the inputs
3. Initialize the table with some values
4. Seed the trivial answer into the table
5. Iterate through the table
6. Fill further positions based on the current position

*Java script program for grid traveller - tabulation*

![[Screenshot 2023-02-07 at 12.58.14 AM.png]]

