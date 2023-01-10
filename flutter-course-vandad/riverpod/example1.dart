import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

final currentDate = Provider((_) => DateTime.now());

class Example1 extends ConsumerWidget {
  const Example1({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final date = ref.watch(currentDate);
    return Center(
        child: Text("Hellooooo consumer wid ${date.toString()}",
            textDirection: TextDirection.ltr));
  }
}
