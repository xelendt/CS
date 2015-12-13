# CS246

## Midterm review session 27/10/15

#### Building ctors for a binary tree

```cpp
struct BinTree{
	int data;
	BinTree *left, *right;

	// default ctor
	// there is occasionally some start-up logic, but this is dope 'nuf
#define MIL
#ifdef MIL
	BinTree()
		: data( 0 )
		, left( NULL )
		, right( NULL )
	{
	}
#else
	BinTree()
	{
		left = NULL;
		right = NULL;
		data = 0;
	}
#endif

	// copy ctor
#define TERNARY
	BinTree( const BinTree &rhs )
		: data( rhs.data )
#ifdef TERNARY
		, left( rhs.left ? new BinTree( *rhs.left ) : NULL ) // calls the copy ctor
		, right ( rhs.right ? new BinTree( *rhs.right ) : NULL )
#else
	{
		if( rhs.left == 0) 
		{
			left = 0;
		}
		else
		{
			left = new BinTree( rhs.left );
		}
		if( rhs.right == 0) 
		{
			right = 0;
		}
		else
		{
			right = new BinTree( rhs.right );
		}
	}
#endif
	
}

// operator overloading
// operators should cascade, and that is why the return type is ostream&
// if you aren't returning something from the operator, you need 
ostream &operator<<( ostream &os, const BinTree& b) 
{
	os << b.data;
	if( b.left != NULL )
	{
		os << b.left;
	}
	if( b.right != NULL )
	{
		os << b.right;
	}
	return os;
}
```

### Why MIL?
 - const references
 	- ```const int i = 5;```, the i cannot be changed
	- ```int &i = v; i = 5```, you change v
	- you can think of a T& ~~ T* const

### Copy ctor notes
 - deep copy /vs/ shallow copy
 	- shallow copy will not copy dynamically allocated stuff, default copy ctor is shallow
	- deep copy will also copy the children to the new object
	- strategy is to field for field, figure out whether you can just copy directly, or whether you need to go deeper. 
 - the general goal is to have all the new data living in a new place in memory to the old one
 - the pattern of recursion for the copy ctor will follow the same pattern as the other functions for that data structure; it is simply a traversal

### Struct notes
 - when you have a function within a struct, the first parameter is the struct itself ( just like in python )

### Buck Fash Scripting
We want to go through the directory and find files that are out of date, and then we want to compile the entire program.
 - filter .cc files
 - check if .out exists
 - last modified check
 - compile if needed
 - compile whole thing

Input specification
```./compile myprog file1.cc file2.cc file3.cc```

Script
```
#!/bin/bash
if ![ $# -ge 2 ]; then
	echo "ERROR" > &2
	exit 2
fi

prog = $1
shift #shift all the things over, eliminating the first variable. now all further files is what you want to compile

# HARD STUFF GOES HERE
# only compile if older
# -ot is older than 
for file in $@ #review $@, cannot have quotations, or else will iterate over 1 file, "$@"
	if [ "${file%cco}" -ot "$file" ]; then # review the truncation
		g++ -c file #compile only, don't link
	fi
done

if [ $? -ne 0 ]; then
	exit 1;
fi

g++ *.o -o $prog
echo "Complete!"
```
If there are spaces in the file names, then that will break, shouldn't have to solve on the midterm! woo!

### fstream review
This will just read a single integer from the file. You can use cin.fail() or cin.eof() if you want to check stuff
```cpp
#include <fstream>
int main() {
	fstream foo( "foo.txt" ); // or you can use str.c_str() if str is a std::string. The funciton takes a C-Style string
	int i;
	foo >> i;
}
```

### g++
things to know ```-o, -DVAR, -c, -W```

### Other practice
 - references and pointers, write up some practice programs
 - write down shit even if you don't know anything, it will get you some marks, as long as it's not wrong lol
