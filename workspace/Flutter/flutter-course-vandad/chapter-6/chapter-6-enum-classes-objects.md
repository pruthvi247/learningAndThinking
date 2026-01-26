
## Enum-classes-objects
#### Enums
1. enum  Properties{
 			firstName,lastname,age
			}
  print(Properties.firstName) -> prints - Properties.firstName
 2. enum Animal {cat,dog,bunny}
		 test(Animal animal){
		 		Print("this method accepts a parameter of type Animal")
		 }
 
3. animalType == Animal.bunny
4. ``` dart
enum WEEK { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }
void main() {
  WEEK thursday = WEEK.THURSDAY;
  print(WEEK.MONDAY.toString()); //WEEK.MONDAY
  print(WEEK.MONDAY.index); // zero
  print(WEEK.MONDAY.runtimeType); // WEEK
} ```

Here is an example to convert Enum to String in Dart?

```dart
enum WEEK { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

void main() {
  WEEK thursday = WEEK.THURSDAY;

  print(thursday.name); // THURSDAY
  print(thursday.name.runtimeType); // String
}

```
(or)
```dart
WEEK thursday = WEEK.THURSDAY;
  String name = thursday.toString().split('.').last;
```
We can also loop over enums
```dart
enum Fruits{
  mango,
  apple,
  banana,
  grapes
}
void main(){

     for(Fruits name in Fruits.values)
    {
        print(name);
     }
}
```

#### Classes

1. this - key word represents current object
#### Abstract Class:
- Abstract class- a class that can't be instantiated.Abstract classes are useful for defining interfaces, often with some implementation.If you want your abstract class to appear to be instantiable define factory constructor.
#### Factory constructors:
	-  In other languages, it is possible to overload your constructor. This means that you can have different constructors with the same name, but with a varying signature (or different set of arguments).
##### Named constructors in Dart

In Dart, this is not possible, but there is a way around it. It is called **named constructors**. Giving your constructors different names allows your class to have many constructors and also to better represent their use cases outside of the class.
```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
   
   	Car.withoutABS(this.make, this.model, this.yearMade): hasABS = false;
}
```
- The constructor **withoutABS** initializes the instance variable hasABS to false, before the constructor body executes. This is known as an **initializer list** and you can initialize several variables, separated by a comma.

The most common use case for initializer lists is to initialize final fields declared by your class.
> Note: Anything that is placed on the right hand side of the colon (:) has no access to **this**.

##### Factory constructors in Dart

A factory constructor is a constructor that can be used when you don't necessarily want a constructor to create a new instance of your class.

This might be useful if you hold instances of your class in memory and don't want to create a new one each time (or if the operation of creating an instance is costly).

Another use case is if you have certain logic in your constructor to initialize a final field that cannot be done in the initializer list.
```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	factory Car.ford(String model, String yearMade, bool hasABS) {
    	return FordCar(model, yearMade, hasABS);
    }
}

class FordCar extends Car {
	FordCar(String model, String yearMade, bool hasABS): super("Ford", model, yearMade, hasABS);
 
}
```
When you want one constructor to call another constructor under the hood, it's referred to as **redirecting constructors**
```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
   
   	Car.withoutABS(this.make, this.model, this.yearMade): this(make, model, yearMade, false);
}
```
#### Custom operators:
```dart
class Person {

final String name;

const Person(this.name);

@override

bool operator ==(covariant Person other) => other.name == name;

@override

int get hashCode => name.hashCode;

}
```















