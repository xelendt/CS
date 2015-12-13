# CS246

## Lecture 22: Big Three, Casting

#### Last time

```cpp 
Book* bp1 = new TextBook();
Book* bp2 = new Textbook();
*bp1 = *bp2;
```

This does partial assignment, which only does *partial assignment*, where is calls the parent's copy ctor.

One solution is to make the assignment operator virtual. That means somewhere in the code, the base class's assignment operator is virtual and the sub-class overrides the base class's assignment op.

```cpp

class Book{
	virtual Book& operator=( const Book& );
};

class TextBook: public Book{
	Textbook &operator=(const Book&);
};
```
This creates a mixed assignment problem.

To solve the problem there is a **recommendation** to always make the base class of a hierarchy abstract.

Here is an example of a better implementation:

```cpp
class AbstractBook{
	string title, author;
	int numPages;
	protected:
		AbstractBook &operator=(const AbstractBook&);
};

class NormalBook: public AbstractBook{
	public:
	NormalBook &operator=(const NormalBook& other ){
		AbstractBook::operator=(other);
		return *this;
	}
};
```

This prevents partial assignment because it prevents the assignment of base class pointers.

#### Casting

There are 4 different types of casts:
1. static_cast
	- ```static_cast<Typename>( myVar )```
	- this works on primitive types
2. const_cast
	- ```const_cast<Typename>( myVar )``` 
	- used for using libraries that aren't const correct
	- if the library call changed myVar, the behaviour is undefined
	- const correctness trickles down through your code
3. reinterpret_cast
	- ```reinterpret_cast<Typename>(&myVar)```
	- there is no restriction on what you can/cannot do
	- the compiler will not be angry, but it will be defined based on the compiler you are using. It just grabs whatever information is at that address
	- can bypass private/protected 
4. dynamic_cast
	- ```dynamic_cast<Typename>( myVar);
	- using a polymorphic array
	- To use dynamic cast, the hierarchy must have at least one virtual method
	- RTTI: Runtime Type Information, get the typename at runtime
