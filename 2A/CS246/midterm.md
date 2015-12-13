# CS246

## Review for the midterm

The [course notes](https://www.student.cs.uwaterloo.ca/~cs246/current/notes.pdf)can be found.

## Shell

###### Linux file system

The *Linux Shell* is the way users can talk to the operating system. All OS come with a graphical shell, which is usually an intuitive interface controlled by the mouse.
As well, there is a command-line shell, which lets you type in commands. This, for us, is bash.

The Linux file system is split into a tree structure of files and directories etc. 

Directories are considered as files, but they are just files that are capable of "containing" other files. 
Ordinary files are not directories. 
To view this structure, you can type "tree /path/to/directory" in bash on linux.

A file is considered "hidden" if its name begins with a ```'.'``` and will not be visible to a normal ```ls``` or to the graphical file folder system.


###### Special Directories

The base is called the root directory. 
An **absolute path** is the location of a file starting at the root directory. 
From this, using an absolute path, any sort of file can be located on the operating system.
The **relative** path is how to get from one directory to another directory.
Another way of saying the absolute path is that it is the relative path from the root directory.
To instantly access the root directory, you can use ```~```. For example, from any directory, you can type ```~/path/to/my/directory``` and get there, since the ```~``` gives access to an absolute path.

Another special directory is ```..```, which is equivalent to the directory above the current directory. 
This is very common for relative paths when you have to backtrack up and then move to a different branch. 
There is no ```..``` directory from root since it is the "root" of the tree.

**Example:** relative path from ```xelendt/CS/blob/master/2A/CS246/``` to ```xelendt/CS/blob/master/1A/CS137``` would be ```../../1A/CS137``` since we want to backtrack up two directories, and then down the ```1A/CS137``` branch.


###### Commands

If you want any more in depth information about any functions, you can use ```man myCommand``` and it will come up with a page that shows all of the documentation for that command.

 - ```cd``` stands for *"change directory"*. It will move your current directory to the specified directory.
 - ```pwd``` stands for *"present working directory"*. It will output to the command line the absolute path of your current directory which you are sitting in.
 - ```ls``` is short for *"listing"* (jk I don't actually know). Either way, it will give you a list of the files in the current directory. 
You can also call a ```ls /path/to/directory/``` and it will give the ```ls``` as if you were in that directory.
We should be at least kinda familiar with some of the functionality of this:
 	- ```-l``` will give you an in-depth list, so the permissions and date updated etc.
	- ```-r``` will give the list in reverse
	- ```-t``` will give the list in chronological order, starting with the newest
	- ```-a``` will display hidden files
 - ```echo``` will print out whatever you ask it to print out. SINGLE AND DOUBLE QUOTES WILL PREVENT THE EXPANSION OF GLOBBING PATTERNS! (know this)
 - ```rm``` will remove a file from a directory. Be careful, you have been warned.

###### Globbing patterns/ReGeX
Globbing patterns, more commonly known as Regular Expressions, or regex. There are a list of things that will make regex your best friend, but most likely, it will be your worst nightmare.
 - ```?``` 		is zero or one occurrences
 - ```*``` 		is zero or more occurrences
 - ```+``` 		is one or more occurrences
 - ```^``` 		indicates the start of a line
 - ```$``` 		indicates the end of a line
 - ```\s``` 	is white space
 - ```\d``` 	is a digit
 - ```{3}``` 	exactly 3
 - ```{3,}``` 	3 or more
 - ```{3,5}``` 	between 3 and 5, so 3, 4 or 5
 - ```.``` 		indicates any character, *except* for newline \n
 - ```(a|b)``` 	indicates a or b
 - ```(...)```	indicates a group
 - ```[abc]``` 	indicates a range, so it could be a, b or c
 - ```[^abc]```	not a, b or c
 - ```[a-q]``` 	lower case letters from a to q
 - ```[A-Q]``` 	upper case letters from a to q
 - ```[0-7]``` 	digits from 0 to 7

That should be it for the death. So the only way to get comfortable with tis is to practice.
You either see it or you don't. There is some funky ass interactions between ```()``` versus ```[]```, since they mean two completely different things.

Globbing patterns can be used pretty much in every command.

###### cat
```cat``` is a program similar to ```echo``` in which it prints out the contents of the file at hand, but it does so in a different way.
Instead of simply printing a string, it will expand whatever it receives in the command line before outputting it.
It is particularly useful in capturing the output of the programs, and for using globbing patterns.

If ```cat``` is run with no auxiliary parameters, then it is assumed that it will receive input from stdin and the user will need to to provide input. To specify the eof, the user gives a ```CTRL+D``` command to let it know that no more input is expected.

###### IO redirection
Every unix process comes with 3 streams: ```stdin```, ```stdout```, ```stderr```. Here is how to redirect:
 - *Input redirection:* ```program1 < program2``` will give the input from program2 to program1
 - *Output redirection:* ```program1 > program2``` will give the output from program1 to program2
 - *Error logging (not real name):* ```program1 2> program2``` will output the stderr to program2, or using ```2>```.

When using the redirection, you can use the ```1>&2``` or whatnot to redirect stdout to stderr. ```1``` means stdout and ```2``` means stderr, os when you use ```1>```, you redirect the stdout to wherever.

###### Pipes
Using a pipe will automatically redirect the output of a program to the input of the next program:
```
program1 | program2
```

###### egrep
egrep will search for patterns. The output is the lines with the successful matches. The matches can be from any point in the line, so it will also do sub-words.
Usage: ```$> egrep pattern source```, where the source is the input, default set to the current directory. You can change this to any file/directory as well.

###### File Permissions(chmod)
To view the file permissions, you can use ```ls -l``` and it will bring it up in a 10 character string, each character represents some type of permission. 

There are 3 types of permissions that exist: read, write and execute.  
 - read, you can read the file, for example, pressing tab to autocomplete a directory listing
 - write, you can write to the file, for directory, this is adding/removing files
 - execute, you can run the file, for directory, this is navigating to the directory
 - if you do not have any of these permissions, it will appear as ```-```

As well, there are different classes of ownership:
 - user, the person who owns the file
 - group, who knows
 - other, everyone else

In general, never allow 'other' users to read/write your files

Therefore these 3 types and 3 classes of ownership make up 9 characters + 1 character to determine whether it is a directory:

```
d rwx rwx rwx
```

The order for this is user, group, other.
You can change the permissions to a certain file using ```chmod``` command. There are specifications you can give it, or just use number for binary, since you either have permission or you don't.
- ownership class
 - ```u``` user
 - ```g``` group
 - ```o``` others
 - ```a``` all
- operator
 - ```+``` add
 - ```-``` remove
 - ```=``` set exactly
- permission
 - ```r``` read
 - ```w``` write
 - ```x``` execute

**Example:** Give others read permission ```$>chmod o+r /path/to/file```.
*(Voodoo hacker mode)* ```$>chmod 644 /path/to/file```.

## Shell Script
Scripts are text files that contain linux commands that can be executed as a program.

Format of a good shell script:

```
#!/bin/bash		#hashbang/shebang line
pwd 
whoami
date
```

The hashbang line is informing that it is a bash script? To run the script, you simply use ```./scriptname```. Before doing so, you must set the executable bit.

###### Shell variables ($PATH)
You can initialize variables within your own session! ```$>x=1``` will create a variable with value 1, but the value is a string, and is local to your session.
You can then ```$>echo $x```, and it will print that value. As well, you can use ```${x}``` to properly dereference it.
There *NEEDS* to be an absence of spaces in order for it to run properly, or else it will look for a program called ```x``` with parameters ```=``` and ```1```.

There is a special variable called ```${PATH}```, and it is the current directory. 
For example, ```ls```, if given no parameters will do a ```ls ${PATH}```, and find the files in the current directory.

*NOTE:* these notes could have incorrect implementation/spacing

###### Command line arguments to a script
```
./script arg1 arg2 arg3
^ $0	 ^ $1 ^ $2 ^ $3
```
Within the script, the arguments can be accessed like so. The ```shift``` function will move ```$2``` to ```$1```, etc... 

######  $?, /dev/null, $0
- ```$?``` is the status code of the last command.
- ```$@``` is all of the arguments passed into the script 
- ```$0``` at the beginning is the name of the script
- ```$#``` will give the number of args
- ```/dev/null``` will throw everything away that is written into it. It is good if you want to ignore some sort of input

###### script functions
To define a function, use ```myfunc(){  }``` and the code goes in the block. The parameters are the same as how arguments work for calling a script -> ```$1``` and so on.

**Example:**
```
usage() {
	echo $1
}

usage "b0ss ples"
```

###### if statements
```
if [ a -eq b ]; then
	functionCall arg1 arg2
fi
```

There need to be spaces everywhere, and as well for the equality comparison, there are a ton of those things, and they are intuitive. (```-ge```, ```-le```, ```-ot``` (older than) )

###### while loop
```
while [ $x -le $1 ]; do
	echo $x
	x=$((x+1))
done
```

###### for loop
This is classic for loop, iterate through stuff, and is a lot like python.

```bash
for word in (cat "$2"); do
	if [ ${word} = "${1}" ]; then
		x=$((x+1))
	fi
done
```

###### testing
There are different types of testing:
 - Black box testing
 	- writing tests before coding, don't know why
 - Functional testing
 	- tests features
	- checks edge cases and corner cases

## C++ 
###### Hello, World!
```cpp
#include <iostream>

using namespace std;

int main( int argc, char* argv[] )
{
	cout << "Hello, World!" << endl;
	return 0;
}
```

###### Compiling/Executing C++ programs
The best compiler is the gnu compiler collection. For C++, the compiler is g++.

```
g++ *.cc -o prog
```

Then you can run ```./prog``` to run your program.

Other options for g++:
 - ```-o``` output
 - ```-c``` compile with nothing else
 - ```-W``` with warnings
 - ```-Ep``` show what the preprocessor sees

There is an order to which the compilation is done to create an executable:
1. C++ preprocessor
 - implements all elements in the preprocessor and creates a set of temporary files
 - this can be printed on stdout if wanted
2. Compiler
 - who knows
 - generates assembler file for next step (```.s``` file) 
3. Assembler
 - generates object file (```.o```)
4. Linker
 - brings in object code for library funcitons
 - outputs the executable

This [process](http://faculty.cs.niu.edu/~mcmahon/CS241/Notes/compile.html) can be read up upon if you don't understand it.

###### Stream objects(cin, cout, cerr)
```cpp
#include <iostream>
#include <fstream>
#include <sstream>
```
With these, you can do a lot of stuff with these:
 - ```std::cin``` reads from the stdin
 - ```std::cout``` outputs to the screen
 - ```istringstream``` will input things to strings
 - ```ostringstream``` will output things to strings
 - ```ifstream```/```ofstream``` will read to files

You can use the streams to convert from string to integers:

```cpp
#include <iostream> 
#include <string>
#include <sstream>
using namespace std;

int main () {
	int n;
	while (true) {
		cout << "Enter a number:" << endl;
		string s;
		if( !(cin>>s) )
		{
			break;
		}

		istringstream ss(s);

		if( ss >> n )
		{
			break;
		}
		cout << "That was not a number!" << endl;
	}
	cout << "You entered " << n << endl;
}
```

###### IO Operators( >>, << )
These are operators that act upon either input or output streams:
 - ``>>`` think of the arrows as pushing the data towards the arrow. So, for these, the lhs is the istream, the rhs is the value to be read into. This returns a reference to a istream, so that cascading can run, so you can do ``` cin >> a >> b;```
 - ``<<`` is the same deal, but for ostream; you are pushing your variable to the ostream

**How to overload:**
```cpp
ostream& operator<<( ostream& os, const Student& s )
{
	os << s.grades << s.name;
	return os;
}
```

###### semantics of reading from cin, cin.fail(), cin.eof()
 - ```cin.fail()``` returns true if one of the following holds:
 	- the entered value does not fit the variable
	- the variable will not be affected
	- the istream is broken
	- the entered value is still in the buffer and will be used for the next ```cin>>variable```
	
	To fix this, you need to either
	- repair the istream using cin.clear()
	- clear the buffer using some funky cin.ignore( Some param )
 - ```cin.eof()``` will occur when there is no more expected input
 	- eof character
	- ```CTRL + D```

###### std::string
*std::string is not the same as c-style string*

In C++, the string is a class, so not just an array of characters. To convert from a std::string to a C-Style string, you use ```somestr.c_str()```. 

There are some methods we should have a general knowledge of:
 - concat. To concatenate two strings, you can use the ```+``` operator on the strings as there is an operator overloaded for concatenation.
 - ```std::string.length()```. This returns the length of the string. Can also be ```str.size()```.
 - comparison. There is a funciton ```strcmp( str1, str2 )``` that performs to see if the pointers in str1 and str2 are greater or less than each other. If they are the same, it will return 0. This is how to do it for cstrings. There is also ```str1.compare( str2 )```. This will return for lexigraphical comparison. It is <0 if str2 is all lower and all previous match and is shorter, >0 if str2 is all greater or longer and all previous match.

###### IO manipulators: hex, dec, showpoint, setprecision, boolalpha, header, <iomanip>
 - octal (%o) | show integral values in octal
 - dec (%d) | show integral values in decimal
 - hex (%x) | show integral values in hex
 - left/right (default) | values with padding before/after values
 - boolalpha / noboolalpha (default) | bool values as false/true or 0/1
 - showbase / noshowbase (default) | values with or without prefix, like 0x for hex
 - showpoint / noshowpoint (default) | print decimal points if no fraction
 - fixed (default) / scientific | e10 or naw
 - setfill('ch') | padding character before or after
 - setw( w ) | NEXT VALUE ONLY in minimum W columns
 - setprecision( p ) | fraction point precision
 - endl | flush output buffer and show new line
 - skipws( default ) / noskipws | skip whitespace characters

###### Stream abstraction for files
You can also, not using input redirection, have srteams that read files. All of the implementation for these are available in: ```<fstream>```, ```<ifstream>``` and ```<ofstream>```.
The 'i' and 'o' stand for input and output respectively.

In C++, to open the stream, simply create an instance of an ```istream``` or ```ostream``` with the file name. 
Then, the stream closes when it goes out of scope, or ```someStream.close()``` is called.
As well, you can check if a stream is open using ```someStream.is_open()```.

###### Default arguments
A function can have default arguments, that will be assigned if there is no specified parameter.
To create a default parameter, assign it in the parameter fields in the function definition: 

```cpp
// print out a student, the default name is Fred.
void dumpStudent( int grade, string name = "Fred" )
{
	// do code
}

dumpStudent( 100 );
```

You need to have the most frequent to be omittied the last in your paramter list.

###### Function overloading
Function overloading happens when you have a function with the same name, and a different parameter list. For example, this is done a lot with construtors, when you have a default ctor and a copy ctor.

Syntax:

```cpp
void dumpStudent( int grade, int year, string name );
void dumpStudent( Student s );
```

[*Review*]
###### Declarations Before Use
A variable must be declared before it is used in a block. It must also be declared only once.

[*Review*]
###### Pointers
A pointer/reference is a memory address.

To dereference a pointer, use ```*p```, and you get the value. Pointers can not be assigned after declaration.

[*Review*]
###### Arrays
- Declare an array: ```int foo[5];```
- Initializing array: ```int foo[5] = { 1, 2, 3, 4, 5 };```
- Empty initialization: ```int bar[5] = { };
- Accessor: ```foo[index]``` returns a reference to the value at the index
- 2D Arrays: ```int foo[5][6]``` you can think of it as an array of arrays. This scales to Rn.

###### Structs in C++ versus in C
In C++, you can have functions in structs, but they are called *methods* within the struct. Same syntax as C

[*Review*]
###### Constants
In C++, you define something as constant ```const``` and there are a ton of subtleties. See [this page](duramecho.com/ComputerInformation/WhyHowCppConst.html) for a proper explanation.

[*Review*]
###### Pass by Value, pass by pointer
Pass by value is ```void func( T myVal )```, whereas pass by pointer/reference is ```void func( T* myVal )``` or ```void func( T& myVal )```.

| | Pros | Cons | 
|:--------------:| ----------------- | ------------------- |
| Pass by value | Good if you want to change the values in the new scope | Calls copy constructor, which can be expensive. Also is bad if you want to change your variable from the original scope.
| Pass by pointer | Does not call the copy constructor, pointers can be null | |
| Pass by reference |  Does not call copy ctor | cannot change the address |

###### References (shaky)
A reference is an address in memory. It is similar to a const pointer. As expected, you cannot assign memory addresses to different things, so references are non-mutable. References, however, do automatic dereferencing.

We should not have to know in depth what rvalues and lvalues are #BLESSED

###### Stack vs heap allocation
C++ manages its dynamic memory using ```new``` and ```delete```. Allocation has 3 steps:
1. determine size of allocation
2. allocate heap storage of correct size/alignment
3. coerce undefined storage to correct type

Lucky for us, the ```new``` operator will do all of this in one step!

For dynamic storage, everything is stored in the heap. Whereas in C, if the heap is full, ```malloc``` will return ```0```, in C++, ```new``` will terminate the program with an error.

Here are two examples, the first of a "basic" new and the second of an "array" new.

```cpp
int *pvar = new int;		// basic "new"
int *parr = new int[10]; 	// parr[] is an array, array "new"

delete pvar; 				// basic delete
delete []parr; 				// array delete
```

Stack allocation eliminates explicit storage-management and is more efficient than heap allocation. This is best used for primitives, and smaller structs.

###### C and C++ preprocessor
 - ```#include``` copy and paste. This will take whatever file is supposed to be included and then paste it on the line where the include is. This is generally done at the beginning of the program.
 - ```#define VAR VALUE``` search and replace. This will go through and find all instances of ```VAR``` and replace it with ```VALUE```. Typically, the variable name is all capitalized to avoid confusion and accidental overwriting of important things.
 - using ```#define``` for conditional compilation ( DEBUG ). There is logic that the preprocessor can do:
 	 - ```cpp
	 #if VALUE
	 #elif VALUE
	 #else
	 #endif
	 ```
	 - ```cpp
	 #ifdef VAR
	 #ifndef VAR
	 #endif
	 ```
	 This will check to see whether ```#define VAR VALUE``` has been done for that value
	 - A superb use of this is to have a line at the beginning of the program for ```#define DEBUG```, or using the ```-DDEBUG``` option in g++. Then, in your code, you can use ```#ifdef DEBUG``` and you can compile with debugging or without! Or, alternatively, you can use ```-DDEBUG="2"``` to assign it to a value using g++. You cannot have both g++ and ```#define``` define the same variable.

###### Separate Compilation
There are a couple of different file types supported by C++.
 - ```.h``` files: These are called header files, and they contain all of the declarations of functions, structs, methods and fields. These are always included and never compiled.
 - ```.cc``` (or ```.C``` or ```.cpp```, but we just use ```.cc```) contain all of the implementation for all of the functions, methods etc. These files are never included, and are the ones we compile.
 - For me, at least, a generic compile line would be ```g++ *.cc -o myProgramName```, where it compiles all of the ```.cc``` files are compiles and an executable is also generated.

###### C++ Classes
 - **What is a class** A class is a struct with functions inside of it.
 - **Distinction between functions and methods** Methods are in structs, functions are not
 - **Initializing objects** There are multiple ways of initializing objects using their different types of constructors.
 	- ```Student bobby( 60, 50, 30 );```
	- ```Student* bill = new Student( 50, 40, 10 );```
	- When you use a constructor with all default variables, and want to create an object using no parameters, you must simply do ```Student newguy;``` with no brackets, or else the compiler will think you are trying to make a function called "newguy" with return type of Student.
	- ```Student newguy = Student();``` would work.
 - **C Style init** ```Student s = {60, 70, 80};```. Once you have overwritten the default constructor, this will disappear (unsure).
 - **Ctors** Constructors are built in functions that will initialize objects.
 - **Built in 0 parameter ctor** There is a built in default ctor, which calls all default ctors on objects within the object being initialized. Pointers and primitives will therefore not be initialized.
 - **Steps occur when an object is created**
 	 1. Space is allocated (heap or stack).
	 2. Field initialization occurs, default ctor for fields that are objects are called.
	 3. Ctor body running.
 - **Member initialization list (MIL)** We look at the above steps and see that there is nowhere where we can initialize consts and references in here. Therefore a MIL is used. We squeeze this between step 2 and step 3:
 ```cpp
 template <typename T>
 struct Node{
	T data;
	Node* next;
	Node( Node* n )
	: data( n->data )
	, next( n->next )
	{
	}
 }
 ```
 - **Copy ctor** Will create a copy of the object that is an exact copy from the parameter.
 - **default ctor** The default ctor will call the default copy constructor for all fields. For pointers, it copies the exact same address. This is called a shallow copy, where none of the dynamically allocated memory will be copied over, only pointers to it.
 - **deep copy ctor** You need to create a copy of all the dynamically allocated memory! The recursive patterns will follow that of the data structure. See midtermSeshTuesday.md for notes on this, an example with a binary tree.
 - **when to use deep copy** Use deep copy when there is any sort of dynamic memory.
 - **places where a ctor is called** A ctor is called whenever an instance of an object is created. Copy constructors are called when returning and pass by value. This is why the parameters in the copy constructor must be const references, so it must not invoke the copy constructor.
