# CS246

## Lecture 21: Compiler dependencies

#### Examples

- If you have a base class, you must include that file.
- If you have an instance of a class, the class must know how big it is, you must include that header file.
- If you have a pointer to the object, you only need to forward declaration because it only needs to know that it exists
	- once you call functions on pointers, you cannot get away with just a forward declaration
- If you only have a function, you only need to forward declare. In the header there is no compilation dependency, but it will be in the implementation file. This is because you never include ```cc``` files, so it is good to put it there.

EXAM: Given forward declaration preferred, give the first n lines of the code.

#### PImpl pattern

ANY change to window.h (even to private fields), require recompiling. 
Need to replace the implementation with a pointer to the implementation.

```cpp
struct XWindowImpl{
	Display* d;
	GC gc;
}; // windorimpl.h

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

struct XWindowIMpl;
class XWindow{
	XWindowImpl *pImpl;
public:
	//etc

}; // window.h
```

#### Low coupling + high cohesion
- code to a public interface
- friends - none
- no public fields

- interactions to work towards the same goal

#### Big 3 with inheritance
Destructor: 
 
- base class dtor is virtual. Then the subclass dtor automatically calls the base class dtor

Copy ctor:

- uses base class ctor
- then it can copy over other fields
- you can then access private things within its own class, so it is allowed to copy EXAM

Assignment op:

```cpp
Textbook& Textbook::operator=(const Textbook& other){
	Book::operator=(other);
	topic = other.topic;
	return *this;
}
```

To use the assignment operator through base class pointers:

```cpp 
Book* p1 = new Textbook( alsd, afds, a,sdf asdf, );
Book* p2 = new Textbook( addm, erf, erwcw, cwerwe );
*p1 = *p2;
```

This will only call the Book's ctor (*partial assignment*). To make it work, you cannot really make it virtual. If you do, you allow the rhs to be anything. This is *mixed assignment*.
