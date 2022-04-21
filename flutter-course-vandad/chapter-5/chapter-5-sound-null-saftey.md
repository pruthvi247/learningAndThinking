## Intro to dart

1. Const age=27 -> "age" variable is compiletime constant 
2. final age ; -> "age" vairable is kind of runtime constant which can be initialised later
3. String? name = null;
	1. name = "myname" -> some times it can be string , some time it can be null
4. List< String>? names = ['foo','bar'] -> List itself can be null (names=null;)
	1. 1. names =['foo','bar',null] -> will throw error
	2. List<String?> names = ['foo','bar',null] ->This works , here we are telling the list of objects can be optional null
	3. List<String?>? names;
		1. This can be names = null;
		2. This also can be names = [ 'foo','bar'];
		3. This is also valid names = ['foo','bar',null];
5. Null aware assignment operator:
	1.  name ??= "someName" (Check if name is null, if yes then assign the value on right)
	2.  name = firstName ?? secondName ?? lastName
6. Conditional invocation:
	1. List< String>? names = null
		1. names.length -> will throw error
		2. names?.length -> Will work, its like , if names is not null then invoke length
		3. len= names?.length ?? 0;
7. cadcac
8. 
	






