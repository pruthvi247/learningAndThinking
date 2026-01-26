import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

const names = [
  "hello world",
  "below world",
  "side world",
  "top world",
  "under world",
  "super world",
  "another world"
];

final tickerProvider = StreamProvider((ref) {
  return Stream.periodic(
    const Duration(
      seconds: 1,
    ),
    (i) => i + 1,
  );
});

final namesProvider = StreamProvider(
  ((ref) => ref.watch(tickerProvider.stream).map(
        (event) => names.getRange(
          0,
          event,
        ),
      )),
);

class Example4 extends ConsumerWidget {
  const Example4({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final names = ref.watch(namesProvider);
    return Scaffold(
      appBar: AppBar(title: Consumer(builder: (context, ref, child) {
        return const Text('Stream Provider');
      })),
      body: names.when(
          data: (names) {
            return ListView.builder(
              itemBuilder: (ctx, index) {
                return ListTile(title: Text(names.elementAt(index)));
              },
              itemCount: names.length,
            );
          },
          error: (_, a) => Text("Reached limit"),
          loading: () => const Center(
                child: CircularProgressIndicator(),
              )),
    );
  }
}
