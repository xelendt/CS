# CS246

## Lecture 12 - Closing remarks on separate compilation, C++ classes

#### Last time
file: vector.h
```cpp
#ifndef VECTOR_H
#define VECTOR_H

//code
//...
//...

#endif
```

This is called an **include guard**. All of the files are separately compiled, so if you don't use include shields, the code can be included by multiple files, causing it to fail compilation. 
If you *do* include it, then the first time the ```.h``` file is included, it will define ```FILENAME_H``` and then for every subsequent include, it will skip over the code because ```FILENAME_H``` is defined.

Other advice (lose marks by not taking advice!!):
- never include ```.cc``` files, they are for implementation
- never compile ```.h``` files
- never use ```cpp using namespace std;``` in ```.h``` files! If you do this, it will create a dependency on the ```std``` namespace. Since your header file uses ```std```, the person who includes it, means they cannot create their own ```string``` or ```cin``` variables. If the client wants to create their own string type, they cannot because it is already defined under the namespace. To avoid this *always* use the full name.

#### C++ classes
C++ really came into existence as *"C with classes"* and it was object oriented programming. The big idea is that you can **put functions within a struct**

**Example:**
```cpp
struct Student{
	int assignments, midterm, final;

	float grade(){
		return 0.4*assignments + 0.2* midterms + 0.4* final;
	}
}

Student s = {60, 70, 80};
s.grade();
```

**A class is a struct that can contain functions.** The difference is that in C, there cannot be functions within structs.
In C++, whenever you use a struct, it is really a class.

C++ does have a ```cpp class``` keyword, but that's going to be brought up maybe next week.

Notation:
 - An **instance** of a class is called an **object**
 - A function insid  a class is called a **member function** or a **method**
 - You call methods on object
 - A method has access to all the fields of the object on which the method was called.

The difference between functions & methods:
 - there is a hidden parameter ```this```. It is a pointer to the object on which the method was called.
 - ```this``` is good for when another variable with the same name as the field exists within the scope. Then ```this->field = field;``` is proper.

Below is the previous example using the ```this``` pointer.
```cpp
struct Student{
	int assignments, midterm, final;

	float grade(){
		return 0.4 this->assignments + 0.2 this->midterms + 0.4 this->final;
	}
}

Student s = {60, 70, 80};
s.grade();
```

#### Initializing Objects
When initializing with the C-style, ```Student s = {60, 70, 80};```, the parameters must have compile time constants

C++ Allows writing methods to construct objects - *constructors*
```cpp
struct Student{
	int assignments, midterm, final;
	
	Student( int assignments, int midterm, int final ){
		this->assignments = assignments;
		this->midterm = midterm;
		this->final = final; 
		// Note, you must use this-> or else assigning "assignments" will 
		// assign to the closest scope, which is the parameter not the field!
	}

}
```
*Note:* the name of the constructor must always be name of the struct

**Examples:**
```cpp
Student bobby( 60, 70, 80 );
istringstream SS( someStr );

Student *pbilly = new Student( 60, 70, 80 ); // initializes to the heap
//...
//...
//...
delete pbilly; // calls the opposite of constructor, the destructor ( will touch upon it later )
```

You can overload ctors and use default arguments in ctors (constructors), just like in functions:
```cpp
struct Student{
	int assignments, midterm, final;
	Student( int assignments = 0, int midterm = 0, int final = 0 ){
		// same as before
		this->assignments = assignments;
		this->midterm = midterm;
		this->final = final; 
	}
}
```
Using these defaults:
```cpp
Student billy( 60, 70 ); // missed the final, final = 0
Student jane( 60 ); // missed midterm and final, both 0
Student newguy; // if you use "Student newguy();" you get an warning because it looks like a function!
Student newguy = Student(); // it would work, but it is called value initialization
```
[Value initialization](http://en.cppreference.com/w/cpp/language/value_initialization) is hard, can read about it if you want...

Rules:
 - 1) Every class comes with a default ctor ( 0 parameters ). It calls defualt ctors on fields that are objects. For all of the variables below, x is a primitive (int), so it will not initialize, s is an object, so it will call the default ctor on that, and p is not an object, so it will not be initialized. Pointers and primitives will not be initialized. If you force value initialization, some of the primitives can be constructed, not recommended at the moment -> always initialize fields yourself.
  ```cpp
  struct A{
	int x;
	Student s;
	Student *p;
  }
  struct myA; // calling 0 parameter ctor
  ```
 - 2) As soon as you write any constructor, the default constructor is GONE. If you write any constructor, you lose C-style initialization as well.
  ```
  struct Vec{
  	int x, y;
	Vec( int x, int y ){
		this->x = x;
		this->y = y;
	}
  };
  Vec v; // won't compile -> "no 0 parameter constructor found"
  Vec v = {1, 2}; // won't compile -> no more C-style initialization
  ```

Suppose you have a class
```cpp
struct MyStruct
{
	const int myconst;
	int &myref; // int &ref = ... ; is called a field initializer 
}
```
C++ 03 disallows field initializers, can do in C++ 11. Not what you want to do anyways for most constants. 
C++ 03 also disallows consts and references in ctor body.
To figure out how to initialize consts and references, we must look at how an object is created:
 - space is allocated, could be stack or heap
 - field initialization occurs. default ctors for fields that are objects are called
 - ctor body running
Since step 3 is too late, we squeeze in the constant or reference initialization, we hijack step 2.

*New syntax:* Member initialization list ( MIL ). It is only available inside a constructor. 
```cpp
struct myStruct{
	const int myconst;
	int &myref;
	myStruct( int c, int &r ): 
		myconst( c )
		, myref ( r )
		, etc( otherVariable )
		, otherField( generalExpression ) // I am a hippy and put my commas on the line before so I don't forget them.
		// they can all be on one line if you want
	{

	}
};
```
Nice things:
 - constants and references can ONLY be initialized through MIL
 - MIL can be used for other types as well

```cpp
struct Student
{
	Student( int assignments, int midterm, int final ):
		assignments( assignments )
		, midterm( midterm )
		, final( final ) // the this pointer doesn't have to be used, the thing outside the brackets has to be a field!
	{
	}
};
```
Even if a MIL does not initialize a fiel that is an object, the default ctor from step 2 will still run. The fields in the MIL are initialized in declaration order, irrespective of the order in MIL. So the order in the parameters is what matters.
