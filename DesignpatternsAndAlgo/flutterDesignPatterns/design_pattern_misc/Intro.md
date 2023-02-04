
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

