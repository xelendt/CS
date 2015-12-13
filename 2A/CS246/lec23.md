# CS246

## Lecture 23 - Exceptions

Exceptions are thrown when a dynamic cast fails.

When an error occurs, an exception is raised/thrown.
- an unhandled exception will cause the program to terminate
- we need to catch the exception

There is a *try catch block* that will deal with exceptions: 

```cpp
// the catch 'catches' any error of a specified type raised in the try

try{
	cout << v.at(TOOBIG) << endl;
	cout << "donezo" endl;
}
catch( out_of_range r ){
	cerr << "BAD RANGE" << endl;
}

```

The *BAD RANGE* will be released into the cerr while *donezo* will not be printed.

You must have at least one catch for every try block, you can have multiple catches.

stack unwinding is the process of popping the call stack until a suitable handler is found for an error.

There is also inheritance on exceptions. So what you can do is protect as well against the subclasses. As well, you can throw more exceptions from within the catch. 

It is best practice to catch by reference rather than catch by value.

To catch all exceptions, in C++, there is the ```exception``` class which is base for all things, except for user defines exceptions.
To get ALL exceptions,

```cpp
try{

}
catch(...){

}
```

Exceptions are quite slow. Use them carefully. Don't throw primitive types. If you want, create an exception class.

**Common exceptions:**
- ```out_of_range: index out of bounds``` is most common on stl containers
- ```bad_alloc: call to new fails``` is when there is no more space on the heap
- ```bad_cast: dynamic_cast to reference fails``` 

We want to write exception safe code (exceptions should not cause memory leaks, dangling pts etc). 
C++ guarentee: during stack unwinding, all stack allocated data will be destroyed.
