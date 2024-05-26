## Dart `export` and `part/partof`
[source-stack-overflow](https://stackoverflow.com/questions/65176443/part-and-export-what-is-the-usage-in-dart)
Here is a simple code sample comprised of 3 files.Explanations for all features are included in comments throughout the files.
`library_main.dart`
```dart
// declare a name for this library to reference from parts
// this is not necessary if we do not need to reference elsewhere
// NOTE: generally, a Dart file is a Library
library counter;

// export adds contents of another Library to this Library's namespace
// here we are adding all content (accessible from outside the library) from
// the material library
// NOTE: this is intended for related libraries
// this arbitrary usage is simply for demonstration purposes
export 'package:flutter/material.dart';

// for finer control, we can use the 'show' directive
// try this to see the effects of selected export
// export 'package:flutter/material.dart' show StatefulWidget, State;

// include any files containing parts of this library
part 'library_part.dart';

class Counter extends AbstractCounter {
  // we can access library private variable _count even though it is in a different
  // file because we made it part of the same library
  reset() => _count = 0;
}
```
`library_part.dart`
```dart
// declare this file as part of the counter library
part of counter;

abstract class AbstractCounter {
  // this is a library private variable (_varName)
  // if this file were not made part of the counter library, this variable
  // would not be accessible to the Counter class in library_main.dart
  // this is an important concept to understand about Dart's library privacy
  // it differs from class based privacy, like that used in Java
  int _count = 0;

  get count => _count;
  increment() => ++_count;
}
```
`library_example.dart`
```dart
// note that 'material.dart' does not need to be imported
// because it has been exported with the counter library
import 'library_main.dart';

class LibraryExample extends StatefulWidget {
  @override
  _LibraryExampleState createState() => _LibraryExampleState();
}

class _LibraryExampleState extends State<LibraryExample> {
  final _counter = Counter();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Library Example'),
      ),
      body: Center(
        child: Text('You have pressed the button ${_counter.count} times.'),
      ),
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          FloatingActionButton(
            child: Text('Reset'),
            onPressed: () => setState(() => _counter.reset()),
          ),
          SizedBox(width: 10),
          FloatingActionButton(
            child: Icon(Icons.add),
            onPressed: () => setState(() => _counter.increment()),
          ),
        ],
      ),
    );
  }
}
```



