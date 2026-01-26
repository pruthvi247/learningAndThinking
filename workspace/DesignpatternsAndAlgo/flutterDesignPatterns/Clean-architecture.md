[Source](https://medium.com/@kamal.lakhani56/clean-architecture-f23b7d9c6ee7)
[Git](https://github.com/fluttertutorialin/cubit_clean_archi?source=post_page-----f23b7d9c6ee7--------------------------------)

# MVC

**Model View Controller (MVC)** — MVC is a default architecture for iOS apps. Every screen is splitted into three components:

- **Model** — where we put our business entities and application models
- **View** — where we show formatted data to the user
- **Controller** — to transform data and handle user interactions

# MVP

**Model View Presenter (MVP)** — This architecture is very similar to MVC, but all the UI business logic is stored in the presenter. For example, we can ask the presenter to show the next view in case of handle button action. Also presenter interacts with a model to fetch and parse business entities. In other words, the presenter contains a method called by view and makes actions on a view. In this case presenter contains reference to the view.

# MVVM

**Model View ViewModel (MVVM)** — Another similar architecture but in this case, we could treat viewmodel as another side of a view abstraction. Viewmodel provides wrapper to model data that can be linked to view. Viewmodel contains commands (methods) to communicate with the model and the view.

_Example_: View could ask for service data in case of tapping button. ViewModel is responsible for fetching the data from service, parsing, processing them, and returning to the view in a proper manner.

The main difference between ViewModel and the presenter is that viewmodel doesn’t know anything about the view.

Another difference is that viewmodel could be shared with other views. Presenters do not. Presenters are associated with a concrete view.

MVVM with Clean Architecture

MVVM and Clean Architecture are two architectural patterns commonly used in Android app development.

Combining these two patterns can lead to a well-structured, maintainable and testable Android application.

𝗠𝗩𝗩𝗠 separates your app into three main components — Model, View, and ViewModel.

- 𝗠𝗼𝗱𝗲𝗹: Represents your data and business logic.  
- 𝗩𝗶𝗲𝘄: Represents the UI components.  
- 𝗩𝗶𝗲𝘄𝗠𝗼𝗱𝗲𝗹: Acts as an intermediary between the Model and View, providing data to the View and handling user interactions.
# Clean Architecture

𝗖𝗹𝗲𝗮𝗻 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲 emphasizes the separation of concerns and the independence of different layers within your app.

- 𝗗𝗼𝗺𝗮𝗶𝗻 𝗟𝗮𝘆𝗲𝗿: Contains your business logic and entities.  
- 𝗗𝗮𝘁𝗮 𝗟𝗮𝘆𝗲𝗿: Manages data access and storage.  
- 𝗣𝗿𝗲𝘀𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻 𝗟𝗮𝘆𝗲𝗿: Handles UI and user interactions.
Every architecture has one common thing — separation of concerns.

Clean Architecture is an architectural pattern that was introduced by Robert C. Martin. It provides a way to structure applications that separate the different components of an application into modules, each with a well-defined purpose. The main idea behind Clean Architecture is to separate the application into three main layers: the presentation layer, the domain layer, and the data layer.

The **Dependency Inversion Principle (DIP)** asserts that high-level modules shouldn’t depend on low-level modules but rather that both should depend on abstractions. Flutter Clean Architecture abides by this rule. This typically entails utilizing abstract classes and interfaces in Flutter to specify the contracts across layers, facilitating easier testing and the flexibility of changing implementations.

We have 4 different layers here. Let’s go deeper.
![[Pasted image 20231012160627.png]]

# Data Layer

Represents the data layer of the application. The Data module, which is a part of the outermost layer, is responsible for data retrieval. This can be in the form of API calls to a server and/or a local database. It also contains repository implementations.

- **Repositories (Domain)**: Actual implementations of the repositories in the Domain layer. Repositories are responsible for coordinating data from the different Data Sources.
- **DTO Models:** Representation of JSON structure that allows us to interact with our data sources.
- **Data sources:** Consist of remote and local Data Sources. Remote Data Source will perform HTTP requests on the API. While local Data Source will cache or persist data.
- **Mapper:** Map Entity objects to Models and vice-versa.

Our **data layer** consists of converter, database, and repository packages. Since the **data layer** depends upon the **domain layer**, we do repository implementation here as said above. The repository communicates with the database, but for each database, we need a separate model, therefore the converter package.

# Model class (mapper class) relationship Entities class

Mapper is a straightforward class, to map data that we get from the API — in our case the DTO — to our business object.

![[Pasted image 20231012161211.png]]

```dart
import 'package:freezed_annotation/freezed_annotation.dart';  
part 'department_entity.freezed.dart';  
  
@Freezed(copyWith: false, equal: false)  
class DepartmentEntity with _$DepartmentEntity {  
const factory DepartmentEntity(  
{ final int? id,  
final String? day}) = _DepartmentEntity;  
  
const DepartmentEntity._();  
}
```
```dart
import 'package:freezed_annotation/freezed_annotation.dart';  
  
part 'department_mapper.freezed.dart';  
part 'department_mapper.g.dart';  
  
@Freezed(copyWith: false, equal: false)  
class DepartmentMapper with _$DepartmentMapper {  
const factory DepartmentMapper(  
{@JsonKey(name: 'ID') final int? id,  
@JsonKey(name: 'DAY')  
final String? day}) = _DepartmentMapper;  
  
const DepartmentMapper._();  
  
factory DepartmentMapper.fromJson(Map<String, dynamic> json) =>  
_$DepartmentMapperFromJson(json);  
}  
  
extension DepartmentExtension on DepartmentMapper {  
DepartmentEntity toDomain() =>  
DepartmentEntity(id: id, day: day);  
}
```
```dart
response.data.map<DepartmentEntity>((data) => DepartmentMapper.fromJson(data).toDomain()).toList()
```
# Equatable

Equatable is a popular Flutter package that makes it easy to compare objects for equality. It’s particularly useful when working with Dart’s built-in `==` operator, which can lead to unintended equality checks for objects with the same data but different references.

Equatable is a Dart package that helps you override the equality (`==`) and hash code (`hashCode`) methods in your classes without writing a lot of boilerplate code. It provides a concise and elegant way to define equality for objects based on their properties, rather than their memory addresses.
# Serializable
```dart
part 'department_mapper.g.dart';  
  
@JsonSerializable()  
class DepartmentMapper extends DepartmentEntity {  
@override  
@JsonKey(name: JsonKeyConstant.idConsignmentJsonKey)  
final int? id;  
  
@override  
@JsonKey(name: JsonKeyConstant.dayConsignmentJsonKey)  
final String? day;  
  
const DepartmentMapper({this.id, this.day})  
: super(id: id, day: day);  
  
factory DepartmentMapper.fromJson(Map<String, dynamic> json) =>  
_$DepartmentMapperFromJson(json);  
  
Map<String, dynamic> toJson() => _$DepartmentMapperToJson(this);  
}
```
```dart
import 'package:equatable/equatable.dart';  
  
class DepartmentEntity extends Equatable {  
final int? _id;  
final String? _day;  
  
const DepartmentEntity({int? id, String? day})  
: _id = id,  
_day = day;  
  
int? get id => _id;  
  
String? get day => _day;  
  
@override  
List<Object> get props => [_id!, _day!];  
  
@override  
bool get stringify => true;  
}
```
```dart
List<DepartmentMapper>.from(response.data  
.map((i) => DepartmentMapper.fromJson(i)))
```
# Use cases

The second layer is responsible for fetching entities from the backend. Just fetching — not parsing! This could be known in our app as **Services**. We could communicate with a server using sockets, REST, or any other known way. Use cases (or services) are not affected by controllers, view models, etc. but they could be affected if some of the entities change. This scenario is known as Dependency Rule and we use a pattern called Crossing Boundaries. We could cross architecture boundaries only in a specific way. Only from the top to the bottom.

- Use Cases: Application-specific business rules. Ause case is a piece of business logic that represents a single task that the system needs to perform. The use case encapsulates the rules and logic required to perform the task, and defines the inputs and outputs required for the operation.
- Entities: Business objects of the application
- Repositories: Abstract classes that define the expected functionality of outer layers
![[Pasted image 20231012161619.png]]

```kotlin
class LoginRemote  
    extends UseCase<Either<RemoteFailure, LoginEntity>, LoginInput> {  
  final GetLoginRepository getLoginRepository;  
  
  LoginRemote(this.getLoginRepository);  
  
  // User login Use case  
  @override  
  Future<Either<RemoteFailure, LoginEntity>> call(LoginInput input) =>  
      getLoginRepository(input: input.toJson());  
}

abstract class GetLoginRepository {  
  Future<Either<RemoteFailure, LoginEntity>> call({Map<String, dynamic>? input});  
}

class GetLoginRepositoryImp extends GetLoginRepository {  
  final RemoteDataSource _remoteDataSource;  
  
  GetLoginRepositoryImp(this._remoteDataSource);  
  
  @override  
  Future<Either<RemoteFailure, LoginEntity>> call(  
      {Map<String, dynamic>? input}) {  
    return _remoteDataSource.login(input: input);  
  }  
}

@Freezed(copyWith: false, equal: false)  
class LoginInput with _$LoginInput {  
  @JsonSerializable(fieldRename: FieldRename.snake, explicitToJson: true)  
  factory LoginInput(  
      {@JsonKey(name:'MOBILE') required String mobile,  
      @JsonKey(name:'PASSWORD') required String password,  
      @JsonKey(name:'DEVICE_ID') String? deviceId,  
      @JsonKey(name:'FIREBASE_TOKEN')  
      String? firebaseToken}) = _LoginInput;  
  
  factory LoginInput.fromJson(Map<String, dynamic> json) =>  
      _$LoginInputFromJson(json);  
}

//KOTLIN  
  
data class Category(  
    val name: String,  
    val color: Int = Ivy.toArgb(),  
    val icon: String? = null,  
    val orderNum: Double = 0.0,  
  
    val isSynced: Boolean = false,  
    val isDeleted: Boolean = false,  
  
    val id: UUID = UUID.randomUUID()  
) {  
    fun toEntity(): CategoryEntity = CategoryEntity(  
        name = name,  
        color = color,  
        icon = icon,  
        orderNum = orderNum,  
        isSynced = isSynced,  
        isDeleted = isDeleted,  
        id = id  
    )  
}

//KOTLIN  
  
@Serializable  
internal data class MovieRemote(  
    val id: Int,  
    val title: String,  
    val overview: String,  
    @SerialName("poster_path")  
    val posterImage: String,  
    @SerialName("release_date")  
    val releaseDate: String  
)  
  
import kotlinx.serialization.SerialName  
import kotlinx.serialization.Serializable  
  
@Serializable  
internal data class MovieRemote(  
    val id: Int,  
    val title: String,  
    val overview: String,  
    @SerialName("poster_path")  
    val posterImage: String,  
    @SerialName("release_date")  
    val releaseDate: String  
)  
  
internal fun MovieRemote.toMovie() : Movie {  
    return Movie(  
        id = id,  
        title = title,  
        description = overview,  
        imageUrl = getImageUrl(posterImage),  
        releaseDate = releaseDate  
    )  
}  
  
private fun getImageUrl(posterImage: String) = "https://www.themoviedb.org/t/p/w500/${posterImage}"  
  
  
interface MovieRepository {  
    suspend fun getMovies(page: Int) : List<Movie>  
    suspend fun getMovie(movieId: Int) : Movie  
}  
  
internal class MovieRepositoryImpl(  
    private val remoteDataSource: RemoteDataSource  
) : MovieRepository {  
    override suspend fun getMovies(page: Int): List<Movie> {  
        return remoteDataSource.getMovies(page = page).results.map {  
            it.toMovie()  
        }  
    }  
  
    override suspend fun getMovie(movieId: Int): Movie {  
        return remoteDataSource.getMovie(movieId = movieId).toMovie()  
    }  
}
```
**Interface adapters** (controllers, viewmodels, interactors, presenters) — This layer is application-specific. We use them to change business models to application models which will be used by our views later. For example, we could store our entities (formatted, processed) in a database.

**UI, Views** — the last and the lowest level layer is responsible for presenting our data to the end user. Generally, we don’t write much code here. We only use this layer to communicate with other layers of our circle.

`**data/**`: This folder contains all the implementation details of the application's data layer. It is further divided into:

- `**datasources/**`: This folder contains the implementation of data sources, which can be either remote or local. For example, an API client to communicate with a backend server can be a remote data source, while a local database can be a local data source.
- `**repositories/**`: This folder contains the implementation of repositories, which act as a single source of truth for the data. Repositories provide an abstraction over the data sources and handle data retrieval and storage.
- `**models/**`: This folder contains the implementation of data models, which are used to represent the data entities of the application.

`**domain/**`: This folder contains the implementation of the application's domain layer. The **Domain** layer will contain our **core business rules** (entity) and **application-specific business rules** (use cases). It is further divided into:

1. **Entities** (main data holders)
2. **Repository** interface definition (communication with datasources)

1. **Use cases** (core business logic of app)

- `**entities/**`: This folder contains the implementation of domain entities, which represent the real-world objects of the application. Entities should be independent of any specific implementation detail.
- `**repositories/**`: we need interface definition for our repository and that is all we need, the rest will be done on the **data layer**.
- `**usecases/**`: This folder contains the implementation of use cases, which define the business logic of the application. Use cases depend on the domain entities and the repository interfaces.

`**domain layer completely independent**`

It fetches and saves the data on various data sources, it must depend upon the **data layer**, right? Well, we want for **data layer** to depend upon the **domain layer**, the **domain layer** must not have **ANY** dependencies. That is why a repository interface is defined on the **domain layer** and its implementation is written on the **data layer.** That is called a **Dependency Inversion Principle**.

`**presentation/**`: This folder contains the implementation of the application's presentation layer. It is further divided into:

- `**pages/**`: This folder contains the implementation of the pages or screens of the application.
- `**widgets/**`: This folder contains the implementation of reusable widgets that are used across different pages or screens.
- `**blocs/providers**`: This folder contains the implementation of BLoCs (Business Logic Components) or providers, which are responsible for managing the state of the application. BLoCs/providers depend on the use cases and provide the necessary data to the pages or screens.
- `**utils/**`: This folder contains helper classes or functions that are used across the presentation layer.

`**injection_container.dart**`: This file contains the dependency injection setup for the application. It defines how the different components of the application should be created and wired together.

# **Either**

And if we want to return a failure case we would wrap it up in a function called left:

return left(UsersListFailure(error: ex.toString()));

Now if we want to return our list / model of data from function, we would simply wrap it up in a function called right from the fpdart package, something like this:

return right(list.map((e) => UserJson.fromJson(e).toDomain()).toList());

**Class DataSource no abstract class**

```dart
class AuthenticationRepository {  
final FirebaseAuth _firebaseAuth;  
final GoogleSignIn _googleSignIn;  
  
AuthenticationRepository(this._firebaseAuth, this._googleSignIn);  
  
Future<UserCredential> createUserWithEmailAndPassword(  
String email, String password) async {  
return await _firebaseAuth.createUserWithEmailAndPassword(  
email: email, password: password);  
}  
}  
  
await injector  
.get<AuthenticationRepository>()  
.createUserWithEmailAndPassword(enter input, enter password);
```

**Best coding structure style**

Document, Comment, Detail add why change

```kotlin
import 'package:freezed_annotation/freezed_annotation.dart';  
  
import '../../core/const/const.dart';  
  
part 'login_input.freezed.dart';  
part 'login_input.g.dart';  
  
/// [mobile] - [JsonKeyConstant.mobileJsonParamKey] Enter the mobile number  
/// [password] - [JsonKeyConstant.passwordJsonParamKey] Enter the password  
/// [deviceId] - [JsonKeyConstant.deviceIdJsonParamKey] Get the device id from mobile  
/// [firebaseToken] - [JsonKeyConstant.firebaseTokenJsonParamKey] Get the firebase token from Firebase  
  
@Freezed(copyWith: false, equal: false)  
class LoginInput with _$LoginInput {  
@JsonSerializable(fieldRename: FieldRename.snake, explicitToJson: true)  
factory LoginInput(  
{@JsonKey(name: JsonKeyConstant.mobileJsonParamKey) required String mobile,  
@JsonKey(name: JsonKeyConstant.passwordJsonParamKey) required String password,  
@JsonKey(name: JsonKeyConstant.deviceIdJsonParamKey) String? deviceId,  
@JsonKey(name: JsonKeyConstant.firebaseTokenJsonParamKey)  
String? firebaseToken}) = _LoginInput;  
  
factory LoginInput.fromJson(Map<String, dynamic> json) =>  
_$LoginInputFromJson(json);  
}
```
**Step new API integrate in Clean architecture**
```
1) input parameter (Domain)  
- equatable  
- generated freezed file, serialization  
2) Entity create (Data - Domain)  
- equatable  
- generated freezed file, serialization  
3) Mapper create (Data)  
4) Repositories create (Domain)  
5) api name add (Core)  
6) RemoteDataSource abstract method create and implement  
7) (Domain) repositories implement (Data) repositories  
8) Usecase create (Domain)  
9) Cubit crate / GetX Controller (Controller, Binding) / Riverpod  
- generated freezed class  
10) UI Create
```
