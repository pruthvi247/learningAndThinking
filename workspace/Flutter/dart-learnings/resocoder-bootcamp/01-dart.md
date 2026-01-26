# Data types
`dynamic` is a type underlying all Dart objects. You shouldn't need to explicitly use it in most cases.

`var` is a keyword, meaning "I don't care to notate what the type is here." Dart will replace the `var` keyword with the initializer type, or leave it `dynamic` by default if there is no initializer.

Use `var` if you expect a variable assignment to change during its lifetime:
```dart
var msg = "Hello world.";
msg = "Hello world again.";
```
Use `final` if you expect a variable assignment to remain the same during its lifetime:

Using `final` (liberally) will help you catch situations where you accidentally change the assignment of a variable when you didn't mean to.

Note that there is a fine distinction between `final` and `const` when it comes to objects. `final` does not necessarily make the object itself immutable, whereas `const` does:

```dart
/ can add/remove from this list, but cannot assign a new list to fruit.
final fruit = ["apple", "pear", "orange"];
fruit.add("grape");

// cannot mutate the list or assign a new list to cars.
final cars = const ["Honda", "Toyota", "Ford"];

// const requires a constant assignment, whereas final will accept both:
const names = const ["John", "Jane", "Jack"];
```
**dynamic:** _can change_ TYPE of the variable, & _can change_ VALUE of the variable later in code.

**var:** _can't change_ TYPE of the variable, but _can change_ VALUE of the variable later in code.

**final:** _can't change_ TYPE of the variable, & _can't change_ VALUE of the variable later in code.

```dart
dynamic v = 123;   // v is of type int.
v = 456;           // changing value of v from 123 to 456.
v = 'abc';         // changing type of v from int to String.

var v = 123;       // v is of type int.
v = 456;           // changing value of v from 123 to 456.
v = 'abc';         // ERROR: can't change type of v from int to String.

final v = 123;       // v is of type int.
v = 456;           // ERROR: can't change value of v from 123 to 456.
v = 'abc';         // ERROR: can't change type of v from int to String.
```

-----------------------------------------
## Immutability
[medium-blog](https://levelup.gitconnected.com/immutability-equality-in-flutter-dart-functional-programming-part-4-339a4e9312bb)
### final vs const

#### final
`final` variables are evaluated at runtime. If we don’t intend to change the value, it is recommended to use final instead of the var keyword or specify explicit types(int, String). The Dart analyzer is smart enough to infer the types.
#### const
On the other hand, `const` is a compile-time constant and is implicitly final. So the value must be known at compile-time and can not be reassigned.
`const` can not only be used with primitives but also with classes, lists, maps, and sets whose values do not change.
#### How to update immutable states?
Of course, how useful is an application that does not change and only shows static content? Not much, Right? So How do we update the state then? **_Instead of changing values, we replace them_**. We create a copy of the instance we need to access and use it. It prevents unexpected side effects.
We can use the `copyWith` method to make our life easier, but we need to implement it first.
```dart
void main(List<String> args) {
  final _user = User(name: 'John', age: '18');
  // ignore: avoid_print
  print(_user); //User(name: John, age: 18)
  final _newUser = _user.copyWith(name: 'Jane');
  // ignore: avoid_print
  print(_newUser); //User(name: Jane, age: 18)
}

class User {
  final String name;
  final String age;
  const User({required this.name, required this.age});
  User copyWith({String? name, String? age}) =>
      User(name: name ?? this.name, age: age ?? this.age);
  @override
  String toString() => 'User(name: $name, age: $age)';
}
```
`copwWith` creates a copy of the instance and only updates the values passed explicitly.

[*From another blog*](https://dart.academy/immutable-data-patterns-in-dart-and-flutter/)
=SOB=
### Using a metatag helper

You can use the `@immutable` metatag from the `meta` package to get helpful analyzer warnings on classes you intend to be immutable:
```dart
import 'package:meta/meta.dart';

@immutable
class Employee {
  int id;            // not final
  final String name;

  Employee(this.id, this.name);
}
```
The metatag does _not_ make your class immutable (if only it were that easy), but in this example, you will get a warning stating that one or more of your fields are not `final`. If you try to add the `const` keyword to your constructor while there are mutable properties, you'll get an error that tells you essentially the same thing. If a class has the `@immutable` tag on it, any subclasses that aren't immutable will also have warnings.

There are a few property types that introduce some complexity when it comes to immutability: objects and collections.
=EOB=

------------------------------------------------
#  Nullability examples

With null safety, none of the variables in the following code can be `null`:
```dart
// With null safety, none of these can ever be null.
var i = 42; // Inferred to be an int.
String name = getFileName();
final b = Foo();
```
To indicate that a variable might have the value `null`, just add `?` to its type declaration:

```
int? aNullableInt = null;
```
```dart
void main() {
  List<String> aListOfStrings = ['one', 'two', 'three'];
  List<String>? aNullableListOfStrings;
  List<String?> aListOfNullableStrings = ['one', null, 'three'];

  print('aListOfStrings is $aListOfStrings.');
  print('aNullableListOfStrings is $aNullableListOfStrings.');
  print('aListOfNullableStrings is $aListOfNullableStrings.');
}
```
##  The null assertion operator (!)

If you’re sure an expression with a nullable type doesn’t equal `null`, you can use the [null assertion operator](https://dart.dev/null-safety/understanding-null-safety#null-assertion-operator)(`!`) to make Dart treat it as non-nullable. By adding `!` after the expression, you assert two conditions to Dart about the expression:

1. Its value doesn’t equal `null`
2. Dart can assign the value to a non-nullable variable
> If the expression does equal `null`, **Dart throws an exception at run-time**. This makes the `!`operator _unsafe_. Don’t use it unless you have no doubt the expression can’t equal `null`

```dart
int? couldReturnNullButDoesnt() => -3;

void main() {
  int? couldBeNullButIsnt = 1;
  List<int?> listThatCouldHoldNulls = [2, null, 4];

  int a = couldBeNullButIsnt;
  int? b = listThatCouldHoldNulls.first; // first item in the list
  int c = couldReturnNullButDoesnt()!.abs(); // absolute value

  print('a is $a.');
  print('b is $b.');
  print('c is $c.');
}
```

##   Null-aware operators

If a variable or expression is nullable, you can use [type promotion](https://dart.dev/codelabs/null-safety#type-promotion) to access the type’s members. You can also use null-aware operators to handle nullable values.

Sometimes the flow of the program tells you that the value of an expression cannot be `null`. To force Dart to treat that expression as non-nullable, add the [null assertion operator](https://dart.dev/codelabs/null-safety#the-null-assertion-operator-) (`!`). If the value does equal `null`, using this operator throws an exception.

To handle potential `null` values, use the conditional property access operator (`?.`) or null-coalescing operators (`??`) to conditionally access a property or provide a default value if `null` respectively.

```dart
// The following calls the 'action' method only if nullableObject is not null
nullableObject?.action();
```
```dart
// Both of the following set nullableString to 'alternate' if it is null
nullableString ??= 'alternate';
nullableString = nullableString != null ?nullableString : 'alternate';
```

## Truncating division operator.

Performs truncating division of this number by `other`. Truncating division is division where a fractional result is converted to an integer by rounding towards zero.

If both operands are [int](https://api.flutter.dev/flutter/dart-core/int-class.html)s, then `other` must not be zero. Then `a ~/ b` corresponds to `a.`
```dart
int getLength(String? str) {
  // Try throwing an exception here if `str` is null.

  return str!.length;
}

void main() {
  print(getLength("ll"));
  print(22~/7); // prints:3
  print(22/7); // prints : 3.142857142857143
}
```

# Higher Order Functions
[  ](https://dev.to/t/dart)
**What Is Higher order function?**  
_In dart programming language can accept a function as an argument, this type of functions is called higher order functions._
The functions are first class citizens in dart programming language because, They can be assigned to a variable, passed as an argument to another function, returned from a function, stored in other Data collections, and created in any scope.
```dart
// this function called higher order function.
void higherOrderFunction(String Function() callbackFunction)
{

  // this function called callback function generally.
  callbackFunction();

 }
```
#good-dart-example
```dart
void main() {
  final twicePlusFive = twice((x)=> x+5);
  final result = twicePlusFive(3);
  print(result);
}
int Function(int) twice(int Function(int) fun){
  return (int x){
    return fun(fun(x));
  };
}

```

# Typedefs

A type alias—often called a _typedef_ because it’s declared with the keyword `typedef`—is a concise way to refer to a type. Here’s an example of declaring and using a type alias named `IntList`:
```dart
typedef IntList = List<int>;
IntList il = [1, 2, 3];
```
A type alias can have type parameters:
```dart
typedef ListMapper<X> = Map<X, List<X>>;
Map<String, List<String>> m1 = {}; // Verbose.
ListMapper<String> m2 = {}; // Same thing but shorter and clearer.
```

```dart
typedef Compare<T> = int Function(T a, T b);

int sort(int a, int b) => a - b;

void main() {
  assert(sort is Compare<int>); // True!
}
```
Dart recommend using [inline function types](https://dart.dev/effective-dart/design#prefer-inline-function-types-over-typedefs) instead of typedefs for functions, in most situations. However, function typedefs can still be useful:
```dart
class FilteredObservable {
  final bool Function(Event) _predicate;
  final List<void Function(Event)> _observers;

  FilteredObservable(this._predicate, this._observers);

  void Function(Event)? notify(Event event) {
    if (!_predicate(event)) return null;

    void Function(Event)? last;
    for (final observer in _observers) {
      observer(event);
      last = observer;
    }

    return last;
  }
}
```

## Spread Operator(...)

```dart
List<int> l1 = [1, 2, 3];
List<int> l2 = [4, 5];
List<int> result = [...l1, ...l2];
print(result);
```

```dart
List<int> nullList = null;
List<int> result = [...l1, ...nullList];
print(result);
```

You will get the following error:

```
  Unhandled exception:  NoSuchMethodError: The getter 'iterator' was called on null.
```

Fortunately, Dart also supports null-aware operator for `spread`. Just add `?` symbol after the triple dot.By using the null-aware operator, the value will be checked first and if it's `null`, it will be ignored.
```dart
List<int> l1 = <int>[1,2,3,4];
  List<int>? nullList = null;
  List<int>? listResult = [...l1, ...?nullList];
```
You can also use `if` condition to determine whether the `List` should be concatenated or not.
```dart

bool condition = false;
List<int> result = [...l1, if (condition) ...l2];
print(result);
```
# [enums in Flutter 3.0](https://tech-lead.medium.com/advanced-enums-in-flutter-a8f2e2702ffd)
 `Enum` is simply a special kind of class used to represent a fixed number of constant values.
 Here is an example of an `enum` class:
 `enum OperatingSystem { macOS, windows, linux }`
 _All enums automatically extend the Enum class. They are also sealed, meaning they cannot be subclassed, implemented, mixed in, or otherwise explicitly instantiated._
_Abstract classes and mixins can explicitly implement or extend Enum, but unless they are then implemented by or mixed into an enum declaration, no objects can actually implement the type of that class or mixin._
!!! Note: refer to blog on how `enum` worked before flutter 3.0
```dart

enum CarType {|
sedan,
suv,
truck
}
```
Enum cases in Dart language are zero based indexed. This means each case defined in the enum type can be accessed by their index-value depending the order of definition. In the above example Sedan = 0 , suv = 1 , truck = 2

```dart
// enhanced enum is more like a constant class
enum CarType {
  none(""),
  suv("ABC-1"),
  sedan("CDE-2");

  // can add more properties or getters/methods if needed
  final String value;

  // can use named parameters if you want
  const CarType(this.value);
}
```
Please not that if your enum has a value type other than String, you can replace `_final String value`_ to `_final [your type] value`_

Using enums in a Dart language is also easy. In the example below CarHireCompany class contains storage type that is an enum of CarType which represents the type of car available for hire:
```dart
class CarHireCompany {
  late CarType storageType;

  CarHireCompany({required this.storageType});

  CarHireCompany.fromID(String key) {
    // Get enum from index
    storageType = CarType.values.firstWhere((element) => element.value == key);
  }

  bool canLend(CarType type) {
    if (type == storageType) {
      return true;
    }
    return false;
  }

  int get storageTypeIndex {
    return storageType.index;
  }
}
```
`print(CarType.sedan.value);`
### Stackoverflow
```dart
enum Fruit { apple, banana }

// Convert to string
String str = Fruit.banana.toString();

// Convert to enum
Fruit f = Fruit.values.firstWhere((e) => e.toString() == 'Fruit.' + str);

assert(f == Fruit.banana);  // it worked
```
**Dart 2.15**

```dart
enum Day { monday, tuesday }

main() {
  Day monday = Day.monday;
  print(monday.name); //prints 'monday'
}
```
**Dart 2.7 - 2.14**

With new feature called [Extension methods](https://dart.dev/guides/language/extension-methods) you can write your own methods for Enum as simple as that!

```dart
enum Day { monday, tuesday }

extension ParseToString on Day {
  String toShortString() {
    return this.toString().split('.').last;
  }
}

main() {
  Day monday = Day.monday;
  print(monday.toShortString()); //prints 'monday'
}
```

# Classes
## Constructors
Declare a constructor by creating a function with the same name as its class (plus, optionally, an additional identifier as described in [Named constructors](https://dart.dev/language/constructors#named-constructors)). The most common form of constructor, the generative constructor, creates a new instance of a class:
```dart
class Point {
  double x = 0;
  double y = 0;

  Point(double x, double y) {
    // See initializing formal parameters for a better way
    // to initialize instance variables.
    this.x = x;
    this.y = y;
  }
}
```
### Named constructor
```dart
const double xOrigin = 0;
const double yOrigin = 0;

class Point {
  final double x;
  final double y;

  Point(this.x, this.y);

  // Named constructor
  Point.origin()
      : x = xOrigin,
        y = yOrigin;
}
```
Remember that constructors are not inherited, which means that a superclass’s named constructor is not inherited by a subclass. If you want a subclass to be created with a named constructor defined in the superclass, you must implement that constructor in the subclass.
In the following example, the constructor for the Employee class calls the named constructor for its superclass, Person. Click **Run** to execute the code.
```dart
class Person {
  String? firstName;

  Person.fromJson(Map data) {
    print('in Person');
    firstName=data['firstName'];
    print(this.firstName);
    
  }
}

class Employee extends Person {
  // Person does not have a default constructor;
  // you must call super.fromJson().
  Employee.fromJson(super.data) : super.fromJson() {
    print('in Employee');
  }
}

void main() {
  var employee = Employee.fromJson({'firstName':'firstName is.........'});
  print(employee);
  // Prints:
  // in Person
  // in Employee
  // Instance of 'Employee'
}
```
The arguments to the superclass constructor are evaluated before invoking the constructor, an argument can be an expression such as a function call:
_**Warning:** Arguments to the superclass constructor don’t have access to `this`. For example, arguments can call static methods but not instance methods._
```dart
class Employee extends Person {
  Employee() : super.fromJson(fetchDefaultData());
  // ···
}
```
### Super parameters
```dart
class Vector2d {
  final double x;
  final double y;

  Vector2d(this.x, this.y);
}

class Vector3d extends Vector2d {
  final double z;

  // Forward the x and y parameters to the default super constructor like:
  // Vector3d(final double x, final double y, this.z) : super(x, y);
  Vector3d(super.x, super.y, this.z);
}
```

> Notice that`super(...)` must always be the last call in the initialiser.

==Super-initializer parameters cannot be positional if the super-constructor invocation already has positional arguments, but they can always be named== example below
```dart
class Super {
  final int x, y;
  Super(this.x, this.y);
}
class Sub extends Super {
  Sub(super.first): super(0);
  //  ^                   ^ super invocation positional argument
  //  ^ positional super parameter
}
```
Here `Sub` has both a positional super-parameter (`super.first`) and an explicit positional argument in the super-invocation (`super(0)`).

The rules for super-parameters do not allow (or cover) this case, 


`Below code is fine`
```dart
class Vector2d {
  final double x;
  final double y;

  Vector2d(this.x, this.y);
}

class Vector3d extends Vector2d {
  final double z;

  Vector3d(final double x, final double y, this.z) : super(x, y);
}
```

```dart
class Super {
  final int x, y;
  Super(this.x, this.y);
}

class Sub extends Super {
  Sub(super.y, super.x);
}

void main() {
  var s = Sub(1, 2);
  print('x=${s.x}, y=${s.y}');
}
```


-----------------------------------------------
[deconstructing dart](https://medium.com/flutter-community/deconstructing-dart-constructors-e3b553f583ef)

```dart
class Robot {
  double height;
  Robot(this.height);
}
```

Imagine that the `height` field is expressed in feet and we want clients to supply the height in meters. Dart also allows us to initialize fields with computations from static methods (as they don't depend on an _instance_ of the class):
```dart
class Robot {
  static mToFt(m) => m * 3.281;
  double height; // in ft
  Robot(height) : this.height = mToFt(height);
}
```
Sometimes we must call `super` constructors when initializing:
```dart
class Machine {
  String name;
  Machine(this.name);
}

class Robot extends Machine {
  static mToFt(m) => m * 3.281;
  double height;
  Robot(height, name) : this.height = mToFt(height), super(name);
}
// Notice that`super(...)` must always be the last call in the initializer.
```
And if we needed to add more complex guards (than types) against a malformed robot, we can use `assert`:
```dart
class Robot {
  final double height;
  Robot(height) : this.height = height, assert(height > 4.2);
}
```
### Accessors and Mutators
```dart
class Robot {
  double height;
  Robot(this.height);
}

main() {
  var r = Robot(5);
  print(r.height); // 5
}
```
To update height 
```dart
main() {
  var r = Robot(5);
  r.height = 6;
  print(r.height); // 6
}
```
Let’s prevent anyone from modifying the height by making the field **private**.
In Dart, there is no `private` keyword. Instead, we use a convention: field names starting with `_` are private (library-private, actually).
```dart
class Robot {
  double _height;
  Robot(this._height);
}
```
Getters are functions that take no arguments and conform to the [uniform access principle](https://en.wikipedia.org/wiki/Uniform_access_principle).

We can simplify our getter by using two shortcuts: single expression syntax (fat arrow) and implicit `this`:
```dart
class Robot {
  double _height;
  Robot(this._height);

  get height => _height
  set height(value) => _height = value;
}
```
is equivalent to:
```dart
class Robot {
  double height;
  Robot(this.height);
}
```
Keep in mind initializers only assign values to fields and it is therefore not possible to use a setter in an initializer:
```dart
class Robot {
  double _height;
  Robot(this.height); // ERROR: 'height' isn't a field in the enclosing class

  get height => _height;
  set height(value) => _height = value;
}
```
If a setter needs to be called, we’ll have to do that in a **constructor body**:
```dart
class Robot {
  double _height;

  Robot(h) {
    height = h;
  }

  get height => _height;
  set height(value) => _height = value;
}
```
We can do all sorts of things in constructor bodies, but we can’t return a value!
```dart
class Robot {
  double height;
  Robot(this.height) {
    return this; // ERROR: Constructors can't return values
  }
}
```
### Final fields

**Final** fields are fields that can only be assigned once.
```dart
final r = Robot(5);
r = Robot(7); /* ERROR */
```
```dart
class Robot {
  final double _height;
  Robot(this._height);

  get height => _height;
  set height(value) => _height = value; // ERROR final field can only be assigned once
}
```
The following won’t work either, because `height`, being `final`, **must** be initialized. And initialization happens before the constructor body is run:
```dart
class Robot {
  final double height;

  Robot(double height) {
    this.height = height; // ERROR: The final variable 'height' must be initialized
  }
}
```
Solution:
```dart
class Robot {
  final double height;
  Robot(this.height);
}
```
### Default values

If _most_ robots are 5-feet tall then we can avoid specifying the height each time. We can make an argument **optional** and provide a **default value**:
```dart
class Robot {
  final double height;
  Robot([this.height = 5]);
}
main() {
  var r = Robot();
  print(r.height); // 5
  
  var r2d2 = Robot(3.576);
  print(r2d2.height); // 3.576
}
```
### Immutable

Our robots clearly have more attributes than a height. Let’s add some more!
```dart
class Robot {
  final double height;
  final double weight;
  final String name;

  Robot(this.height, this.weight, this.name);
}

main() {
  final r = Robot(5, 170, "Walter");
  r.name = "Steve"; // ERROR-As all fields are `final`, our robots are immutable! Once they are initialized, their attributes can't be changed.
}
```
As all fields are `final`, our robots are immutable! Once they are initialized, their attributes can't be changed.

Now let’s imagine that robots respond to many different names:
```dart
class Robot {
  final double height;
  final double weight;
  final List<String> names;

  Robot(this.height, this.weight, this.names);
}

main() {
  final r = Robot(5, 170, ["Walter"]);
  print(r.names..add("Steve")); // [Walter, Steve]
}
```
Dang, using a `List` made our robot mutable again!

We can solve this with a **const** constructor:

```dart
class Robot {
  final double height;
  final double weight;
  final List<String> names;

  const Robot(this.height, this.weight, this.names);
}

main() {
  final r = const Robot(5, 170, ["Walter"]);
  print(r.names..add("Steve")); // ERROR: Unsupported operation: add
}
```

`const` instances are canonicalized which means that equal instances point to the same object in memory space when running.And yes, using `const` constructors can improve performance in Flutter applications.

### Optional arguments always last!

If we wanted the `weight` argument to be **optional** we'd have to declare it at the end:
```dart
class Robot {
  final double height;
  final double weight;
  final List<String> names;

  const Robot(this.height, this.names, [this.weight = 170]);
}

main() {
  final r = Robot(5, ["Walter"]);
  print(r.weight); // 170
}
```
#### Naming things

Having to construct a robot like `Robot(5, ["Walter"])` is not very explicit.

Dart has named arguments! Naturally, they can be provided in any order and are all optional by default:
```dart
class Robot {
  final double height;
  final double weight;
  final List<String> names;

 Robot({ this.height, @required this.weight, this.names}); // (or use `assert(weight != null)` in the initializer!)
}

main() {
  final r = Robot(height: 5, names: ["Walter"]);
  print(r.height); // 5
}
```

How about making the attributes private?
```dart
class Robot {
  final double _height;
  final double _weight;
  final List<String> _names;

  Robot({ this._height, this._weight, this._names }); // ERROR: Named optional parameters can't start with an underscore
}
```
It fails! Unlike with positional arguments, we need to specify the mappings in the initializer:
```dart
class Robot {
  final double _height;
  final double _weight;
  final List<String> _names;

  Robot({ height, weight, names }) : _height = height, _weight = weight, _names = names;
  
  get height => _height;
  get weight => _weight;
  get names => _names;
}

main() {
  print(Robot(height: 5).height); // 5
}
```
Need default values?
```dart
class Robot {
  final double _height;
  final double _weight;
  final List<String> _names;

  Robot({ height, weight, names }) : _height = height ?? 7, _weight = weight, _names = names;
  
  get height => _height;
  get weight => _weight;
  get names => _names;
}

main() {
  print(Robot().height); // 7
}
```
We simply employ the handy “if-null” operator `??`.

Or, for example, a static function that returns default values:
```dart
class Robot {
  final double _height;
  final double _weight;
  final List<String> _names;
  
  static _d(key) => { 'height': 5, 'weight': 100, 'names': <String>[] }[key];

  Robot({ height, weight, names }) :
    _height = height ?? _d('height'),
    _weight = weight ?? _d('weight'),
    _names = names ?? _d('names');
  
  @override
  toString() => 'height: $_height / weight: $_weight / names: $_names';
}

main() {
  print(Robot(height: 7)); // height: 7 / weight: 100 / names: []
}
```
### Mixing it up

Both positional and named argument styles can be used together:
```dart
class Robot {
  final double _height;
  final double _weight;
  final List<String> _names;

  Robot(height, { weight, names }) :
    _height = height,
    _weight = weight,
    _names = names;
  
  get height => _height;
  get weight => _weight;
}

main() {
  var r = Robot(7, weight: 120);
  print(r.height); // 7
  print(r.weight); // 120
}
```
## Named constructors

Not only can arguments be named. We can give names to any number of constructors:
```dart
class Robot {
  final double height;
  Robot(this.height);
  
  Robot.fromPlanet(String planet) : height = (planet == 'geonosis') ? 2 : 7;
  Robot.copy(Robot other) : this(other.height);
}

main() {
  print(Robot.copy(Robot(7)).height); // 7
  print(new Robot.fromPlanet('geonosis').height); // 2
  print(new Robot.fromPlanet('earth').height); // 7
}
```
What happened in `copy`? We used `this` to call the default constructor, effectively "redirecting" the instantiation.

( `new` is optional but I sometimes like to use it, since it clearly states the intent.)

Invoking named `super` constructors works as expected:
```dart
class Machine {
  String name;
  Machine();
  Machine.named(this.name);
}

class Robot extends Machine {
  final double height;
  Robot(this.height);

  Robot.named({ height, name }) : this.height = height, super.named(name);
}

main() {
  print(Robot.named(height: 7, name: "Walter").name); // Walter
}
```
Note that named constructors require an unnamed constructor to be defined!
### Keeping it private

But what if we didn’t want to expose a public constructor? Only `named`?

We can make a constructor private by prefixing it with an underscore:
```dart
class Machine {
  String name;
  Machine._();
  Machine.named(this.name);
}

class Robot extends Machine {
  final double height;
  Robot._(this.height, name) : super.named(name);
  
  Robot.named({ height, name }) : this._(height, name);
}

main() {
  print(Robot.named(height: 7, name: "Walter").name); // Walter
}
```

The named constructor is “redirecting” to the private default constructor (which in turn delegates part of the creation to its `Machine` ancestor).

Consumers of this API only see `Robot.named()` as a way to get robot instances.

We said constructors were not allowed to return. Guess what?
**Factory constructors** can!
## Factory constructors

```dart
class Robot {
  final double height;

  Robot._(this.height);

  factory Robot() {
    return Robot._(7);
  }
}
main() {
  print(Robot().height); // 7
}
```

Factory constructors are syntactic sugar for the “factory pattern”, usually implemented with `static` functions.

They appear like a constructor from the outside (useful for example to avoid breaking API contracts), but internally they can delegate instance creation invoking a “normal” constructor. This explains why factory constructors **do not** have initializers.

Since factory constructors can return other instances (so long as they satisfy the interface of the current class), we can do very useful things like:

- caching: conditionally returning existing objects (they might be expensive to create)
- subclasses: returning other instances such as subclasses
They work with both normal and named constructors!

Here’s our robot warehouse, that only supplies one robot per height:
```dart
class Robot {
  final double height;
  
  static final _cache = <double, Robot>{};

  Robot._(this.height);

  factory Robot(height) {
    return _cache[height] ??= Robot._(height);
  }
}

main() {
  final r1 = Robot(7);
  final r2 = Robot(7);
  final r3 = Robot(9);
  
  print(r1.height); // 7
  print(r2.height); // 7
  print(identical(r1, r2)); // true
  print(r3.height); // 9
  print(identical(r2, r3)); // false
}
```
Finally, to demonstrate how a factory would instantiate subclasses, let’s create different robot brands that calculate prices as a function of height:
```dart
abstract class Robot {
  factory Robot(String brand) {
    if (brand == 'fanuc') return Fanuc(2);
    if (brand == 'yaskawa') return Yaskawa(9);
    if (brand == 'abb') return ABB(7);
    throw "no brand found";
  }
  double get price;
}

class Fanuc implements Robot {
  final double height;
  Fanuc(this.height);
  double get price => height * 2922.21;
}

class Yaskawa implements Robot {
  final double height;
  Yaskawa(this.height);
  double get price => height * 1315 + 8992;
}

class ABB implements Robot {
  final double height;
  ABB(this.height);
  double get price => height * 2900 - 7000;
}

main() {
  try {
    print(Robot('fanuc').price); // 5844.42
    print(Robot('abb').price); // 13300
    print(Robot('flutter').price);
  } catch (err) {
    print(err); // no brand found
  }
}
```
# Singletons

Singletons are classes that only ever create one instance. We think of this as a specific case of caching!

Let’s implement the singleton pattern in Dart:
```dart
class Robot {
  static final Robot _instance = new Robot._(7);
  final double height;

  factory Robot() {
    return _instance;
  }

  Robot._(this.height);
}

main() {
  var r1 = Robot();
  var r2 = Robot();
  print(identical(r1, r2)); // true
  print(r1 == r2); // true
}
```

The factory constructor `Robot(height)` simply always returns the one and only instance that was created when loading the `Robot` class. (So in this case, I prefer not to use `new` before `Robot`.)

--------------------------------------------------
# Static Members
-----------------------------------------------------
[blog](https://www.kodeco.com/books/dart-apprentice-fundamentals/v1.0/chapters/10-static-members)

Putting `static` in front of a member variable or method causes the variable or method to belong to the _class_ rather than the _instance_.
```dart
class SomeClass {
  static int myProperty = 0;
  static void myMethod() {
    print('Hello, Dart!');
  }
}
```
```dart
final value = SomeClass.myProperty;
SomeClass.myMethod();
```
## Static Variables

Static variables are often used for constants and in the singleton pattern.
__Note__: Variables receive different names according to where they belong or are located. Because static variables belong to the class, they’re called **class variables**. Non-static member variables are called **instance variables** because they only have a value after an object is instantiated. Variables within a method are called **local variables**. And top-level variables outside of a class are called **global variables**.

You can define class constants by combining the `static` and `const` keywords. For example, add the following class to your project below `main`:
```dart
class TextStyle {
  static const _defaultFontSize = 17.0;

  TextStyle({this.fontSize = _defaultFontSize});
  final double fontSize;
}
```

## Private variables

Dart allows you to make variables private by adding an underscore (_) in front of their name.
```dart
“User({int id = 0, String name = 'anonymous'})
      : _id = id,
        _name = name;”
```
The initializer list is always executed before the body of the constructor, if the body exists. You don’t need a body for this constructor, but if you wanted to add one, it would look like this:
```dart
User({int id = 0, String name = 'anonymous'})
    : _id = id,
      _name = name {
  print('User name is $_name');
}
```
--------------------------------------------------
## Class properties
1. **Understanding Setters and Getters:**  
    Setters and getters are methods used to access and modify the values of class properties. They provide a level of abstraction, enabling developers to encapsulate internal data and control access to it. Setters are used to modify property values, while getters are used to retrieve property values.
```dart
class Person {  
String _name;  
String get name => _name;  
  
set name(String value) {  
if (value.isNotEmpty) {  
_name = value;  
}  
}  
}  
void main() {  
final Person person = Person();  
  
person.name = 'John'; // Invokes the setter  
print(person.name); // Invokes the getter - Output: John  
}
```
Favourite ways of using getters is getting a `Map` from an object.
```dart
void main() {
 Vehicle car = Vehicle(make:"Honda",model:"Civic",manufactureYear:2010,color:"red");
  print(car.map); // output - {make: Honda, model: Civic, manufactureYear: 2010, color: red}
 print(car.make); // output - Honda
 print(car.model); // output - Civic
 car.age = 2019;
 print(car.age); // output - 
}
class Vehicle {
  String make;
  String model;
  int manufactureYear;
  int vehicleAge;
  String color;
  Map<String,dynamic> get map {
    return {
      "make": make,
      "model": model,
      "manufactureYear":manufactureYear,
      "color": color,
    };
  }
  int get age {
    return DateTime.now().year - manufactureYear;
  }
  void set age(int currentYear) {
    vehicleAge = currentYear - manufactureYear;
  }
Vehicle({this.make,this.model,this.manufactureYear,this.color,});
}
```

## Copywith
```dart
//File: email_sign_in_model.dart

class EmailSignInModel {
  EmailSignInModel({
    this.email='',
    this.formType=EmailSignInFormType.signIn,
    this.isLoading=false,
    this.password='',
    this.submitted=false,
  });

  final String email;
  final String password;
  final EmailSignInFormType formType;
  final bool isLoading;
  final bool submitted;

  EmailSignInModel copyWith({
    String email,
    String password,
    EmailSignInFormType formType,
    bool isLoading,
    bool submitted,

  }) {
    return EmailSignInModel(
    email: email ?? this.email,
    password: password?? this.password,
    formType: formType?? this.formType,
    isLoading: isLoading?? this.isLoading,
    submitted: submitted?? this.submitted
   
    );
  }
}



//File: email_sign_in_bloc.dart

import 'dart:async';
import 'package:timetrackerapp/app/sign_in/email_sign_in_model.dart';

class EmailSignInBloc {
 final StreamController<EmailSignInModel> _modelController = StreamController<EmailSignInModel>();
 Stream<EmailSignInModel> get modelStream => _modelController.stream;
 EmailSignInModel _model = EmailSignInModel();

 void dispose() {
   _modelController.close();
 }

void updateWith({
  String email,
  String password,
  EmailSignInFormType formType,
  bool isLoading,
  bool submitted

}) {
  //update model
  _model = _model.copyWith(
    email:email,
    password: password,
    formType: formType,
    isLoading: isLoading,
    submitted: submitted


  );
  //add updated model _tomodelController
  _modelController.add(_model);
}

}
```

---------------------------------
[medium-blog](https://medium.com/pinch-nl/comparing-objects-in-dart-made-easy-with-equatable-d208e5eb9571)
# Equality
By default, Dart checks for referential equality. If we compare any two non-constant objects in dart with the same value, it evaluates to false. The default implementation of the `==` operator is to return true if both the objects are identical, in other words, if both the objects are the same.
```dart
class Person {
  String ssn;
  String name;

  Person(this.ssn, this.name);

  // Define that two persons are equal if their SSNs are equal
  bool operator ==(other) {
    return (other is Person && other.ssn == ssn);
  }
}

main() {
  var bob =  Person('111', 'Bob');
  var robert =  Person('111', 'Robert');

  print(bob == robert); // true

  print(identical(bob, robert)); // false, because these are two different instances
}
```
Use `identical(a, b)` to check if two variables reference the same instance. The [identical](https://api.dart.dev/be/175003/dart-core/identical.html) function is a top-level function found in `dart:core`.
It should be noted that the use of the `identical` function in dart has some caveats as mentioned by this github issue [comment](https://github.com/dart-lang/sdk/issues/563#issuecomment-108304500):

> The specification has been updated to treat identical between doubles like this:
> 
> The identical() function is the predefined dart function that returns true iff its two arguments are either:
> 
> - The same object.
> - Of type int and have the same numeric value.
> - Of type double, are not NaNs, and have the same numeric value.
> - `identical` can act a little unexpected when working with primitives like `int` or `String` . You hardly ever need to use `identical` but you should be aware.

```dart
// objects
final car1 = Car();
final car2 = Car();

// identical objects
print(identical(car1, car2)); // false
print(identical(car1, car1)); // true

// identical primitives
print(identical(1,1)); // true
print(identical(1, 3-2)); // true
print(identical('hello world','hello world')); // true

// equal objects
print(car1 == car2); // false
print(car1 == car1); // true

// equal primitives
print(1 == 1); // true
print(1 == 3-2); // true
print('hello world' == 'hello world'); // true
```
### Hashcode and ==

By default, each instance you create is unique. This explains the behavior in the example above.

When we want two instances to be considered _equal_, we must override `==` operator and `hashcode` on that class. When overriding, it’s important that the outcomes of both overrides are consistent.

When we want two objects to be considered _equal_ the `==` operator should return `true` and `hashcode` on both objects should be returning the same `int` .

```dart
void main() {
  final car1 = Car(Color.green,Make.jaguar,2019);
  final car2 = Car(Color.green,Make.jaguar,2019);
  final car3 = Car(Color.red,Make.tesla,2020);
  
  print(car1 == car2); // true
  print(car1 == car3); // false
}

enum Color { blue, green, red }
enum Make { audi, jaguar, tesla }

class Car {
  final Color color;
  final Make make;
  final int year;

  Car(this.color, this.make, this.year);

  @override
  bool operator ==(Object other) {
    if (other is! Car) return false;
    if (color != other.color) return false;
    if (make != other.make) return false;
    if (year != other.year) return false;
    return true;
  }

  @override
  int get hashCode {
    var result = 17;
    result = 37 * result + color.hashCode;
    result = 37 * result + make.hashCode;
    result = 37 * result + year.hashCode;
    return result;
  }
}
```
Now that we’ve implemented our own logic for `==` and `hashcode` , we decide which instances of `Car`s are equal. We do this by checking the three properties; `color`, `make` and `year`. We also calculate a new `hashcode` based on these properties.

As you can see in the example, `car1` and `car2` are instantiated with the same properties, so they are now considered _equal_.

`car3` is completely different, and is therefor _not_ _equal_ to `car1`.

How we implement the `==` and `hashcode` logic is completely up to us. We could leave out certain properties if we’d like. The important thing is that both `==` and `hashcode` behave similar. If `==` says the objects are equal, then `hashcode` of both objects should also return the same value.

As you might think after seeing the example above; “_damn, that’s a lot of work for something so simple_”. And you are right. In the example above it takes up most of the class for a simple class that only holds a little bit of data.
### Equatable

To help you gain the advantages of _object equality_ and prevent you from making application breaking mistakes, there is the [equatable](https://pub.dev/packages/equatable) package.

Equatable will do the necessary overrides for you. All you have to do is tell it which properties to take into account by implementing the `props` getter.

Let’s update our example so it uses `Equatable`.
```dart
import 'package:equatable/equatable.dart';

enum Color { blue, green, red }
enum Make { audi, jaguar, tesla }

class Car extends Equatable {
  final Color color;
  final Make make;
  final int year;

  Car(this.color, this.make, this.year);

  @override
  List<Object?> get props => [color, make, year];
}
```

---------------------------------------
# Inheritance
## **Inheritance by extending a class**
```dart
class Car {  
  void accelerate(){  
    print("simple acceleration");  
  }  
    
  void brakes(){  
    print("simple brakes");  
  }  
}class Toyota extends Car {  
  [@override](http://twitter.com/override)  
  void brakes(){  
    print("toyota disk brakes");  
  }  
}void main(){  
  Toyota toyota = new Toyota();  
  toyota.accelerate();  
  toyota.brakes();  
}//output  
simple acceleration   
toyota disk brakes
```
## **Inheritance using interface**
Dart don’t have a separate keyword for an interface, instead we can simply implement a class. Most of the rules are same as java.
When implementing an interface, either provide implementation for all methods or make your calls an abstract one.
```dart
/// This is an abstract class but we treat it as an "Interface" because we're going to use 
/// 'implements' on this type (rather than 'extends').
abstract class Example {
  void methodOne();
  void methodTwo() {}

  int get calculate;
}

/// This is a concrete class.
class AnotherExample implements Example {
  @override
  void methodOne() {
    print('hello1!');
  }

  @override
  void methodTwo() {
    print('hello 2!');
  }

  @override
  int get calculate => 1;
}
```

!!!Note: When using `implements`, you must override **every** method declared in the superclass. With `extends` you could instead override zero or more methods (so you’re not forced to redefine them all). You could also use a regular class as an interface:

#### @mustCallSuper guarantees super is invoked
`@mustCallSuper` doesn't constrain the declarations where it occurs, as far as I know, it's used to report issues with declarations that are overriding declarations with that metadata (so `@mustCallSuper` really means "overriding declarations must call _me_!").

So if you want superinvocations all the way through a sequence of mixins then the `@mustCallSuper` should probably be located in a superclass.
```dart
import 'package:meta/meta.dart';

abstract class Disposer {
  @mustCallSuper
  void dispose() {
    // No-op.
  }
}

mixin Mixin1 on Disposer {
  @override
  void dispose() {
    print('i am Mixin1');
    super.dispose(); // Now linted if missing.
  }
}

mixin Mixin2 on Disposer {
  @override
  void dispose() {
    print('i am Mixin2');
    super.dispose(); // Now linted if missing.
  }
}

class User extends Disposer with Mixin1, Mixin2 {
  @override
  void dispose() {
    print('i am User');
    super.dispose(); // Now linted if missing.
  }
}

void main() {
  User().dispose(); 
}
//// output
// i am User
// i am Mixin2
// i am Mixin1
```

# Factory constructor
## What is Factory Design Pattern?

**Definition:** _In a Factory pattern, we create objects without exposing the creation logic to the client and refer to newly created objects using a common interface._
```dart
class Dog{
 String name;
 Dog(this.name);
}
class Labrador extends Dog{
 Labrador(String name):super(name);
}
class Doberman extends Dog{
 Doberman(String name):super(name);
}
```
If we need to create the object of these subclasses with the following criteria,

1. Give **Doberman** instance, if the user wants a dog to guard
2. Give **Labrador** instance, otherwise.

How can we naively do that?
```dart
void main(){
     Dog dog;
     String name='tommy';
     bool isGuardian= false;
     if(isGuardian){
         dog = Doberman(name);
      }
     else{
         dog = Labrador(name);
      }
      //do whatever you want
}
```
This is fine in one place, what if you want this logic in multiple places? You have to repeatedly use the if-else statement. How can we simplify this? The answer is **factory constructor.**
```dart
class Dog{
 String name;
 Dog(this.name);
 
 factory Dog.createDog({required String name,bool gaurdDog=false}){
     if(gaurdDog){
       return Doberman(name);
     }
     else{
       return Labrador(name);
     }
  }
}
```
```dart
Dog myGaurdDog = Dog.createDog(name:’Rocky’,gaurdDog:true);
```
Use a factory in situations where you don't _necessarily_ want to return a _new_ instance of the class itself. Use cases:

- the constructor is expensive, so you want to return an existing instance - if possible - instead of creating a new one;
- you only ever want to create one instance of a class (the singleton pattern);
- you want to return a subclass instance instead of the class itself.


# Named Constructors

In other languages, it is possible to overload your constructor. This means that you can have different constructors with the same name but with a varying signature (or a different set of arguments).
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

# Factory Vs Named Constructor
## 1.Ac
cess to instance members

- A named Constructor has access to **_this_** _keyword so it can access any member variables and methods._
- Factory Constructor is static so it has no access to **this** keyword.

## 2. The Return Statement

- Named Constructor works like a normal constructor, it need not return an instance explicitly. (No need for return statement) have you ever seen a constructor with a return statement at the end?
- Factory Constructor should return an instance explicitly. See all the factory constructors, there’s always a return statement at the end.

## 3. Type of instance returned

- A named constructor can only generate the instance of the current class.
- A factory constructor can decide which instance to return on runtime, it can return either the instance of the current class or any of the instances of its descendants class.

## 4. New or Old instance

- This may be a trivial point, but the named constructor will always return a new instance.
- Factory constructor can return a new instance or a cached instance based on our implementation(more on this [here](https://imsaravananm.medium.com/factory-constructor-in-dart-part-2-7db2a5981ac3))


# Realtime use case for FactoryConstructor
[medium-blog](https://medium.com/nerd-for-tech/factory-constructor-in-dart-part-2-7db2a5981ac3)

## **caching of different Loggers**
if you don’t know what a logger does, it is used to print messages to the console for debugging purposes. We usually have a logger for each class to print their own debugging messages preceded with their class name(so that we can identify “which message belong to which class”)

Let’s say we have implemented our own simple Logger class
```dart
class Logger {
  final String name;
  Logger(this.name){
      print("New logger created with name ${this.name}");
  }
  void log(String msg){
      print("${this.name} : $msg");
  } 
}
```
This Logger class is very obvious, it has only one attribute **_name_** and only one method **_void log(String msg)_**. we will create an instance of the logger for each class by passing its class name as the parameter. But if you are creating the same instance every time(from scratch) for the same class, it’s not a good practice and also when the instance is very expensive it will cost a lot of computational time.

Example Scenario,
```dart
class A{  
late final Logger _logger;  
A(){  
_logger = Logger(‘A’);  
}  
}
```
In the main() method, let’s do create 5 instances of A,
```dart
main() {  
for(int i=1;i<=5;i++){  
print("Creating instance ${i}");  
A a = A();  
print(""); //newline  
}  
}
```
The output will be
```
Creating instance 1
New logger created with name A

Creating instance 2
New logger created with name A

Creating instance 3
New logger created with name A

Creating instance 4
New logger created with name A

Creating instance 5
New logger created with name A
```
Whenever you create an instance of A, a corresponding logger instance will also be created. Is there any way we can reuse the logger instance? Yes, we have, by caching we can achieve that.
## Logger class with caching enabled
```dart
class Logger {
  final String name;
  
  static final Map<String, Logger> _cache =
      <String, Logger>{};

  factory Logger(String name) {
    return _cache.putIfAbsent(
        name, () => Logger._internal(name));
  }
  //private constructor
  Logger._internal(this.name){
     print("New logger created with name ${this.name}");
  }
  void log(String msg) {
    print("${this.name} : $msg");
  }
}
```
**Note**: Factory constructors have no access to `this`. That’s why we have declared _cache as **static.**
If you look at this new logger class, I have made some noticeable changes.

1. Removed the public constructor and added a private constructor Logger._internal(), so that we can’t directly create an instance of the Logger class anymore.
2. Introduced a Map ‘**__cache_**’ that is used for storing the previously created instances with their class name as the key.
3. Added a factory constructor, that will decide whether to return a new instance or an already existing one.

If you run the main() method again, our output will be
```
Creating instance 1

New logger created with name A
Creating instance 2
Creating instance 3
Creating instance 4
Creating instance 5
```
## How does it work?

1. When you first create the instance of A, it will ask the factory constructor of Logger to give it an instance of Logger with the name ‘A’.
2. The factory constructor will look for a Logger instance with key ‘A’ in the _cache map. Since it is the first time, it can’t find any Logger with key ‘A’. So it creates a new instance of Logger with the name as ‘A’, stores it in the map with key as ‘A’, and returns the same.
3. For the subsequent calls, since the Logger with key ‘A’ is already existing in the cache, it will not create a new instance and return the cached instance.

This caching technique comes in very handy if the instance we need to create is very expensive(takes a lot of computational time).

# Generics
Generics are often required for type safety, but they have more benefits than just allowing your code to run:
```dart
class Foo<T extends SomeBaseClass> {
  // Implementation goes here...
  String toString() => "Instance of 'Foo<$T>'";
}

class Extender extends SomeBaseClass {...}
```
```
var someBaseClassFoo = Foo<SomeBaseClass>();
var extenderFoo = Foo<Extender>();
```

```dart
class MyClass {
  T myMethod<T>(T param) {
    prinz(param);
  }
}
```
```dart
/// usage
new MyClass().myMethod<List<String>>(['a', 'b', 'c']);
```
**Type safe collection**
```dart
CollectionType <dataType> identifier = CollectionType <dataType>();
// example
List<int> numbers = List<int>();
```
Generics class example
```dart
/A class for grocery product
class Product {
  final int id;
  final double price;
  final String title;
  Product(this.id, this.price, this.title);

  @override
  String toString() {
    return "Price of ${this.title} is \$${this.price}";
  }
}

//A class for product's inventory
class Inventory {
  final int amount;

  Inventory(this.amount);

  @override
  String toString() {
    return "Inventory amount: $amount";
  }
}

//Custom type variables- Single letter
class Store<P, I> {
  final HashMap<P, I> catalog = HashMap<P, I>();

  List<P> get products => catalog.keys.toList();

  void updateInventory(P product, I inventory) {
    catalog[product] = inventory;
  }

  void printProducts() {
    catalog.keys.forEach(
      (product) => print("Product: $product, " + catalog[product].toString()),
    );
  }
}

//Custom type variables- Descriptive
class MyStore<MyProduct, MyInventory> {
  final HashMap<MyProduct, MyInventory> catalog =
      HashMap<MyProduct, MyInventory>();

  List<MyProduct> get products => catalog.keys;

  void updateInventory(MyProduct product, MyInventory inventory) {
    catalog[product] = inventory;
  }

  void printProducts() {
    catalog.keys.forEach(
      (product) => print("Product: $product, " + catalog[product].toString()),
    );
  }
}

//Demonstrating single letter vs descriptive names for generics.
//Both variations have the same results.
void mainCustomParams() {
  Product milk = Product(1, 5.99, "Milk");
  Product bread = Product(2, 4.50, "Bread");

  //Using single letter names for Generics
  Store<Product, Inventory> store1 = Store<Product, Inventory>();
  store1.updateInventory(milk, Inventory(20));
  store1.updateInventory(bread, Inventory(15));
  store1.printProducts();

  //Using descriptive names for Generics
  MyStore<Product, Inventory> store2 = MyStore<Product, Inventory>();
  store2.updateInventory(milk, Inventory(20));
  store2.updateInventory(bread, Inventory(15));
  store2.printProducts();
```

# Freezed
[code-with-andrea-blog](https://codewithandrea.com/articles/parse-json-dart-codegen-freezed/?source=post_page-----c942e9aa2428--------------------------------)
Freezed is a **code-generation package** that helps you to create **data classes** in Dart
## Installation

First, you need to add the `freezed` package to your **dev_dependencies** and add `freezed_annotation` as a **dependency**. To generate code, we still need the `build_runner` package in the dev_dependencies. Also we want to use the package `jsonn_serializable` to handle json easier (toJson and fromJson).

 Here's what they do:

- `json_serializable`: provides the [Dart Build System](https://github.com/dart-lang/build) with some builders for handling JSON
- `json_annotation`: defines the annotations used by `json_serializable`
- `freezed`: a powerful code generator that can handle complex use-cases with a simple API
- `freezed_annotation`: defines the annotations used by `freezed`
- `build_runner`: this is a standalone build package that can generate Dart files for us
>You can generate the JSON parsing code with `json_serializable` alone (without `freezed`). However, `freezed` is more powerful and can handle complex use-cases with a simple API.

## [A sample JSON document](https://codewithandrea.com/articles/parse-json-dart-codegen-freezed/?source=post_page-----c942e9aa2428--------------------------------#a-sample-json-document)
```json
{
  "name": "Pizza da Mario",
  "cuisine": "Italian",
  "year_opened": 1990,
  "reviews": [
    {
      "score": 4.5,
      "review": "The pizza was amazing!"
    },
    {
      "score": 5.0,
      "review": "Very friendly staff, excellent service!"
    }
  ]
}
```
Since `Restaurant` **depends** on `Review`, let's start with the `Review` class:
```dart
// review.dart
// 1. import freezed_annotation
import 'package:freezed_annotation/freezed_annotation.dart';

// 2. add 'part' files
part 'review.freezed.dart';
part 'review.g.dart';

// 3. add @freezed annotation
@freezed
// 4. define a class with a mixin
class Review with _$Review {
  // 5. define a factory constructor
  factory Review({
    // 6. list all the arguments/properties
    required double score,
    String? review,
  // 7. assign it with the `_Review` class constructor
  }) = _Review;

  // 8. define another factory constructor to parse from json
  factory Review.fromJson(Map<String, dynamic> json) => _$ReviewFromJson(json);
}
```
Let's do the same for the `Restaurant` class:
```dart
// restaurant.dart
import 'package:freezed_annotation/freezed_annotation.dart';
// import any other models we depend on
import 'review.dart';

part 'restaurant.freezed.dart';
part 'restaurant.g.dart';

@freezed
class Restaurant with _$Restaurant {
  factory Restaurant({
    required String name,
    required String cuisine,
    // note: using a JsonKey to map our JSON key that uses
    // *snake_case* to our Dart variable that uses *camelCase*
    @JsonKey(name: 'year_opened') int? yearOpened,
    // note: using an empty list as a default value
    @Default([]) List<Review> reviews,
  }) = _Restaurant;

  factory Restaurant.fromJson(Map<String, dynamic> json) =>
      _$RestaurantFromJson(json);
}
```
Note how both the `Restaurant` and `Review` classes have a factory constructor listing all the arguments we need, _but we haven't declared the corresponding properties_.
### Running the code generator

To generate the missing code, we can run this on the console:
```dart
flutter pub run build_runner build --delete-conflicting-outputs
```
Above command will generate few files,And if we look in the project explorer, we can find some new files:
```
restaurant.dart
restaurant.freezed.dart
restaurant.g.dart
review.dart
review.freezed.dart
review.g.dart
```
The `.freezed.dart` files contain a lot of code. If you want to see all the generated code, you can check [this gist](https://gist.github.com/bizz84/07cb696d46e80627939d009e10ca37c9).

What's important is that for each model class, the code generator has added:

- all the stored properties that we need (and made them `final`)
- the `toString()` method
- the `==` operator
- the `hashCode` getter variable
- the `copyWith()` method
- the `toJson()` method
And if we ever need to modify any of the properties in our model classes, we just need to update their factory constructors:
```dart
@freezed
class Review with _$Review {
  factory Review({
    // update any properties as needed
    required double score,
    String? review,
  }) = _Review;

  factory Review.fromJson(Map<String, dynamic> json) => _$ReviewFromJson(json);
}
```
```dart
@freezed
class Restaurant with _$Restaurant {
  factory Restaurant({
    // update any properties as needed
    required String name,
    required String cuisine,
    @JsonKey(name: 'year_opened') int? yearOpened,
    @Default([]) List<Review> reviews,
  }) = _Restaurant;

  factory Restaurant.fromJson(Map<String, dynamic> json) =>
      _$RestaurantFromJson(json);
}
```
#TODO unions and sealed classes
Sealed classes: https://www.woolha.com/tutorials/dart-sealed-classes-examples


# Async programming

Asynchronous programming refers to a block of code that runs in parallel with other blocks of code. As a result, we can do several things at the same time.

**Async** means that this function is asynchronous and you might need to wait a bit to get its result.
**Await** literally means - wait here until this function is finished and you will get its return value.
**Future** is a type that ‘_comes from the future_’ and returns value from your asynchronous function. It can complete with success(.then) or with  
an error(._catchError_).
**.Then((value){…})** is a callback that’s called when future completes successfully(with a value).
Dart gives us two ways to implement asynchronous logic
- Stream
- Future
```dart
void main() {
  print('start fetching recipes');

  Future.delayed(Duration(seconds: 1), () {
    print('recipes fetched');
  }).then((_) {
    print('after fetching recipes');
  });

  String computation = 'a random computation';
  print(computation);
}
```
```dart
/// output
start fetching recipes
a random computation
recipes fetched
after fetching recipes
```
## Using `async-await`
```dart
void main() async {
  print('start fetching recipes');

  await Future.delayed(Duration(seconds: 1), () {
    print('recipes fetched');
  });

  print('after fetching recipes');

  String computation = 'a random computation';
  print(computation);
}
```
```dart
/// output
start fetching recipes
recipes fetched
after fetching recipes
a random computation
```

Example1:
```dart
void main() {
  Future.delayed(Duration(seconds: 1), () {
    print('inside delayed 1');
  }).then((_) async {
    print('inside then 1');

    await Future.delayed(Duration(seconds: 1), () {
      print('inside delayed 2');
    });

    print('inside then 2');
  });

  print('after delayed');
}
/// output
after delayed
inside delayed 1
inside then 1
inside delayed 2
inside then 2
```
--------------------------------------------------
=SOB=
[medium-blog](https://medium.com/dartlang/dart-asynchronous-programming-futures-96937f831137)
Future can be in one of 3 states:

1. **Uncompleted:** The gift box is closed_._
2. **Completed with a value:** The box is open, and your gift (data) is ready.
3. **Completed with an error:** The box is open, but something went wrong.
Here’s an example of using `catchError()` to handle the case where a future completes with an error:
```dart
void main() {
  Future.delayed(
    Duration(seconds: 3),
    () => throw 'Error!',
  ).then((value) {
    print(value);
  }).catchError((err) {
    print('Caught $err');
  }, test: (err) { // Optional test parameter.
    print('test $err');
    return err is String;
  });
  print('Waiting for a value...');
}
```
Above example, You can even give `catchError()` a test function to check the error before invoking the callback. You can have multiple `catchError()` functions this way, each one checking for a different kind of error. Here’s an example of specifying a test function, using the optional `test` parameter to `catchError()`

There’s one more method you might want to use: `[whenComplete()](https://api.dartlang.org/stable/dart-async/Future/whenComplete.html)`. You can use it to execute a function when the future is completed, no matter whether it’s with a value or an error.
### Future in Flutter
```dart
    return FutureBuilder<String>(
      future: _fetchNetworkData(5),
      builder: (context, snapshot) {
        if (snapshot.hasError) {
          // Future completed with an error.
          return Text(
            'There was an error',
          );
        } else if (snapshot.hasData) {
          // Future completed with a value.
          return Text(
            json.decode(snapshot.data)['field'],
          );
        } else {
          // Uncompleted.
          return Text(
            'No value yet!',
          );
        }
      },
    );
```
# Streams
![[Pasted image 20231023135038.png]]
If you’re using the `File` class’s`[openRead](https://api.dart.dev/stable/dart-io/File/openRead.html)()` method to read data from a file, for example, this method returns a stream.
## **Listening to streams**
Say you have a class that gives you a stream that emits a new integer once every second (1, 2, 3, 4, 5…). You can use the `[listen](https://api.dart.dev/stable/dart-async/Stream/listen.html)()`method to subscribe to the stream. The only required parameter is a function
```dart
final myStream = NumberCreator().stream;final subscription = myStream.listen(  
    (data) => print(‘Data: $data’),  
);
```
>**Important:** By default, streams are set up for single subscription. They hold onto their values until someone subscribes, and they only allow a single listener for their entire lifespan. If you try to listen to a stream twice, you’ll get an exception.
>Fortunately Dart also offers broadcast streams. You can use the `[asBroadcastStream()](https://api.dart.dev/stable/dart-async/Stream/asBroadcastStream.html)` method to make a broadcast stream from a single subscription one. Broadcast streams work the same as single subscription streams, but they can have multiple listeners.
>**Another difference of broadcast streams:** if nobody’s listening when a piece of data is ready, that data is tossed out.

As mentioned earlier, streams can produce errors just like futures can. By adding an [onError](https://api.dart.dev/stable/2.16.2/dart-async/StreamSubscription/onError.html) function to the `listen()` call, you can catch and process any errors.

There’s also a `cancelOnError` property that’s true by default, but can be set to false to keep the subscription going even after an error.

You can add the [onDone](https://api.dart.dev/stable/2.16.2/dart-async/StreamSubscription/onDone.html) function to execute some code when the stream is finished sending data, such as when a file has been completely read.

With all four of those parameters combined — `onError`, `onDone`, `cancelOnError`, and the required parameter ([onData](https://api.dart.dev/stable/2.16.2/dart-async/StreamSubscription/onData.html)) — you can be ready in advance for whatever happens.
```dart
final myStream = NumberCreator().stream;final subscription = myStream.listen(  
  (data){  
    print(‘Data: $data’);  
},  
onError: (err) {  
  print(‘Error!’);  
},  
cancelOnError: false,  
onDone: () {  
  print(‘Done!’):  
 },  
);
```
>**Tip:** The object that `listen()` returns has some useful methods of its own. It’s called a `StreamSubscription`, and you can use it to pause, resume, and even cancel the flow of data.

## **Using and manipulating streams**

Now that you know how to use `listen()` to subscribe to a stream and receive data events, let’s talk about what makes streams really cool: manipulating them.

Once you’ve got data in a stream, there are a lot of operations that suddenly become fluent and elegant.

Let’s go back to that number stream from earlier.

Using a method called `[map](https://api.dart.dev/stable/dart-async/Stream/map.html)()`_,_ you can take each value from the stream and convert it on the fly into something else. Give `map()` a function to do the conversion, and it returns a new stream, typed to match the return value of the function.

Instead of a stream of integers, now there is a stream of strings. Throw a `listen()`call on the end, pass it the `[print](https://api.dart.dev/stable/2.16.2/dart-async/Zone/print.html)()`function, and now it prints strings directly off the stream — asynchronously, as they arrive.
```dart
NumberCreator().stream  
    .map((i) => ‘String $i’)  
    .listen(print) ;String 1  
String 2  
String 3  
String 4  
*/
```
There are many methods you can chain up like this. If you only want to print the even numbers, for example, you can use `where()` to filter the stream. Give it a test function that returns a boolean for each element, and it returns a new stream that only includes values that pass the test.
```dart
NumberCreator().stream  
    .where((i) => i % 2 == 0)  
    .map((i) => ‘String $i’)  
    .listen(print) ;String 2  
String 4  
String 6  
String 8
```
The [distinct](https://api.dart.dev/stable/dart-async/Stream/distinct.html)() method is another good one. With an app that uses a Redux store, that store emits new app state objects in an [onChange](https://api.dart.dev/stable/2.16.2/dart-html/Document/onChange.html) stream.

You can use `map()` to convert the stream of state objects to a stream of view models for one part of the app. Then you can use the `distinct()` method to get a stream that filters out consecutive identical values (in case the store kicks out a change that doesn’t affect the subset of data in the view model).

You can then listen and update the UI whenever you get a new view model.
```dart
myReduxStore.onChange  
.map((s) => MyViewModel(s))  
.distinct()  
.listen( /* update UI */ )
```
There are additional methods built into Dart that you can use to shape and modify your streams. Plus, when you’re ready for more advanced features, there’s the [async package](https://pub.dev/packages/async) maintained by the Dart team and available on [pub.dev](https://pub.dev/). It has classes that can merge two streams together, cache results, and perform other types of stream-based wizardry.
For even more stream magic, take a look at the [stream_transform package](https://pub.dev/packages/stream_transform).

## **Creating streams**

Finally, one more advanced topic that deserves a mention here is how to create streams of your own.

Just like with futures, most of the time you’re going to be working with streams created for you by network libraries, file libraries, state management, and so on, but you can make your own using a `[StreamController](https://api.dart.dev/stable/dart-async/StreamController-class.html)`.

Let’s go back to that `NumberCreator` example we’ve been using so far. Here’s the actual code for it:

A [StreamController](https://api.dart.dev/stable/2.16.2/dart-async/StreamController-class.html) creates a brand new stream from scratch and gives you access to both ends of it. There’s the stream end itself, where data arrives. (We’ve been using that one throughout this article.)
`Stream<int> get stream => _controller.stream;`

And there’s the sink end, which is where new data gets added to the stream:

`_controller.sink.add(_count);`

`NumberCreator` uses both of them. When the timer goes off, it adds the latest count to the controller’s sink, and then it exposes the controller’s stream with a public property so other objects can subscribe to it.
```dart
class NumberCreator {  
  NumberCreator() {  
    Timer.periodic(const Duration(seconds: 1), (timer) {  
      _controller.sink.add(_count);  
     _count += 1;  
   });  
 } final _controller = StreamController<int>();  
 var _count = 0;  
 Stream<int> get stream => _controller.stream;  
}
```
### **Building Flutter widgets using streams**
For streams, there’s a similar widget called [StreamBuilder](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html). Give it a stream like the one from number creator and a builder method, and it rebuilds its children whenever a new value is emitted by the stream.
```dart
StreamBuilder<String>(
  stream: NumberCreator().stream.map((i) => ‘String $i’),
  builder: (context, snapshot) {
    if (snapshot.connectionState == ConnectionState.waiting) {
      return const Text(‘No data yet.’);
    } else if (snapshot.connectionState == ConnectionState.done) {
      return const Text(‘Done!’);
    } else if (snapshot.hasError) {
      return const Text(‘Error!’);
    } else {
      return Text(snapshot.data ?? ‘’);
    } 
  },
);
```

=EOB=

--------------------------------------------------