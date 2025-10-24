import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:uuid/uuid.dart';

@immutable
class Person {
  final String id;
  final String name;
  final int age;

  Person({
    String? id,
    required this.name,
    required this.age,
  }) : id = id ?? const Uuid().v4();
  Person updated([String? name, int? age]) => Person(
        name: name ?? this.name,
        age: age ?? this.age,
        id: id,
      );
  String get displayName => '$name ($age years old)';

  @override
  bool operator ==(covariant Person other) => id == other.id;
  @override
  int get hashCode => id.hashCode;
  // int get hashCode => Object.hash(name, age, id);

  @override
  String toString() => 'Person(name:$name,age:$age,id:$id)';
}

class DataModel extends ChangeNotifier {
  final List<Person> _people = [];

  int getCount() => _people.length;
  UnmodifiableListView<Person> get people => UnmodifiableListView(_people);

  void addPerson(Person person) {
    _people.add(person);
    notifyListeners();
  }

  void remove(Person person) {
    _people.remove(person);
    notifyListeners();
  }

  void update(Person updatedPerson) {
    final index = _people.indexOf(updatedPerson);
    final oldPerson = _people[index];
    if (oldPerson.name != updatedPerson.name ||
        oldPerson.age != updatedPerson.age) {
      _people[index] = oldPerson.updated(
        updatedPerson.name,
        updatedPerson.age,
      );
      notifyListeners();
    }
  }
}

final nameController = TextEditingController();
final ageController = TextEditingController();

Future<Person?> createOrUpdatePersonDialog(
  BuildContext ctx, [
  Person? existingPerson,
]) {
  String? name = existingPerson?.name;
  int? age = existingPerson?.age;
  nameController.text = name ?? '';
  ageController.text = age?.toString() ?? '';
  return showDialog(
      context: ctx,
      builder: (ctx) {
        return AlertDialog(
          title: const Text("create person"),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: nameController,
                decoration:
                    const InputDecoration(labelText: 'Enter name here...'),
                onChanged: (value) {
                  name = value;
                },
              ),
              TextField(
                controller: ageController,
                decoration:
                    const InputDecoration(labelText: 'Enter age here...'),
                onChanged: (value) {
                  age = int.parse(value);
                },
              ),
            ],
          ),
          actions: [
            TextButton(
                onPressed: () => Navigator.of(ctx).pop(),
                child: const Text('cancle')),
            TextButton(
                onPressed: () {
                  if (name != null && age != null) {
                    if (existingPerson != null) {
                      final newPerson = existingPerson.updated(
                        name,
                        age,
                      );
                      Navigator.of(ctx).pop(
                        newPerson,
                      );
                    } else {
                      Navigator.of(ctx).pop(Person(
                        name: name!,
                        age: age!,
                      ));
                    }
                  } else {
                    Navigator.of(ctx).pop();
                  }
                },
                child: const Text('save'))
          ],
        );
      });
}

final peopleProvider = ChangeNotifierProvider(
  (_) => DataModel(),
);

class Example5 extends ConsumerWidget {
  const Example5({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(title: Consumer(builder: (context, ref, child) {
        return const Text('Change notifier');
      })),
      body: Consumer(builder: (contex, widRef, child) {
        final dataModel = widRef.watch(peopleProvider);
        return ListView.builder(
          itemCount: dataModel.getCount(),
          itemBuilder: (context, index) {
            final person = dataModel.people[index];
            return ListTile(
              title: GestureDetector(
                child: Text(person.displayName),
                onTap: () async {
                  final updatedPerson =
                      await createOrUpdatePersonDialog(context, person);
                  if (updatedPerson != null) {
                    dataModel.update(updatedPerson);
                  }
                },
              ),
            );
          },
        );
      }),
      floatingActionButton: FloatingActionButton(
          child: const Icon(Icons.add),
          onPressed: () async {
            final person = await createOrUpdatePersonDialog(context);
            if (person != null) {
              final dataModel = ref.read(peopleProvider);
              dataModel.addPerson(person);
              // Navigator.of(context).pop();
            } else {
              // Navigator.of(context).pop();
            }
          }),
    );
  }
}
