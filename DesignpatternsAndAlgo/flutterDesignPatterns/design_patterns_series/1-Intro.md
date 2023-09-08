
#### **Structural vs Behavioral**


Q:  How did they segregate in to structural and behavioural patterns?

From Gof book

> "Structural patterns are concerned with how classes and objects are composed to form larger structures. "

some structural patterns:

-   Adapter
-   Decorator
-   Facade
-   Proxy
-   Flyweight

etc

> "Behavior patterns are concerted with algorithms and the assignment of responsibilities between objects. Behavioral patterns describe not just the patterns of objects or classes but also the patterns of communication between them."

Some behavior patterns:

-   Chain of Responsibility
-   Command
-   Iterator
-   Mediator
-   Observer
-   Strategy
-   Visitor

A **behavioral pattern** is used to abstract some kind of variation in behavior. One of the most common behavioral patterns is [Strategy](https://en.wikipedia.org/wiki/Strategy_pattern). A good example of the Strategy pattern in Java is the [`Collections.sort(List<T>, Comparator<? super T>)`](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#sort-java.util.List-java.util.Comparator-) method. The `Comparator` in this method is the Strategy used to determine how the list will be sorted. There is one `sort` method, but you are free to pass in any number of `Comparator` implementations that effectively control how the sort is performed. This is the essence of the Strategy pattern.

A **structural pattern** is used to bring together existing objects into some new kind of design. One of the most common structural patterns is [Adapter](https://en.wikipedia.org/wiki/Adapter_pattern). A good example of the Adapter pattern in Java is the [`Arrays.asList()`](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#asList-T...-) method. This method returns an object (the Adapter) that makes the array appear as if it implements the `List` interface, thus allowing you to pass the array to a method that expects an implementation of `List`.
> [Design patterns - java lang examples](https://stackoverflow.com/questions/1673841/examples-of-gof-design-patterns-in-javas-core-libraries)


Observer is behavioral pattern: Presents interface, allowing object to communicate without any concrete knowledge about each other. Also known as Publish-Subscribe pattern. Object to inform other object about its state, **without the knowledge which are these objects**.

Adapter is structural pattern: **Adapter converts the given class' interface into another class** requested by the client. Wrap an existing class with a new interface. Impedance match an old component to a new system. Allows classes to work together when this is impossible due to incompatible interfaces.

--------------------------------------------------------
## The 7 Most Important Software Design Patterns

[#External-source](https://learningdaily.dev/the-7-most-important-software-design-patterns-d60e546afb0e)
1.  **Singleton**
2.  **Factory Method**
3. **Builder**
4. **Adapter**
5. **Strategy**
6. **Observer**
8. **State**

**Observer**
This pattern is a one-to-many dependency between objects so that when one object changes state, all its dependents are notified. This is typically done by calling one of their methods.

**Strategy**
The strategy pattern allows grouping related algorithms under an abstraction, which allows switching out one algorithm or policy for another without modifying the client. Instead of directly implementing a single algorithm, the code receives runtime instructions specifying which of the group of algorithms to run.

**Factory Method**
A normal factory produces goods; a software factory produces objects. And not just that — it does so without specifying the exact class of the object to be created. To accomplish this, objects are created by calling a factory method instead of calling a constructor.

**Builder**
As the name implies, a builder pattern is used to build objects. Sometimes, the objects we create can be complex, made up of several sub-objects or require an elaborate construction process. The exercise of creating complex types can be simplified by using the builder pattern. A _composite_ or an _aggregate_ object is what a builder generally builds.

**Adapter**
This allows incompatible classes to work together by converting the interface of one class into another. Think of it as a sort of translator: when two heads of states who don’t speak a common language meet, usually an interpreter sits between the two and translates the conversation, thus enabling communication.

**State**
The state pattern encapsulates the various states a machine can be in, and allows an object to alter its behavior when its internal state changes. The machine or the **_context_**, as it is called in pattern-speak, can have actions taken on it that propel it into different states. Without the use of the pattern, the code becomes inflexible and littered with if-else conditionals.

------------------------------------------------

------------------
#External-source
![[Pasted image 20230204142208.png]]

[Adapter vs strategy](https://stackoverflow.com/questions/46023431/difference-between-strategy-pattern-and-adapter)
Adapter patterns basically allows classes to work together that on their own could not due to incompatible interfaces. Adapter converts the interface of one class into something that may be used by another class.

Similar to how if you travel abroad you need to carry a power adapter to be able to use the wall sockets.

Strategy pattern, on the other hand takes a group of algorithms, and makes them interchangeable (by extending from a common interface). So that whatever class that is going to use the strategy can easily interchange it with another strategy from the group.

In other words, Adapter does not add behaviour in any way, it just modifies the existing interface to allow some other class to access the existing functionality.

Strategy pattern on the other hand encapsulates different behaviour, and allows them to be switched at run time.

`Creational` : Deals with way of creating objects or families of objects
`Structural` : Deals with ways of managing complex objects hierarchies
`Behavioral` : Deals with ways of identifying and improving object messaging

