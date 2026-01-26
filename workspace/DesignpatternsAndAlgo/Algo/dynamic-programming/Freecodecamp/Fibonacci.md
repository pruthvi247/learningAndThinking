
[source](https://www.youtube.com/watch?v=oBt53YbR9Kk)
![[Pasted image 20230114143653.png]]
### Fib memoization vs Feb tabulation

**Fib Regular approach
```python
# Function for nth Fibonacci number  
def Fibonacci(n):  
  
   # Check if input is 0 then it will  
   # print incorrect input   if n < 0:  
      print("Incorrect input")  
  
   # Check if n is 0  
   # then it will return 0   elif n == 0:  
      return 0  
  
   # Check if n is 1,2  
   # it will return 1   elif n == 1 or n == 2:  
      return 1  
  
   else:  
      return Fibonacci(n-1) + Fibonacci(n-2)  
  
# Driver Program  
print(Fibonacci(9))
```

Above approach takes long time if n is large.  Time complexity O(2^n) 
![[Pasted image 20230206120103.png]]

 Space complexity is O(n), As the algo returns when it hits the base condition space will be cleared.


Fib Memoization
```python
def fib(n, memo):  
   if n == 0 or n == 1:  
      memo[n] = n  
      return n  
  
   if n not in memo:  
      memo[n] = fib(n-2, memo)+fib(n-1, memo)  
   return memo[n]  
mydict = {}  
n = 12  
res = fib(n, mydict)  
print('fib of', n,'=', res)
```
![[Pasted image 20230206164118.png]]  ![[Pasted image 20230206164234.png]]
O(n) Time complexity
O(n) Space complexity

**Fib Tabulation
![[Pasted image 20230206165040.png]]

![[Screenshot 2023-02-06 at 4.49.43 PM.png]]
![[Screenshot 2023-02-06 at 4.49.48 PM.png]]
![[Pasted image 20230206165324.png]]
```python
# Python program Tabulated (bottom up) version  
from urllib3.connectionpool import xrange  
  
def fib(n):  
   # array declaration  
   f = [0] * (n + 1)  
   # base case assignment  
   f[1] = 1  
   # calculating the fibonacci and storing the values  
   for i in xrange(2, n + 1):  
      f[i] = f[i - 1] + f[i - 2]  
   return f[n]  
  
def main():  
   n = 12  
   print("Fibonacci number is ", fib(n))  
  
if __name__ == "__main__":  
   main()
```

Time complexity : O(n)
Space complexity : O(n)

