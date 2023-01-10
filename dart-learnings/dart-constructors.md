#### [Source](https://itnext.io/deep-dive-in-dart-constructors-51e4c006fb8f)

### Constructors in dart :
```dart
// Default Constructor  
// Does nothing specialclass User {  
  String name = 'ehe';  
  **User();**  
}///////////////////  
// Constructor with parameters  
// Gets parameters and assigns to them to their variables class User {  
  String name;  
  **User(this.name);**  
}///////////////////  
// Constructor with the initial method  
// Fires the codes immediatelyclass User {  
  String name;  
  User(this.name) **{  
    // do some magic  
  }**  
}/////////////////  
// Constructor with assertion  
// Asserts some rules to parametersclass User {  
  String name;  
  User(this.name) **: assert(name.length > 3);**  
}////////////////  
// Constructor with initializer  
// You can also initialize the values with customizations tho!class User {  
  static String uppercase(String e) => e.toUpperCase();  
  String name;  
  User(name) **: name = yell(name);** static String yell(String e) => e.toUpperCase();  
}/////////////////////  
// Constructor with super()  
// you can override the values it extends**abstract** class **Person {**  
  String id;  
  **Person(this.id);**  
}class User **extends Person {**  
  String name;  
  User(this.name,**String id**) **: super(id);**  
}/////////////////////  
// Constructor with this()  
// you can redirect the values as wellclass User {  
  String name;  
  int salary; **User(this.name, this.salary);** **User.worker(String name) : this(name, 10);  
  User.boss(String name) : this(name, 9999999);**  
}
```

#### Private Constructor — Class._() :

```dart
class Print {  
  static void log(String message) => print(message);  
}
Print.log('ehe');
// You want to write an util like this but there is a problem with that, because you can also create an instance which is something we don't want
Print(); // it's absolutely unnecassary in this case
// How to prevent that? Answer is private constructors!
class Print {  
  Print._(); // This one will prevent creating instance**  
  static void log(String message) => print(message);  
}
Print(); // This will give compile time error nowYour instance is safe now!

// Your instance is safe now! So basically you can prevent creating an instance!

```

#### Named Constructor — Class.named()

You can create different types of instances in one `class`

For example;

```dart
class User {  
  String name;  
  int salary;  
  **User.worker**(this.name) : **salary = 10**;  
  **User.boss**(this.name) : **salary = 99999999**;  
}
```

#### Private Named Constructor —Class. _named()

You can easily be laundering your instance!

```dart
class User {  
String name;  
int salary;  
**User.worker**(this.name) : **salary = 10**;  
**User.boss**(this.name) : **salary = 99999999**;  
**User._mafia**(this.name) : **salary = 9999999999999**;  
}
```

you can create singletons using a private constructor!
```dart
class User {  
**User._privateConstructor();**  
**static final User instance = User._privateConstructor();**  
}
```

#### Const Constructor — const Class()

You can make your class immutable using `const constructor!`

> A const constructor is an optimization! The compiler makes the object immutable, allocating the same portion of memory for all `Text('Hi!')` objects. — Frank Treacy

```dart
const user = User('ehe');
class User {  
  final String name;  
  const User(this.name);  
}
```

#### Factory Constructor — factory class Class()

We said constructors were not allowed to return. Guess what?

**Factory constructors** can!

Also what factory constructors can do?

You don't have to create a new instance at all! you can invoke another constructor or subclass and you can even return an instance from a cache!!

Lastly, Little caution for Factories!

You cannot invoke the superclass constructor (`super()`)

##### Simple Examples
```dart
class User {  
  final String name;  
  User(this.name); **factory User.fromJson**(Map<String, dynamic> json) {  
    **return** **User(json["name"]);**  
  }  
}// Singleton Example  
class User {  
  User._internal(); static final User _singleton = Singleton._internal();  
  
  **factory User() => _singleton;**  
}
```


#### Named vs Factory constructors: 

[reference](https://medium.com/nerd-for-tech/named-constructor-vs-factory-constructor-in-dart-ba28250b2747)
>Tip : We use factory constructor when we want to
>1.  Decide which instance to return on runtime([_see this article_](https://imsaravananm.medium.com/factory-constructor-in-dart-part-1-1bbdf0d0f7f0))
>2. Cache instances for reusing purposes.

##### Access to instance members

-   A named Constructor has access to **_this_** _keyword so it can access any member variables and methods._
-   Factory Constructor is static so it has no access to **this** keyword.

##### The Return Statement

-   Named Constructor works like a normal constructor, it need not return an instance explicitly. (No need for return statement) have you ever seen a constructor with a return statement at the end?
-   Factory Constructor should return an instance explicitly. See all the factory constructors, there’s always a return statement at the end.
##### New or Old instance

-   This may be a trivial point, but the named constructor will always return a new instance.
-   Factory constructor can return a new instance or a cached instance based on our implementation(more on this [here](https://imsaravananm.medium.com/factory-constructor-in-dart-part-2-7db2a5981ac3))

>Note : You cannot invoke the superclass constructor (`super()`)
