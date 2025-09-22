[source-blog](https://iamvishnu.com/posts/software-design-patterns-in-real-life)
# Software Design Patterns in Real-Life Software Development

2021-04-16

_This is an extension of an answer that I wrote [on Quora](https://www.quora.com/How-are-design-patterns-implemented-in-real-life/answer/Vishnu-Haridas) years back._

The question is: **How are software design patterns implemented in real life?**

Design Patterns are actually used extensively in real-life software projects, and their main purpose is creating readable, extensible, reusable, and maintainable software.

Of course, you can write software without using any of the design patterns, it will work, but you will end up in a massive pile of source code that looks like a dense forest to a new developer. Adding a new feature, or extending some existing feature will be a tough task.

Let's consider a real-life example: An application that prints tickets. For simplicity, let's focus on the ticket "printing" functionality only.

The requirements are:

- There are different types of printers.
- Currently, it should support dot matrix and inkjet printers.
- The client may add other types of printers later.

One way to do this is to write drivers for each of the printers and embed them into the code. Just straightforward logic, something like this:

```java
String selectedPrinter = showPrinterSelectionDialog();

if(selectedPrinter == "DotMatrix"){

  Device device = loadDriver("dot_matrix.driver");
  rollRibbon(device);
  heatHammers(device);
  startPrinting(device, text);

} else if(selectedPrinter == "InkjetPrinter"){

  int port = startInkjetPrinter();
  sendSignal(PRINT_START, port);
  sendData(PRINT_DATA, text.toBytesArray(), port);
  sendSignal(PRINT_STOP, port);

} else {
  throw new Exception("Please choose a valid printer");
}
```

There are several problems with this approach:

- Maintenance of this code is a little bit tough in the long term. It has everything related to the printer in a large single file, with many `if-else` conditions. Changing a line could break something else.
- Extending it by adding a new printer? We have to write a new printer driver between those lines, still ensuring not to break the existing functionality.
- Poor readability - because of the complex structure, it's tough to understand the logic.

Editing these kinds of codebases is a little bit tricky, and can be challenging sometimes.

Let's try out a different approach and try to get rid of these problems.

## Applying some design patterns

First, you will create an interface named "Printer" which has one job to do — **to print a given text**.

```java
interface Printer{ 
  void print(String text); 
}
```

Then you pass this interface to other developers, who will write implementations:

```java
class InkjetPrinter implements Printer { 
  void print(String text){ 
    // spray ink to the paper, roll the paper, etc. 
  } 
} 
```

```java
class DotMatrixPrinter implements Printer { 
  void print(String text){ 
    // heat the hammers, roll the ribbon, strike each letter, etc. 
  } 
} 
```

Next, when you need to print something, you will just write:

```java
Printer ticketPrinter = new InkjetPrinter(); 

ticketPrinter.print("This is a sample message"); 
```

You see, how that worked? You simply created an Inkjet printer instance, and printed it on the Inkjet printer! If you want to change the printer to a Dot Matrix one, you can change the first line to:

```java
Printer ticketPrinter = new DotMatrixPrinter();
```

...and the rest is handled by the DotMatrixPrinter class.

When your new developer wants to add a new "Multijet Color Printer", they will just implement the `Printer` interface like this:

```java
class MultijetColorPrinter implements Printer {
  void print(String text){
    // Calculate canvas dimensions
    // Warm up the jets and ink tanks
    // Start printing the given text...
  }
}
```

...and change the printer initilization to:

```java
Printer ticketPrinter = new MultijetColorPrinter();
```

...and that's it! It now prints on the new Multijet Color Printer with only a single line of change within the existing code.

You just saw an example of the very famous [SOLID principles](https://en.wikipedia.org/wiki/SOLID). SOLID lists five useful principles to make use of interfaces and abstractions to make the code more readable, extensible, and maintainable.

## More to do: adding a printer "Factory"

Now we are initializing printer objects directly by using its constructor. What if we have a helper class that can take care of initializing the printer objects? Technically, that's a kind of a "factory" pattern.

A [factory pattern](https://en.wikipedia.org/wiki/Factory_method_pattern) helps to create objects without exposing the creation logic and returns the object using a common interface.

Now we can put all the printer creation logic inside a single class called `PrinterFactory` and add a function to create printer objects for us without even knowing the initilization logic for each of them.

```java
class PrinterFactory {
   
  enum TYPE { 
    LASER,
    INKJET,
    DOT_MATRIX,
    MULTIJET_COLOR,
    // Add a new printer type here.
  }

  // creates a printer object.
  static Printer createPrinter(TYPE type){

    switch(type){
      case LASER: return new LaserPrinter();
      case INKJET: return new InkjetPrinter();
      case DOT_MATRIX: return new DotMatrixPrinter();
      case MULTIJET_COLOR: return new MultijetColorPrinter();
      // return your new printer from here.

      default: throw new Exception("Invalid printer"); // or return a default from above.
    }

  }
}
```

Thus the code will change to:

```java
Printer ticketPrinter = PrinterFactory.createPrinter(PrinterFactory.LASER);
```

Or

```java
Printer ticketPrinter = PrinterFactory.createPrinter(PrinterFactory.DOT_MATRIX);
```

See, the code is getting easier to understand, and it's now more extensible and maintainable. Adding another type of printer isn't a big task now. Just write an implementation of the `Printer` interface, and add the new implementation to the `PrinterFactory` class. DONE!

## A popular use-case

Most of the time the REST APIs will not be ready when we start a new project. So we will come up with an interface, and write a mock implementation that can be consumed until the real APIs are available. Once the API service is ready, we switch the mock implementation with the real one — mostly a single line to change.  It looks something like this:

```java
// The interface
interface RestApi {
  UserInfo login(String username, String pass);
  Settings getSettings(String token);
}

// Mock Implementation - just returns some dummy response.
class MockApi implements RestApi {

  UserInfo login(String username, String pass) {
    // Add some delay here to simulate network latency.
    return new UserInfo("Alice", "alice@example.com", "token_9e95fc382738fdaaa02a4617842efed7");
  }

  Settings getSettings(String token) {
    return new Settings(
      sendEmails = true, 
      email = "alice@example.com", 
      notifications = true
    );
  }
}

// Real API implementation - makes HTTP calls.
class MyAppApi implements RestApi {

  UserInfo login(String username, String pass) {
    Json response = HttpHelper.callApi("/login", username, pass);
    return UserInfo.fromJson(response);
  }

  Settings getSettings(String token) {
    Json response = HttpHelper.callApi("/me/settings", token);
    return Settings.fromJson(response);
  }
}
```

Now we consume the mock APIs like this everywhere in the app:

```java
RestApi api = new MockApi();

UserInfo user = api.login(someName, somePassword);
Settings settings = api.getSettings(user.token);
```

Once the real API service is ready, we can switch the first line to the real API implementation like this:

```java
RestApi api = new MyAppApi();
```

...and it will work seamlessly! We do this "mocking" a lot to do experiments, like testing UI for certain API responses.

---

  
Software design patterns are a vast subject. Learning them will help you to approach problems from a different perspective, and helps greatly in writing readable, extensible, and maintainable code. These patterns and principles are really important in large-scale software projects.

References: Here's the [Wikipedia article](https://en.wikipedia.org/wiki/Software_design_pattern) on design patterns. Here's an [interesting website](https://refactoring.guru/design-patterns) that I found. Still, do a Google search for ["Software Design Patterns"](https://www.google.com/search?q=software+design+patterns) and ["SOLID principles"](https://www.google.com/search?q=solid+principles) for more articles, illustrations, and tutorials.