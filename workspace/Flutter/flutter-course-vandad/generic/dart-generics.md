[source : https://vandad.sh/dart-generics/]

- Generics are a way for a programming language such as Dart to **not** directly specify the data-type of a value in a class, or a mixin, extension, type-alias or a function. They usually are written as letters such as E or T or G but can also be written as full words such as Element or Type or Value or Key.


## Constrained Generic Functions
A function can be made generic when its inputs and/or the result do not necessarily have to be tied to an exact data-type. Let’s say that you are tasked with writing a function that has no parameters, and it returns either an `int` or a `double` depending on what the caller expects it to do. How could you write such a function? Let’s see a very naive implementation of such a function:
```dart
// this is just for the purpose of demonstration
// ideally you should never write a function
// like this in your code
num eitherIntOrDouble(bool isInt) {
  // detect if the requested value is an int
  if (isInt) {
    // if yes, return 1
    return 1;
  } else {
    // if no, assume it's a double
    // and return 1.1
    return 1.1;
  }
}
```

At the call-site then when you call this function, you have to pass a parameter to it stating whether you want an `int` or not, and if you pass `false` to the `isInt` parameter, you will get a `double`. But note that the data-type of the returned value of this function is `num` and cannot be both a `double` and an `int` at the same time, hence we are using a super data-type that wraps both `int` and `double`:

```dart
// take the result and manually convert 
// it to an `int` and print it out to console
final age = eitherIntOrDouble(true) as int;
age.log(); // prints 1
// do the same thing but this type convert
// the result to a `double` and print it out
final height = eitherIntOrDouble(false) as double;
height.log(); // prints 1.1
```
As you can see both the function implementation and the call-site look quite strange in that you have to make decisions on the type of value to return based on a parameter (and if you remember we were supposed to not have any parameters to the function at all). But if you ignore that fact for a while and try to clean up this code, you _could_ go ahead and change the input parameter

Let’s introduce a generic type to our function and re-write the code:
```dart
// a function that returns either an `int`
// or a `double` depending on the data-type
// that the caller expects from this
// function. This function's return value
// should conform to the `num` class which only
// `int` and `double` are allowed to conform to
E eitherIntOrDouble<E extends num>() {
  switch (E) {
    case int:
      return 1 as E;
    case double:
      return 1.0 as E;
    default:
      // this happens when the call-site forgets
      // to specify the generic type argument
      return 0 as E;
  }
}
```
Pay close attention to the way the function is defined. It specifies not only a generic data-type called `E` (as in _element_), but it specifies that the generic type _has to be_ conformant to the `num` class, meaning that it can only be an `int` or a `double`. If you read the documentation for the `num` class in Dart, you can see this fact:

Inside the function itself, if you go back to our code, you can see that we are checking the data-type to return using a switch statement. How do you then call this function, well, you can call it in two ways. Either you specify the data-type for the function to return or you don’t. If you specify the data-type, you will get that data-type (`int` or `double`) back, but if you don’t, you will get a `num` back where our code just returns the value of 0 in the `default` case:
```dart
// the call-site specifies the expected return type
// by specifying a data-type for its variables
final int age = eitherIntOrDouble();
age.log(); // prints 1
// specify `double` and get a `double` back
final double height = eitherIntOrDouble();
height.log(); // prints 1.1
// in this case the call-site forgets to specify
// the generic type argument, so the compiler
// infers the type to be `num`
final forgetDataType = eitherIntOrDouble();
forgetDataType.log();
```
If you were to call this function and expect a data-type that is not a sub-type of `num`, you will get a run-time error (as opposed to a compile-time error), meaning that you app compiles fun but when it runs, it will crash and burn:
```dart
// 🚨 this causes a run-time error
// type 'int' is not a subtype of type 'Never' 
// in type cast
final String invalid = eitherIntOrDouble();
invalid.log();
```
## Unconstrained Generic Functions

A constrained generic function as we saw earlier is a function that has a constraint on its generic type where the generic type has to be of a specific data-type. An unconstrained generic function is a function whose generic type is not constrained to any other type. Here is a very simple example:
```dart
// a function that takes in any value of any
// data-type and returns the same
// value with the same data-type
T iReturnWhatYouGiveMe<T>(T value) => value;

void testIt() {
  // integer is of type `int` here because
  // the value of `1` is an integer of type `int`
  final integer = iReturnWhatYouGiveMe(1);
  // float is of type `double` here because
  // the value of `1.0` is a floating point
  // value of type `double`
  final float = iReturnWhatYouGiveMe(1.1);
  // str is of type `String` here because
  // the value of `'hello'` is of type `String`
  final str = iReturnWhatYouGiveMe('hello');
}
```
Unconstrained generic functions are functions that do not put a constraint on their generic types. Remember that a function doesn’t necessarily have to be limited to 1 generic type. A function can have as many generic types as it requires and none of them have to be constrained!

Here is an example of a function that has two unconstrained generic parameters:
```dart
// a function that checks whether two values
// which are passed as parameters have the same
// datatype or not
bool doTypesMatch<T, E>(T value1, E value2) => T == E;

// we can then put the function to test
void testIt() {
  doTypesMatch(1, 2).log(); // true
  doTypesMatch(1, 2.2).log(); // false
  doTypesMatch('Hello', 1).log(); // false
}
```

## Constrained Generic Type-Aliases
Just like constrained generic functions which we saw examples of earlier, you can also create constrained generic type-alias. Let’s have a look at an example where we have a mixin and two classes that implement this mixin:
```dart
// a normal mixin that expects
// any type that implements it to
// have an `activate()` function
mixin CanBecomeActive {
  void activate();
}

// an immutable `Person` class that
// implements the `CanBecomeActive` mixin
@immutable
class Person with CanBecomeActive {
  const Person();
  @override
  void activate() {
    //empty for now
  }
}

// same as above but this time under a different
// name of `Animal
@immutable
class Animal with CanBecomeActive {
  const Animal();
  @override
  void activate() {
    //empty for now
  }
}
```
Now if you want to define a type-alias to a `Map` that contains keys that can be activated (read, conform to the `CanBecomeActive` mixin) you could write your code as shown here:
```dart
// a type-alias whose keys are constrained
// to have to conform to the `CanBecomeActive` mixin
typedef PersonsAndNames<C extends CanBecomeActive> = Map<C, String>;

void testIt() {
  const PersonsAndNames personsAndNames = {
    Person(): 'Vandad',
    Animal(): 'Kitty',
  };
  // {Instance of 'Person': Vandad, Instance of 'Animal': Kitty}
  personsAndNames.log();
}
```
This type-alias ensures that all keys of the underlying `Map` conform to the `CanBecomeActive` mixin, so both `Person` and `Animal` classes, or any other classes written in the future that conform to this mixin, will be able to get stored in the `Map`.

## Specializing Generic Type-Aliases

When using type-aliases in Dart, the compiler usually does a good job of determining the data-type of generic types. However, sometimes you might want to be more specific about the data-types. Let’s see an example:
```dart
// a generic type-alias that resolves to a
// Map<String, T> where T can only be a number
// that is derived from the `num` class: meaning
// that it can either be an integer or a double
typedef NamesAndHeights<T extends num> = Map<String, T>;

void testIt() {
  // This data-type is inferred to be Map<String, num>
  // eventhough the values passed to the map are
  // both of type `int`
  final NamesAndHeights namesAndHeights = {
    'Vandad': 180,
    'Joe': 170,
  };
}
```

you can go ahead and specialize your type-alias by specifying the generic data-types at call-site as shown here:
```dart
// we are specializing the generic constraint
// on `NamesAndHeights` to be specifically
// of type `int`
final NamesAndHeights<int> namesAndHeights = {
  'Vandad': 180,
  'Joe': 170,
};
```
```dart
final NamesAndHeights<int> namesAndHeights = {
  'Vandad': 180,
  'Joe': 170.2, // 🚨 compile-time error
  // a `double` value is not an `int`
};
```
## Generic Mixins

Just like generic functions and type-aliases, mixins in Dart can also be generic. A generic mixin is used in places where you cannot make an exact decision as to the data-type to be used for a variable or a function’s return type or parameter inside a mixin.

Let’s say that you have a mixin called `HasHeight` where the height is programmed to be of type `double`. You then go ahead and implement this mixin inside a `Person` class as shown here:

```dart
// a mixin that exposes a `height` property
mixin HasHeight {
  double get height;
}

// a class that mixes this mixin
@immutable
class Person with HasHeight {
  // we then define the height exactly
  // as specified by the mixin
  @override
  final double height;
  const Person(this.height);
}
```

What happens then if you want to create another class called `Dog` that also has a height but the height has to be of type `int`?
```dart
@immutable
class Dog with HasHeight {
  @override
  // 🚨 this code won't compile because
  // HasHeight expects the height variable
  // to be of type `double` but in our implementation
  // we need it to be an integer of type `int`
  final int height; // 🚨 compile-time error
  const Dog(this.height);
}
```
This code won’t compile since `HasAge` needs the height variable to be of type `double`. Wouldn’t it be better if this mixin left it to the class to decide whether the `height` variable is an integer or a double? That’s why you need generic mixins. Let’s change the implementation of `HasHeight` to become generic:
```dart
// a mixin that exposes a generic `height` property
mixin HasHeight<H extends num> {
  H get height;
}

// a class that mixes this mixin
// where the height is a `double`
@immutable
class Person with HasHeight {
  @override
  final double height;
  const Person(this.height);
}

// and in this class we mix the same mixin
// but instead have a `height` property that is an `int`
@immutable
class Dog with HasHeight {
  @override
  final int height;
  const Dog(this.height);
}
```
## Specializing Generic Mixins

You can also specialize generic functions that take in generic mixins as parameters. Let’s say that you have to write a function that takes in a parameter of type `HasHeight` but only operates on the parameter if it has a height of type `int`. You should then change your `Dog` implementation to ensure that its `height` property is indeed marked as `int` also in the class definition:
```dart
// ensure that your dog class specializes
// the `HasHeight` mixin and ensure that the
// height value is specified as a `int`
@immutable
class Dog with HasHeight<int> {
  @override
  final int height;
  const Dog(this.height);
}

void describe<H extends int>(HasHeight<H> hasHeight) {
  'The height is an int'.log();
}

void testIt() {
  // 🚨 compile-time error, Person
  // does not have a `height` property of
  // type `int`
  describe(const Person(180.0)); // 🚨 compile-time error
  describe(const Dog(40)); // prints: The height is an int
}
```
Sometimes you might need to fidget with the type-system a little bit in Dart to get things to work. For instance, in the example above, if you left out `Dog` to use `HasHeight` instead of specializing it as `HasHeight<int>`, the Dart compiler won’t understand that the implementation of `Dog` indeed is specializing the `height` property as `int`. In some other languages such as Rust, the compiler can infer these generics automatically, but in Dart, you might need to help the compiler sometimes.
## Generic Classes

All we’ve learnt about generics so far culminate into creating generic classes. A generic class is a class who has variables, or functions, or both, who are generic. A generic class usually is a container class since a non-generic class itself can contain generic functions. But if you are to declare generic variables on a class, then your class for sure has to be a generic class.

Let’s see an example of a non-generic class in Dart that has a generic function:
```dart
// a very simple example of a non-generic
// class that has a generic function
class Person {
  // a generic function that takes in another
  // function as a parameter, calls the 
  // function-parameter and returns its result
  T get<T>(T Function() getter) => getter();
}
```
When we talk about generic classes, we usually mean a class that has at least one generic data type. Let’s implement a simple `Tuple2` class that contains two values which can be returned from a function inside another class:
```dart
// a simple Tuple class that can contain
// 2 values, and each of the values can be
// of any data type
@immutable
class Tuple2<V1, V2> {
  final V1 first;
  final V2 second;
  const Tuple2(this.first, this.second);
}
```
Now that we have this generic class, we can use it inside another class whose implementation itself isn’t generic:
```dart
// a `Person` class that has a first and last name
// properties and can export those properties
// in form of a `Tuple2<String, String>`
class Person {
  final String firstName;
  final String lastName;
  const Person(this.firstName, this.lastName);

  // here we get our tuple of first and last name
  Tuple2<String, String> get fullName => Tuple2(firstName, lastName);
}
```
## Generic Extensions

After implementing our `Tuple2` class before, we can create generic extensions on our class. For instance, if we have a `Tuple<int, int>`, we can write an extension that can sum up the values and return the sum as a property:
```dart
// our extension only works on tuples whose
// both values are of type `int`
extension Tuple2Sum on Tuple2<int, int> {
  int get sum => first + second;
}

void testIt() {
  // the first two lines work
  const Tuple2(1, 2).sum.log(); // 3
  const Tuple2(10, 20).sum.log(); // 30
  // this line won't compile
  const Tuple2(1, 2.2).sum.log(); // 🚨 compile-time error
}
```
You might be asking yourself: but why can’t we let an integer be added to a double and return the double as the result? Well, there is no reason for not allowing that. All you have to do is to put a constrain on your generic extension and instead of extending `Tuple2<int, int>`, extend `Tuple2<T, T>` where `T` is a `num` as shown here:
```dart
// our extension works now on any combination of
// values as long as they extend `num`
extension Tuple2Sum<T extends num> on Tuple2<T, T> {
  T get sum => first + second as T;
}

void testIt() {
  // all 3 compile fine now
  const Tuple2(1, 2).sum.log(); // 3
  const Tuple2(10, 20).sum.log(); // 30
  const Tuple2(1, 2.2).sum.log(); // 3.2
}
```
