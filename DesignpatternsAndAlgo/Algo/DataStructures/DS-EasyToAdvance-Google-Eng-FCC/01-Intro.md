[source-code](https://github.com/williamfiset/Algorithms/blob/master/slides/datastructures/dynamicarray/Arrays.pdf)
[source](https://www.youtube.com/watch?v=RBSGKlAvoiM)
# Abstract Data Type
An abstract data type-ADT is an abstraction of a data structure which provides only the interface to which a data structure must adhere to 
The interface does not give any specific details about how something should be implemented or in what programming language
![[Pasted image 20241101034952.png]]

### Big-O Notation
Big-O Notation gives an upper bound of the complexity in the worst case, helping to quantify performance as the input size becomes arbitrarily large
![[Pasted image 20241101035807.png]]
![[Pasted image 20241101040130.png]]
![[Pasted image 20241101040511.png]]
Finding all subsets of a set - O(2<sup>n</sup>)
Finding all permutations of a string - O(n!)
Sorting using merge sort - O(nlog(n))
Iterating over all the cells in a matrix of size n by m - O(nm)

## Static and Dynamic Arrays

**Array**:
A static array is a fixed length container containing n elements `indexable` from the range [0,n-1]
__indexable__ : This means that each slot/index in the array can be referenced with a number

When and where is a static array used?
1) Storing and accessing sequential data
2) Temporarily storing objects
3) Used by IO routines as buffers
4) Lookup tables and inverse lookup tables
5) Can be used to return multiple values from a function
6) Used in dynamic programming to cache answers to subproblems
![[Pasted image 20241103214740.png]]
Dynamic arrays: Grows and shrinks size as needed

## Linked List Intro














































