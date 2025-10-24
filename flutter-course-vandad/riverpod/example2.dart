import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

final currentDate = Provider((_) => DateTime.now());

extension OptionalInfixAddition<T extends num> on T? {
  T? operator +(T? other) {
    final shadow = this;
    if (shadow != null) {
      return shadow + (other ?? 0) as T;
    } else {
      return null;
    }
  }
}

final counterProvider = StateNotifierProvider<Counter, int>(
  (ref) => Counter(),
);

class Counter extends StateNotifier<int> {
  Counter() : super(2);
  void increment() => state = state == null ? 1 : state + 1;
  int? get value => state;
}

class Example2 extends ConsumerWidget {
  const Example2({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // final val = ref.watch(counterProvider);
    // print("TRACE: Bild method ${val.toString()} ");
    print("TRACE: Bild method");
    return Scaffold(
      //// using val = ref.watch(counterProvider); and val value in app bar will re trigger the build method every time
      /// when counter is pressed, where as if we use consumer in app bar , will only rebuild the app bar but not entire widget
      // appBar: AppBar(title: Text('${val}')),
      appBar: AppBar(title: Consumer(builder: (context, ref, child) {
        final count = ref.watch(counterProvider);
        print("TRACE: Appbar ");

        return Text(count.toString());
      })),
      body: Column(
        children: [
          TextButton(
            child: const Text('Increment counter'),
            // onPressed: ref.read(counterProvider.notifier).increment,
            onPressed: () {
              ref.read(counterProvider.notifier).increment();
              // final abc = ref.read(counterProvider.notifier).state;
              print(
                  "TRACE: On pressed ${ref.read(counterProvider.notifier).value}");
            },
          ),
        ],
      ),
    );
  }
}
