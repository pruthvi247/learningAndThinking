[Source](https://www.youtube.com/watch?v=oBt53YbR9Kk)
**Problem

Write a funtion 'canSum' that takes in a targetsum and an array of numbers as arguments. The function should return a boolean indicating whether or not it is possible to generate the targetsum using numbers from the array. 
You may use an element of the array as many times as needed.You may assume that all input numbers are non negative

cansum(7,[5,3,4,7]) -> true
![[Pasted image 20230207112820.png]]  ![[Pasted image 20230207112913.png]]
![[Pasted image 20230207113231.png]] ![[Pasted image 20230207113320.png]]
From above image in the second level where `4` is present one branch is true and another is flase (-3 branch). In recursion when we are returning form `1` and `0` nodes , we need to return true if one of the branch is true. Shown in below image highlighted with circle

![[Screenshot 2023-02-07 at 11.50.56 AM.png]]
Negative scenario:
![[Pasted image 20230207115919.png]]

Python program - recursive way
```python
def canSum(targetSum,numbers):  
   if(targetSum ==0):  
      return True  
   if targetSum < 0:  
      return False  
   for num in numbers:  
      remainder = targetSum-num  
      if canSum(remainder,numbers)== True:  
         return True  
   return False
## So, if the input is like nums = [2, 3, 5] sum = 28,  
## then the output will be True as we can get 26 by using 5 + 5 + 5 + 5 + 3 + 3 + 2  
if __name__ == '__main__':  
   print(canSum(6,[5,4,1]))  
   print(canSum(8,[2,3,1]))
```
 **canSum - Memoization
![[Pasted image 20230207133941.png]]
![[Pasted image 20230207133819.png]]
![[Pasted image 20230207134115.png]]

**can sum - Memoization

```python
def canSum(targetSum,numbers,memo={}):  
   if (targetSum in memo):  
      return memo[targetSum]  
   if(targetSum ==0):  
      return True  
   if targetSum < 0:  
      return False  
   for num in numbers:  
      remainder = targetSum-num  
      if canSum(remainder,numbers)== True:  
         memo[remainder]= True  
         return True   memo[targetSum] = False  
   return Falseif __name__ == '__main__':  
   print(canSum(6,[5,4,1]))  
   print(canSum(300,[7,14]))
```
![[Pasted image 20230207183134.png]]
**can sum - Tabulation

Since we can come up with the size of the table, we are creating array of size of target sum and fill it with false value. But seed value as true.
ie. first value to True
O(m * n) = time
O(m) = space
![[Pasted image 20230207183924.png]]
![[Pasted image 20230207184002.png]]
![[Pasted image 20230207184029.png]]
![[Pasted image 20230207184051.png]]

**cansum - javascript - tabulation
![[Pasted image 20230207184739.png]]


