### Influxdb Learnings

#### Pointers
- [Intro to influx](https://www.influxdata.com/resources/introduction-to-flux-and-functional-data-scripting/)
- [map and reduce influx db](https://www.youtube.com/watch?v=h6KYk17FBNk)



##### Intro to influx db:
![[Pasted image 20220304160535.png]]
``` 
r - represents row
```




###### output of above query:
![[Pasted image 20220304161009.png]]

###### Predicate funtions
![[Pasted image 20220304163721.png]]

```
In the above expression if we dont put brackets around r.host =="host1" or r.host== "host2"

when ever the funtion evaluates the row and if the row has ` host: "host2" `, it will not evaluate the next conditions and the row gets discarded,Hence we need to add brackets so the row get selected.

> Alternative to above command ` r.host =~ /host1|host2 `

```
##### Shaping data
###### Grouping
![[Pasted image 20220304164643.png]]

```We have window function also along with grouping ```


##### Transforming data
###### Map
![[Pasted image 20220304165402.png]]

``` 
In the above example in the ouput "_time" field is missing, to over come that we can use with keyword in map funtion, Example is given below 
```
![[Pasted image 20220304170336.png]]

###### Complex query example
![[Pasted image 20220304170658.png]]

##### map and reduce influx db
![[Pasted image 20220304180732.png]]
```
=<- Means that get the tables from the tables after this expression
```
![[Pasted image 20220304181016.png]]
```
Map() and reduce() are row iterator, means if you input a table it will iterate on the each row one at a time
```
![[Pasted image 20220304181514.png]]

```
Above query is verbose, we can achieve the same funtionality using "custom transformation". Its like encapsulation of above funtion to custom function

|>toF()

```
![[Pasted image 20220304181838.png]]
###### Conditional logic
``` 
Replace a value in the row with another value 
```
![[Pasted image 20220304182028.png]]
![[Pasted image 20220304182200.png]]
![[Pasted image 20220304182226.png]]
*** Gothchas ***
```

- Map() does not add new columns to group keys
- Map() only operates on a single row at a time
- If your operation requires values from separate fields use pivot() or join() to align fields values in rows
```

##### Reduce():
```
reduce allows you create custom aggregate transformations
```
![[Pasted image 20220304183050.png]]
```
Accumulator: Accumulator record is ouput from previous row iteration
identity: initial state of accumulator
```
![[Pasted image 20220304183355.png]]
###### Calculating Avg:
```
Note: We can not use the "sum" funtion value when calculating "avg", That is why we have to recalculate the sum again when calculating avg

eg: avg : (r.value+ accumulator.sum)

- we can only use the value from previous iteration using accumulator, we can not use the same funtion value in same iteration
```
![[Pasted image 20220304184045.png]]
###### Renaming and dropping columns
![[Pasted image 20220304184511.png]]
###### Min Max and Mean
![[Pasted image 20220304184558.png]]

*** Gothchas ***
```
- reduce() does not support the with operator
- Columns not in the group key or explicitly mapped in the reduce operation are dropped
- Mathematical operands must be of the same data type
- reduce() is distructive and will only output a single row per table 
```

![[Screenshot 2022-03-22 at 7.28.05 PM.png]]

![[Screenshot 2022-03-23 at 7.58.55 PM.png]]

![[Screenshot 2022-03-23 at 11.03.54 AM.png]]

![[Screenshot 2022-03-23 at 10.43.12 AM.png]]

![[Screenshot 2022-03-23 at 10.37.00 AM.png]]

![[Screenshot 2022-03-23 at 10.31.13 AM.png]]

![[Screenshot 2022-03-23 at 10.20.30 AM.png]]

![[Screenshot 2022-03-23 at 10.16.36 AM.png]]

![[Screenshot 2022-03-23 at 10.03.53 AM.png]]

![[Screenshot 2022-03-23 at 10.03.07 AM.png]]

![[Screenshot 2022-03-22 at 7.28.05 PM 1.png]]

![[Screenshot 2022-03-22 at 6.55.03 PM.png]]

![[Screenshot 2022-03-22 at 6.52.52 PM.png]]