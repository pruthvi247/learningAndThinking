import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

enum City {
  tirupathi,
  banglore,
  chennai,
  amaravathi,
}

typedef WeatherEmoji = String;

Future<WeatherEmoji> getWeather(City? city) {
  return Future.delayed(
    const Duration(seconds: 1),
    () => {
      City.tirupathi: "🎯",
      City.banglore: "💎",
      City.chennai: "🔥",
      City.amaravathi: "🎉"
    }[city]!,
  );
}

const String unknownWeatherEmoji = '🤷🏻‍♂️';

/// UI will write and read to this provider
final currentCityProvider = StateProvider<City?>(
  (_) => null,
);
//// UI will read form this provider
final weatherProvider = FutureProvider<WeatherEmoji>((weatherRef) {
  final city = weatherRef.watch(currentCityProvider);
  if (city != null) {
    return getWeather(city);
  } else {
    return unknownWeatherEmoji;
  }
});

class Example3 extends ConsumerWidget {
  const Example3({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // final val = ref.watch(counterProvider);
    // print("TRACE: Bild method ${val.toString()} ");
    print("TRACE: Bild method");
    final currentWeather = ref.watch(weatherProvider);
    return Scaffold(
      appBar: AppBar(title: Consumer(builder: (context, ref, child) {
        return const Text('Future provider');
      })),
      body: Column(
        children: [
          currentWeather.when(
            data: (data) => Text(data),
            error: (obj, err) => const Text("💣"),
            loading: (() => const Center(
                  child: CircularProgressIndicator(),
                )),
          ),
          Expanded(
              child: ListView.builder(
                  itemCount: City.values.length,
                  itemBuilder: (BuildContext cxt, index) {
                    final city = City.values[index];
                    final isSelected = city == ref.watch(currentCityProvider);
                    return ListTile(
                      title: Text(city.toString()),
                      trailing: isSelected ? const Icon(Icons.check) : null,
                      onTap: () {
                        ref
                            .read(
                              currentCityProvider.notifier,
                            )
                            .state = city;
                      },
                    );
                  })),
        ],
      ),
    );
  }
}
