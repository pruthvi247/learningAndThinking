## Advanced dart

##### Extensions
Example
```dart
extension NumberParsing on String {
  int parseInt() {
    return int.parse(this);
  }
  // ···
}
print('42'.padLeft(5)); // Use a String method.
print('42'.parseInt()); // Use an extension method.
```

##### Generators
1.  **Synchronous** Generator: Returns an [**Iterable**](https://api.dart.dev/stable/dart-core/Iterable-class.html) object.
2.  **Asynchronous** Generator: Returns a [**Stream**](https://api.dart.dev/stable/dart-async/Stream-class.html) object.
- A generator in dart is a fuction which returns list of things (Iterable)
- iterables in dart are kind of lazy collections
- anology for iterable (lazy collection) - Food in restaurant is prepared based on the orders placed

##### Synchronous Generator in Dart

The synchronous generator returns an iterable object i.e. it returns the collection of values, or “elements”, that can be accessed sequentially. To implement **synchronous** generator function, mark the function body as **sync***, and use **yield statements** to deliver value(s).
```dart
// sync* functions return an iterable
Iterable geeksForGeeks(int number) sync* {
int geek = number;
while (geek >= 0) {
	
	// Checking for even number
	if (geek % 2 == 0) {
		
	// 'yield' suspends
	// the function
	yield geek;
		
	}
	
	// Decreasing the
	// variable geek
	geek--;
}
}

// Main Function
void main()
{
print("------- Geeks For Geeks --------");
	
print("Dart Synchronous Generator Example For Printing Even Numbers From 10 In
		Reverse Order:");
	
// Printing positive even numbers
// from 10 in reverse order
geeksForGeeks(10).forEach(print);
}

```

##### Asynchronous Generator in Dart

The asynchronous generator returns a stream object. A Stream provides a way to receive a sequence of events. Each event is either a data event, also called an _**element**_ of the stream, or an error event, which is a notification that something has failed. To implement an **asynchronous** generator function, mark the function body as **async***, and use **yield statements** to deliver value(s).

```dart
// async* function(s) return an stream
Stream geeksForGeeks(int number) async* {
int geek = 0;
	
// Checking for every
// geek less than number
while (geek <= number) yield geek++;
// Incrementing geek
// after printing it
}

// Main Function
void main()
{
print("-------- Geeks For Geeks -----------");
	
print("Dart Asynchronous Generator Example For Printing Numbers Less Than 10:");
	
// Printing numbers less
// than or equal to 10
geeksForGeeks(10).forEach(print);
}

```
#### Generics
