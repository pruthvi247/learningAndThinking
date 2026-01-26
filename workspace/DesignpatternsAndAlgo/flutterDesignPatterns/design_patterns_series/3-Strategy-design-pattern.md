[source](https://kazlauskas.dev/flutter-design-patterns-5-strategy/)
[source](https://refactoring.guru/design-patterns/strategy)

**Strategy**, also known as policy, belongs to the category of **behavioural** design patterns. The intention of this design pattern is described in the [GoF book](https://en.wikipedia.org/wiki/Design_Patterns):

> _Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it._

The primary purpose of the Strategy design pattern is to encapsulate a family of algorithms (related algorithms) such that they could be callable through a common interface, hence being interchangeable based on the specific situation. Also, this pattern should be considered when you want to use different calculation logic within an object and/or be able to switch between different algorithms at run-time. A general rule of thumb - if you notice different behaviours lumped into a single class, or there are several conditional statements in the code for selecting a specific algorithm based on some kind of context or business rules (multiple if/else blocks, switch statements), this is a big indicator that you should use the Strategy design pattern and encapsulate the calculation logic in separate classes (strategies). This idea promotes the **Open-Closed Principle** (the letter **O** in [**SOLID**](https://en.wikipedia.org/wiki/SOLID) principles) since extending your code with new behaviour (algorithm) does not insist you change the logic inside a single class but allows creating a new strategy class instead - _software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification_.

- Sorting algorithms - each algorithm (e.g. bubble sort, quicksort, etc.) is extracted into a separate class, a common interface is defined which provides a method _sort()_;
- Payment strategies - you want to define different payment options in your code (mobile payment, bank transfer, cash, credit card, you name it) and use them based on the user's selection;
- Damage calculation in RPG game - there are several different types of attack in the game e.g. attacking with different moves, combos, spells, using weapons, etc. Several different algorithms could be defined for each attack type and the damage value could be calculated based on the context.

![[Pasted image 20230611193415.png]]
- _Strategy_ - declares an interface that is common to all supported algorithms. It also declares a method the _Context_ uses to execute a specific strategy;
- _ConcreteStrategies_ - implement different algorithms using the _Strategy_ interface which is used by the _Context_;
- _Context_ - maintains a reference to a _Strategy_ object, but is independent of how the algorithm is implemented;1. The context calls the execution method on the linked strategy object each time it needs to run the algorithm. The context doesn’t know what type of strategy it works with or how the algorithm is executed.
- _Client_ - creates a specific strategy object and passes it to the _Context_.


[Realworld example](https://refactoring.guru/design-patterns/strategy)

One day you decided to create a navigation app for casual travelers. The app was centered around a beautiful map which helped users quickly orient themselves in any city.

One of the most requested features for the app was automatic route planning. A user should be able to enter an address and see the fastest route to that destination displayed on the map.

The first version of the app could only build the routes over roads. People who traveled by car were bursting with joy. But apparently, not everybody likes to drive on their vacation. So with the next update, you added an option to build walking routes. Right after that, you added another option to let people use public transport in their routes.

However, that was only the beginning. Later you planned to add route building for cyclists. And even later, another option for building routes through all of a city’s tourist attractions.

**Solution**:
The Strategy pattern suggests that you take a class that does something specific in a lot of different ways and extract all of these algorithms into separate classes called _strategies_.

The original class, called _context_, must have a field for storing a reference to one of the strategies. The context delegates the work to a linked strategy object instead of executing it on its own.

The context isn’t responsible for selecting an appropriate algorithm for the job. Instead, the client passes the desired strategy to the context. In fact, the context doesn’t know much about strategies. It works with all strategies through the same generic interface, which only exposes a single method for triggering the algorithm encapsulated within the selected strategy.

This way the context becomes independent of concrete strategies, so you can add new algorithms or modify existing ones without changing the code of the context or other strategies.
![[Pasted image 20230611193812.png]]

In our navigation app, each routing algorithm can be extracted to its own class with a single `buildRoute` method. The method accepts an origin and destination and returns a collection of the route’s checkpoints.

Even though given the same arguments, each routing class might build a different route, the main navigator class doesn’t really care which algorithm is selected since its primary job is to render a set of checkpoints on the map. The class has a method for switching the active routing strategy, so its clients, such as the buttons in the user interface, can replace the currently selected routing behavior with another one.

####  Pseudocode
In this example, the context uses multiple **strategies** to execute various arithmetic operations.

```
// The strategy interface declares operations common to all
// supported versions of some algorithm. The context uses this
// interface to call the algorithm defined by the concrete
// strategies.
interface Strategy is
    method execute(a, b)

// Concrete strategies implement the algorithm while following
// the base strategy interface. The interface makes them
// interchangeable in the context.
class ConcreteStrategyAdd implements Strategy is
    method execute(a, b) is
        return a + b

class ConcreteStrategySubtract implements Strategy is
    method execute(a, b) is
        return a - b

class ConcreteStrategyMultiply implements Strategy is
    method execute(a, b) is
        return a * b

// The context defines the interface of interest to clients.
class Context is
    // The context maintains a reference to one of the strategy
    // objects. The context doesn't know the concrete class of a
    // strategy. It should work with all strategies via the
    // strategy interface.
    private strategy: Strategy

    // Usually the context accepts a strategy through the
    // constructor, and also provides a setter so that the
    // strategy can be switched at runtime.
    method setStrategy(Strategy strategy) is
        this.strategy = strategy

    // The context delegates some work to the strategy object
    // instead of implementing multiple versions of the
    // algorithm on its own.
    method executeStrategy(int a, int b) is
        return strategy.execute(a, b)

// The client code picks a concrete strategy and passes it to
// the context. The client should be aware of the differences
// between strategies in order to make the right choice.
class ExampleApplication is
    method main() is
        Create context object.

        Read first number.
        Read last number.
        Read the desired action from user input.

        if (action == addition) then
            context.setStrategy(new ConcreteStrategyAdd())

        if (action == subtraction) then
            context.setStrategy(new ConcreteStrategySubtract())

        if (action == multiplication) then
            context.setStrategy(new ConcreteStrategyMultiply())

        result = context.executeStrategy(First number, Second number)

        Print result.
```
## Applicability

 Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to switch from one algorithm to another during runtime.

 The Strategy pattern lets you indirectly alter the object’s behavior at runtime by associating it with different sub-objects which can perform specific sub-tasks in different ways.

 Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.

 The Strategy pattern lets you extract the varying behavior into a separate class hierarchy and combine the original classes into one, thereby reducing duplicate code.

 Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.

 The Strategy pattern lets you isolate the code, internal data, and dependencies of various algorithms from the rest of the code. Various clients get a simple interface to execute the algorithms and switch them at runtime.

 Use the pattern when your class has a massive conditional statement that switches between different variants of the same algorithm.

 The Strategy pattern lets you do away with such a conditional by extracting all algorithms into separate classes, all of which implement the same interface. The original object delegates execution to one of these objects, instead of implementing all variants of the algorithm.

##  How to Implement

1. In the context class, identify an algorithm that’s prone to frequent changes. It may also be a massive conditional that selects and executes a variant of the same algorithm at runtime.
    
2. Declare the strategy interface common to all variants of the algorithm.
    
3. One by one, extract all algorithms into their own classes. They should all implement the strategy interface.
    
4. In the context class, add a field for storing a reference to a strategy object. Provide a setter for replacing values of that field. The context should work with the strategy object only via the strategy interface. The context may define an interface which lets the strategy access its data.
    
5. Clients of the context must associate it with a suitable strategy that matches the way they expect the context to perform its primary job.

## Relations with Other Patterns

- [Bridge](https://refactoring.guru/design-patterns/bridge), [State](https://refactoring.guru/design-patterns/state), [Strategy](https://refactoring.guru/design-patterns/strategy) (and to some degree [Adapter](https://refactoring.guru/design-patterns/adapter)) have very similar structures. Indeed, all of these patterns are based on composition, which is delegating work to other objects. However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way. It can also communicate to other developers the problem the pattern solves.
    
- [Command](https://refactoring.guru/design-patterns/command) and [Strategy](https://refactoring.guru/design-patterns/strategy) may look similar because you can use both to parameterize an object with some action. However, they have very different intents.
    
    - You can use _Command_ to convert any operation into an object. The operation’s parameters become fields of that object. The conversion lets you defer execution of the operation, queue it, store the history of commands, send commands to remote services, etc.
        
    - On the other hand, _Strategy_ usually describes different ways of doing the same thing, letting you swap these algorithms within a single context class.
        
- [Decorator](https://refactoring.guru/design-patterns/decorator) lets you change the skin of an object, while [Strategy](https://refactoring.guru/design-patterns/strategy) lets you change the guts.
    
- [Template Method](https://refactoring.guru/design-patterns/template-method) is based on inheritance: it lets you alter parts of an algorithm by extending those parts in subclasses. [Strategy](https://refactoring.guru/design-patterns/strategy) is based on composition: you can alter parts of the object’s behavior by supplying it with different strategies that correspond to that behavior. _Template Method_ works at the class level, so it’s static. _Strategy_ works on the object level, letting you switch behaviors at runtime.
    
- [State](https://refactoring.guru/design-patterns/state) can be considered as an extension of [Strategy](https://refactoring.guru/design-patterns/strategy). Both patterns are based on composition: they change the behavior of the context by delegating some work to helper objects. _Strategy_ makes these objects completely independent and unaware of each other. However, _State_ doesn’t restrict dependencies between concrete states, letting them alter the state of the context at will.
## **Strategy** in Flutter
[source](https://kazlauskas.dev/flutter-design-patterns-5-strategy/)
### Usecase :
The following example and the problem we want to resolve could look similar to some of you, which are using Flutter to build an e-commerce mobile application. Let's say that your e-shop business offers several different shipping types for your customers:

- Picking up the ordered items from a physical store (or any other physical place, e.g. a warehouse);
- Sending order items using parcel terminal services;
- Sending order items directly to your customers in the shortest delivery time possible - priority shipping.

These three types contain different shipping costs calculation logic which should be determined at run-time, e.g. when the customer selects a specific shipping option in UI. At first sight, the most obvious solution (since we do not know which shipping option would be selected) is to define these algorithms in a single class and execute a specific calculation logic based on the customer's choice. However, this implementation is not flexible, for instance, if you want to add a new shipping type in the future, you should adjust the class by implementing the new algorithm, at the same time adding more conditional statements in the code - this violates the Open-Closed principle since you need to change the existing code for the upcoming business requirements. A better approach to this problem is to extract each algorithm into a separate class and define a common interface that will be used to inject the specific shipping costs calculation strategy into your code at run-time. Well, the Strategy design pattern is an obvious choice for this problem, isn't it?

 ###Class diagram[​](https://kazlauskas.dev/flutter-design-patterns-5-strategy/#class-diagram "Direct link to Class diagram")

The class diagram below shows the implementation of the Strategy design pattern:
![[Pasted image 20230611195141.png]]

`IShippingCostsStrategy` defines a common interface for all the specific strategies:

- `label` - a text label of the strategy which is used in UI;
- `calculate()` - method to calculate shipping costs for the order. It uses information from the `Order` class object passed as a parameter.

`InStorePickupStrategy`, `ParcelTerminalShippingStrategy` and `PriorityShippingStrategy` are concrete implementations of the `IShippingCostsStrategy` interface. Each of the strategies provides a specific algorithm for the shipping costs calculation and defines it in the `calculate()` method.

`StrategyExample` widget stores all different shipping costs calculation strategies in the `shippingCostsStrategyList` variable.

### IShippingCostsStrategy[​](https://kazlauskas.dev/flutter-design-patterns-5-strategy/#ishippingcostsstrategy "Direct link to IShippingCostsStrategy")

An interface that defines methods and properties to be implemented by all supported algorithms.
``ishipping_costs_strategy.dart``
```dart
abstract interface class IShippingCostsStrategy {  
late String label;  
double calculate(Order order);  
}
```
#### Specific implementations of the `IShippingCostsStrategy` interface[​](https://kazlauskas.dev/flutter-design-patterns-5-strategy/#specific-implementations-of-the-ishippingcostsstrategy-interface "Direct link to specific-implementations-of-the-ishippingcostsstrategy-interface")

`InStorePickupStrategy` implements the shipping strategy which requires the customer to pick up the order in the store. Hence, there are no shipping costs and the `calculate()` method returns 0.
``in_store_pickup_strategy.dart``
```dart
class InStorePickupStrategy implements IShippingCostsStrategy {
  @override
  String label = 'In-store pickup';

  @override
  double calculate(Order order) => 0.0;
}
```
`ParcelTerminalShippingStrategy` implements the shipping strategy when an order is delivered using the parcel terminal service. When using parcel terminals, each order item is sent separately and the shipping cost depends on the parcel size. The final shipping price is calculated by adding up the separate shipping cost of each order item.
`parcel_terminal_shipping_strategy.dart`
```dart
class ParcelTerminalShippingStrategy implements IShippingCostsStrategy {
  @override
  String label = 'Parcel terminal shipping';

  @override
  double calculate(Order order) => order.items.fold<double>(
        0.0,
        (sum, item) => sum + _getOrderItemShippingPrice(item),
      );

  double _getOrderItemShippingPrice(OrderItem orderItem) =>
      switch (orderItem.packageSize) {
        PackageSize.S => 1.99,
        PackageSize.M => 2.49,
        PackageSize.L => 2.99,
        PackageSize.XL => 3.49,
      };
}
```

`PriorityShippingStrategy` implements the shipping strategy which has a fixed shipping cost for a single order. In this case, the `calculate()` method returns a specific price of 9.99.
`priority_shipping_strategy.dart`
```dart
class PriorityShippingStrategy implements IShippingCostsStrategy {
  @override
  String label = 'Priority shipping';

  @override
  double calculate(Order order) => 9.99;
}
```
### Order
A simple class to store an order's information. `Order` class contains a list of order items, provides a method to add a new `OrderItem` to the order, and also defines a getter method `price` which returns the total price of the order (without shipping).
`order.dart`
```dart
class Order {
  final List<OrderItem> items = [];

  double get price =>
      items.fold(0.0, (sum, orderItem) => sum + orderItem.price);

  void addOrderItem(OrderItem orderItem) => items.add(orderItem);
}
```

### OrderItem[​](https://kazlauskas.dev/flutter-design-patterns-5-strategy/#orderitem "Direct link to OrderItem")

A simple class to store information about a single order item. `OrderItem` class contains properties to store the order item's title, price and package (parcel) size. Also, the class exposes a named constructor `OrderItem.random()` which allows creating/generating an `OrderItem` with random property values.
`order_item.dart`
```dart
class OrderItem {
  const OrderItem({
    required this.title,
    required this.price,
    required this.packageSize,
  });

  final String title;
  final double price;
  final PackageSize packageSize;

  factory OrderItem.random() {
    const packageSizeList = PackageSize.values;

    return OrderItem(
      title: faker.lorem.word(),
      price: random.integer(100, min: 5) - 0.01,
      packageSize: packageSizeList[random.integer(packageSizeList.length)],
    );
  }
}
```

### PackageSize[​](https://kazlauskas.dev/flutter-design-patterns-5-strategy/#packagesize "Direct link to PackageSize")

A special kind of class - _enumeration_ - defines different package sizes of the order item.
`package_size.dart`
```dart
enum PackageSize {
  S,
  M,
  L,
  XL,
}
```
`StrategyExample` implements the example widget of the Strategy design pattern. It contains a list of different shipping strategies (`shippingCostsStrategyList`) and provides it to the `ShippingOptions` widget where the index of a specific strategy is selected by triggering the `setSelectedStrategyIndex()` method. Then, the selected strategy is injected into the `OrderSummary` widget where the final price of the order is calculated.

`strategy_example.dart`
```dart
class StrategyExample extends StatefulWidget {
  const StrategyExample();

  @override
  _StrategyExampleState createState() => _StrategyExampleState();
}

class _StrategyExampleState extends State<StrategyExample> {
  final List<IShippingCostsStrategy> _shippingCostsStrategyList = [
    InStorePickupStrategy(),
    ParcelTerminalShippingStrategy(),
    PriorityShippingStrategy(),
  ];
  var _selectedStrategyIndex = 0;
  var _order = Order();

  void _addToOrder() => setState(() => _order.addOrderItem(OrderItem.random()));

  void _clearOrder() => setState(() => _order = Order());

  void _setSelectedStrategyIndex(int? index) {
    if (index == null) return;

    setState(() => _selectedStrategyIndex = index);
  }

  @override
  Widget build(BuildContext context) {
    return ScrollConfiguration(
      behavior: const ScrollBehavior(),
      child: SingleChildScrollView(
        padding: const EdgeInsets.symmetric(
          horizontal: LayoutConstants.paddingL,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            OrderButtons(
              onAdd: _addToOrder,
              onClear: _clearOrder,
            ),
            const SizedBox(height: LayoutConstants.spaceM),
            Stack(
              children: <Widget>[
                AnimatedOpacity(
                  duration: const Duration(milliseconds: 500),
                  opacity: _order.items.isEmpty ? 1.0 : 0.0,
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text(
                        'Your order is empty',
                        style: Theme.of(context).textTheme.titleLarge,
                      ),
                    ],
                  ),
                ),
                AnimatedOpacity(
                  duration: const Duration(milliseconds: 500),
                  opacity: _order.items.isEmpty ? 0.0 : 1.0,
                  child: Column(
                    children: <Widget>[
                      OrderItemsTable(
                        orderItems: _order.items,
                      ),
                      const SizedBox(height: LayoutConstants.spaceM),
                      ShippingOptions(
                        selectedIndex: _selectedStrategyIndex,
                        shippingOptions: _shippingCostsStrategyList,
                        onChanged: _setSelectedStrategyIndex,
                      ),
                      OrderSummary(
                        shippingCostsStrategy:
                            _shippingCostsStrategyList[_selectedStrategyIndex],
                        order: _order,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
```

`ShippingOptions` widget handles the selection of a specific shipping strategy. The widget provides a radio button list item for each strategy in the `shippingOptions` list. After selecting a specific shipping strategy, the `onChanged()` method is triggered and the selected index is passed to the parent widget (`StrategyExample`). This implementation allows us to change the specific shipping costs calculation strategy at run-time.

`shipping_options.dart`
```dart
class ShippingOptions extends StatelessWidget {
  final List<IShippingCostsStrategy> shippingOptions;
  final int selectedIndex;
  final ValueChanged<int?> onChanged;

  const ShippingOptions({
    required this.shippingOptions,
    required this.selectedIndex,
    required this.onChanged,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(LayoutConstants.paddingM),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(
              'Select shipping type:',
              style: Theme.of(context).textTheme.titleMedium,
            ),
            for (var i = 0; i < shippingOptions.length; i++)
              RadioListTile<int>(
                title: Text(shippingOptions[i].label),
                value: i,
                groupValue: selectedIndex,
                onChanged: onChanged,
                dense: true,
                activeColor: Colors.black,
              ),
          ],
        ),
      ),
    );
  }
}
```
`OrderSummary` widget uses the injected shipping strategy of type `IShippingCostsStrategy` for the final order's price calculation. The widget only cares about the type of shipping strategy, but not its specific implementation. Hence, we can provide different shipping costs calculation strategies of type `IShippingCostsStrategy` without making any changes to the UI.

`order_summary.dart`
```dart
class OrderSummary extends StatelessWidget {
  final Order order;
  final IShippingCostsStrategy shippingCostsStrategy;

  const OrderSummary({
    required this.order,
    required this.shippingCostsStrategy,
  });

  double get shippingPrice => shippingCostsStrategy.calculate(order);
  double get total => order.price + shippingPrice;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(LayoutConstants.paddingM),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(
              'Order summary',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const Divider(),
            OrderSummaryRow(
              fontFamily: 'Roboto',
              label: 'Subtotal',
              value: order.price,
            ),
            const SizedBox(height: LayoutConstants.spaceM),
            OrderSummaryRow(
              fontFamily: 'Roboto',
              label: 'Shipping',
              value: shippingPrice,
            ),
            const Divider(),
            OrderSummaryRow(
              fontFamily: 'RobotoMedium',
              label: 'Order total',
              value: total,
            ),
          ],
        ),
      ),
    );
  }
}
```


The final result of the Strategy design pattern's implementation looks like this:
https://kazlauskas.dev/assets/images/example-f81e527ee73e907ea9c1f6b66905730b.gif

![[example-f81e527ee73e907ea9c1f6b66905730b.gif]]

























## **Strategy** in Java
[source](https://refactoring.guru/design-patterns/strategy/java/example)
**Strategy** is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside original context object.

The original object, called context, holds a reference to a strategy object. The context delegates executing the behavior to the linked strategy object. In order to change the way the context performs its work, other objects may replace the currently linked strategy object with another one.

**Usage examples:** The Strategy pattern is very common in Java code. It’s often used in various frameworks to provide users a way to change the behavior of a class without extending it.

Java 8 brought the support of lambda functions, which can serve as simpler alternatives to the Strategy pattern.

Here some examples of Strategy in core Java libraries:

- [`java.util.Comparator#compare()`](http://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html#compare-T-T-) called from `Collections#sort()`.
    
- [`javax.servlet.http.HttpServlet`](http://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpServlet.html): `service()` method, plus all of the `doXXX()` methods that accept `HttpServletRequest` and `HttpServletResponse` objects as arguments.
    
- [`javax.servlet.Filter#doFilter()`](http://docs.oracle.com/javaee/7/api/javax/servlet/Filter.html#doFilter-javax.servlet.ServletRequest-javax.servlet.ServletResponse-javax.servlet.FilterChain-)
    

**Identification:** Strategy pattern can be recognized by a method that lets a nested object do the actual work, as well as a setter that allows replacing that object with a different one.

## Payment method in an e-commerce app

In this example, the Strategy pattern is used to implement the various payment methods in an e-commerce application. After selecting a product to purchase, a customer picks a payment method: either Paypal or credit card.

Concrete strategies not only perform the actual payment but also alter the behavior of the checkout form, providing appropriate fields to record payment details.

### [](https://refactoring.guru/design-patterns/strategy/java/example#example-0--strategies) **strategies**

#### [ **strategies/PayStrategy.java:** Common interface of payment methods](https://refactoring.guru/design-patterns/strategy/java/example#example-0--strategies-PayStrategy-java)

```java
package refactoring_guru.strategy.example.strategies;

/**
 * Common interface for all strategies.
 */
public interface PayStrategy {
    boolean pay(int paymentAmount);
    void collectPaymentDetails();
}
```
#### [**strategies/PayByPayPal.java:** Payment via PayPal](https://refactoring.guru/design-patterns/strategy/java/example#example-0--strategies-PayByPayPal-java) 

```java
package refactoring_guru.strategy.example.strategies;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * Concrete strategy. Implements PayPal payment method.
 */
public class PayByPayPal implements PayStrategy {
    private static final Map<String, String> DATA_BASE = new HashMap<>();
    private final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private String email;
    private String password;
    private boolean signedIn;

    static {
        DATA_BASE.put("amanda1985", "amanda@ya.com");
        DATA_BASE.put("qwerty", "john@amazon.eu");
    }

    /**
     * Collect customer's data.
     */
    @Override
    public void collectPaymentDetails() {
        try {
            while (!signedIn) {
                System.out.print("Enter the user's email: ");
                email = READER.readLine();
                System.out.print("Enter the password: ");
                password = READER.readLine();
                if (verify()) {
                    System.out.println("Data verification has been successful.");
                } else {
                    System.out.println("Wrong email or password!");
                }
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private boolean verify() {
        setSignedIn(email.equals(DATA_BASE.get(password)));
        return signedIn;
    }

    /**
     * Save customer data for future shopping attempts.
     */
    @Override
    public boolean pay(int paymentAmount) {
        if (signedIn) {
            System.out.println("Paying " + paymentAmount + " using PayPal.");
            return true;
        } else {
            return false;
        }
    }

    private void setSignedIn(boolean signedIn) {
        this.signedIn = signedIn;
    }
}

#### [](https://refactoring.guru/design-patterns/strategy/java/example#example-0--strategies-PayByCreditCard-java)
```

 **strategies/PayByCreditCard.java:** Payment via credit card
 ```java
 package refactoring_guru.strategy.example.strategies;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Concrete strategy. Implements credit card payment method.
 */
public class PayByCreditCard implements PayStrategy {
    private final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private CreditCard card;

    /**
     * Collect credit card data.
     */
    @Override
    public void collectPaymentDetails() {
        try {
            System.out.print("Enter the card number: ");
            String number = READER.readLine();
            System.out.print("Enter the card expiration date 'mm/yy': ");
            String date = READER.readLine();
            System.out.print("Enter the CVV code: ");
            String cvv = READER.readLine();
            card = new CreditCard(number, date, cvv);

            // Validate credit card number...

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    /**
     * After card validation we can charge customer's credit card.
     */
    @Override
    public boolean pay(int paymentAmount) {
        if (cardIsPresent()) {
            System.out.println("Paying " + paymentAmount + " using Credit Card.");
            card.setAmount(card.getAmount() - paymentAmount);
            return true;
        } else {
            return false;
        }
    }

    private boolean cardIsPresent() {
        return card != null;
    }
}
```

#### [**strategies/CreditCard.java:** A credit card class](https://refactoring.guru/design-patterns/strategy/java/example#example-0--strategies-CreditCard-java) 

```java
package refactoring_guru.strategy.example.strategies;

/**
 * Dummy credit card class.
 */
public class CreditCard {
    private int amount;
    private String number;
    private String date;
    private String cvv;

    CreditCard(String number, String date, String cvv) {
        this.amount = 100_000;
        this.number = number;
        this.date = date;
        this.cvv = cvv;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public int getAmount() {
        return amount;
    }
}
```
 **order/Order.java:** Order class
 ```java
 package refactoring_guru.strategy.example.order;

import refactoring_guru.strategy.example.strategies.PayStrategy;

/**
 * Order class. Doesn't know the concrete payment method (strategy) user has
 * picked. It uses common strategy interface to delegate collecting payment data
 * to strategy object. It can be used to save order to database.
 */
public class Order {
    private int totalCost = 0;
    private boolean isClosed = false;

    public void processOrder(PayStrategy strategy) {
        strategy.collectPaymentDetails();
        // Here we could collect and store payment data from the strategy.
    }

    public void setTotalCost(int cost) {
        this.totalCost += cost;
    }

    public int getTotalCost() {
        return totalCost;
    }

    public boolean isClosed() {
        return isClosed;
    }

    public void setClosed() {
        isClosed = true;
    }
}
```
**Demo.java:** Client code
```java
package refactoring_guru.strategy.example;

import refactoring_guru.strategy.example.order.Order;
import refactoring_guru.strategy.example.strategies.PayByCreditCard;
import refactoring_guru.strategy.example.strategies.PayByPayPal;
import refactoring_guru.strategy.example.strategies.PayStrategy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * World first console e-commerce application.
 */
public class Demo {
    private static Map<Integer, Integer> priceOnProducts = new HashMap<>();
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static Order order = new Order();
    private static PayStrategy strategy;

    static {
        priceOnProducts.put(1, 2200);
        priceOnProducts.put(2, 1850);
        priceOnProducts.put(3, 1100);
        priceOnProducts.put(4, 890);
    }

    public static void main(String[] args) throws IOException {
        while (!order.isClosed()) {
            int cost;

            String continueChoice;
            do {
                System.out.print("Please, select a product:" + "\n" +
                        "1 - Mother board" + "\n" +
                        "2 - CPU" + "\n" +
                        "3 - HDD" + "\n" +
                        "4 - Memory" + "\n");
                int choice = Integer.parseInt(reader.readLine());
                cost = priceOnProducts.get(choice);
                System.out.print("Count: ");
                int count = Integer.parseInt(reader.readLine());
                order.setTotalCost(cost * count);
                System.out.print("Do you wish to continue selecting products? Y/N: ");
                continueChoice = reader.readLine();
            } while (continueChoice.equalsIgnoreCase("Y"));

            if (strategy == null) {
                System.out.println("Please, select a payment method:" + "\n" +
                        "1 - PalPay" + "\n" +
                        "2 - Credit Card");
                String paymentMethod = reader.readLine();

                // Client creates different strategies based on input from user,
                // application configuration, etc.
                if (paymentMethod.equals("1")) {
                    strategy = new PayByPayPal();
                } else {
                    strategy = new PayByCreditCard();
                }
            }

            // Order object delegates gathering payment data to strategy object,
            // since only strategies know what data they need to process a
            // payment.
            order.processOrder(strategy);

            System.out.print("Pay " + order.getTotalCost() + " units or Continue shopping? P/C: ");
            String proceed = reader.readLine();
            if (proceed.equalsIgnoreCase("P")) {
                // Finally, strategy handles the payment.
                if (strategy.pay(order.getTotalCost())) {
                    System.out.println("Payment has been successful.");
                } else {
                    System.out.println("FAIL! Please, check your data.");
                }
                order.setClosed();
            }
        }
    }
}
```

**OutputDemo.txt:** Execution result
```sh
Please, select a product:
1 - Mother board
2 - CPU
3 - HDD
4 - Memory
1
Count: 2
Do you wish to continue selecting products? Y/N: y
Please, select a product:
1 - Mother board
2 - CPU
3 - HDD
4 - Memory
2
Count: 1
Do you wish to continue selecting products? Y/N: n
Please, select a payment method:
1 - PalPay
2 - Credit Card
1
Enter the user's email: user@example.com
Enter the password: qwerty
Wrong email or password!
Enter user email: amanda@ya.com
Enter password: amanda1985
Data verification has been successful.
Pay 6250 units or Continue shopping?  P/C: p
Paying 6250 using PayPal.
Payment has been successful.
```
