import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

@immutable
class Film {
  final String id;
  final String title;
  final String description;
  final bool isFavorite;
  const Film({
    required this.id,
    required this.title,
    required this.description,
    required this.isFavorite,
  });
  Film copy({
    required bool isFavorite,
  }) =>
      Film(
          id: id,
          title: title,
          description: description,
          isFavorite: isFavorite);
  @override
  String toString() =>
      'Film(id: $id,title: $title,description: $description,isFavorite: $isFavorite)';
  @override
  bool operator ==(covariant Film other) =>
      id == other.id && isFavorite == other.isFavorite;
  @override
  int get hasCode => Object.hashAll([id, isFavorite]);
}

const allFilms = [
  Film(
      id: "1", title: "title1", description: "description1", isFavorite: false),
  Film(
      id: "2", title: "title2", description: "description2", isFavorite: false),
  Film(
      id: "3", title: "title3", description: "description3", isFavorite: false),
  Film(
      id: "4", title: "title4", description: "description4", isFavorite: false),
  Film(
      id: "5", title: "title5", description: "description5", isFavorite: false),
  Film(
      id: "6", title: "title6", description: "description6", isFavorite: false),
];

class FilmsNotifier extends StateNotifier<List<Film>> {
  FilmsNotifier() : super(allFilms);
  void update(Film film, bool isFavorite) {
    state = state
        .map((thisFilm) => thisFilm.id == film.id
            ? thisFilm.copy(
                isFavorite: isFavorite,
              )
            : thisFilm)
        .toList();
  }
}

enum Favouritestatus {
  all,
  favorites,
  notFavorite,
}

final favoriteStatusProvider = StateProvider<Favouritestatus>(
  (_) => Favouritestatus.all,
);

final allFilmsProvider = StateNotifierProvider<FilmsNotifier, List<Film>>(
  (_) => FilmsNotifier(),
);

final favoriteFilmProvider = Provider<Iterable<Film>>(
  (ref) => ref.watch(allFilmsProvider).where((film) => film.isFavorite),
);
final notFavoriteFilmProvider = Provider<Iterable<Film>>(
  (ref) => ref.watch(allFilmsProvider).where((film) => !film.isFavorite),
);

class FilmsWidget extends ConsumerWidget {
  final AlwaysAliveProviderBase<Iterable<Film>> provider;

  const FilmsWidget({
    required this.provider,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final films = ref.watch(provider);
    return Expanded(
        child: ListView.builder(
      itemCount: films.length,
      itemBuilder: (contex, index) {
        final film = films.elementAt(index);
        final favoriteIcon = film.isFavorite
            ? const Icon(Icons.favorite)
            : const Icon(Icons.favorite_border);
        return ListTile(
          title: Text(film.title),
          subtitle: Text(film.description),
          trailing: IconButton(
              onPressed: () {
                final isfav = !film.isFavorite;
                ref.read(allFilmsProvider.notifier).update(
                      film,
                      isfav,
                    );
              },
              icon: favoriteIcon),
        );
      },
    ));
  }
}

class FilterWidget extends StatelessWidget {
  const FilterWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer(
      builder: ((context, ref, child) {
        return DropdownButton<Favouritestatus>(
          value: ref.watch(favoriteStatusProvider),
          items: Favouritestatus.values
              .map(
                (fs) => DropdownMenuItem<Favouritestatus>(
                  value: fs,
                  child: Text(
                    fs.toString().split('.').last,
                  ),
                ),
              )
              .toList(),
          onChanged: (Favouritestatus? fs) {
            ref
                .read(
                  favoriteStatusProvider.notifier,
                )
                .state = fs!;
          },
        );
      }),
      child: const Text("data"),
    );
  }
}

class Example6 extends ConsumerWidget {
  const Example6({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    print("TRACE: Bild method");
    return Scaffold(
      appBar: AppBar(title: Text('Riverpod vandad')),
      body: Column(
        children: [
          const FilterWidget(),
          Consumer(builder: (context, ref, child) {
            final filter = ref.watch(favoriteStatusProvider);
            switch (filter) {
              case Favouritestatus.all:
                return FilmsWidget(provider: allFilmsProvider);
              case Favouritestatus.favorites:
                return FilmsWidget(provider: favoriteFilmProvider);

              case Favouritestatus.notFavorite:
                return FilmsWidget(provider: notFavoriteFilmProvider);

              default:
                return FilmsWidget(provider: allFilmsProvider);
            }
            // return const FilmsWidget(provider: provider);
          })
        ],
      ),
    );
  }
}
