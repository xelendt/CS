# CS246

## Lecture 13: The big three 

#### Free midterm marks 
- Question on preprocessor
- Shell script, similar to runsuite
- Write 2 constructors
- Write copy constructor
- Attempt due date q1, q2 for prep

#### Copy constructor

Copy constructor is used to construct a new object as a copy of an existing object.
You get a copy constructor for free.
Every class comes with 4 things -> default ctor ( goes away once you write your own ctor ), a copy ctor, destructor, copy assignment operator.

For a class 'C', the copy constructor takes one parameter ```( const C& )```

**Example (mimics the default copy ctor):**
```cpp
struct Student{
	int assigns, midterm, final;
	Student( const Student &other ) // or const Student &rhs for right hand side
		: assigns( other.assigns )
		, midterm( other.midterm )
		, final( other.final )
	{
	}
}
```
It is performed when ```Student bobby = billy;```. It is initialization if you create a new object.
 - ```bobby = billy;``` -> assignment
 - ```Student bobby = billy; // short hand for Student bobby(billy)``` -> copy

**Example:**
```cpp
struct Node{
	int data;
	Node* next;
	Node( int data, Node* next )
		: data( data )
		, next( next )
	{
	}
	Node( const Node &other )
		: data ( other.data )
		, next ( other.next )
	{
	}
}

// now we can create a linked list on the heap and copy it 
Node *np = new Node( 1, new Node( 2, new Node( 3, NULL ))); 
Node m = *np; // this calls the copy constructor
// to do in the heap:
Node *npCopy = new Node( *np );
```
When you do this, you create two new heads of the linked list with the same tail. This is called a **shallow copy**. What we want is 3 *independent* copies, or we want a **deep copy**
We want the deep copy when an object contains fields that are dynamically allocated.

**Custom implementaion for deep copy for Node class**
```cpp
sruct Node{
	int data;
	Node* next;
	Node( const Node& other )
	{
		this->data = other.data;
		if( other.next == NULL )
		{
			this->next == NULL;
		}
		else
		{	
			// we want to send the object
			// this calls the copy ctor recursively
			this->next = new Node( *other.next ); 
		}
	}
}
```
If we want to write it nicely:
```cpp
struct Node{
	// this uses ternary operators within the MIL, you can't have if or else there
	// this can also be found on the sample files
	Node( const Node& other )
		: data( other.data )
		, next( (other.next) ? new Node( *(other.next) ) : NULL )
	{
	}
}
```
Places where copy ctor is used:
1. creating an object as a opy of another -> ```Node m = n;```
2. when an object is passed by value, the copy ctor is called
3. whenever an object is returned, it copies from the funciton's stack frame to the other stack frame

Why must the parameter be a const reference? Because when you do pass by value, you must invoke the copy constructor, which is what you are trying to define!

#### Single Parameter constructors
```cpp
struct Node{
	Node( int data ) : data( data ),
		next( NULL )
	{}
	void foo( Node n )
	{}
}

Node m = 4;
```
This will compile and run, the ```4``` will be sent to the single parameter consrtuctor.
Similarly, you can say, ```foo(4)``` and it will pass it to the proper place. Single parameter constructors create implicit conversions.

A good example for this is a string: ```std::string str = "hello";``` and this gives an implicit conversion from ```char*``` to ```std::string```. 

The **explicit** keyword disables the automatic conversion using the single parameter constructors.

#### Destructor
When an object is destroyed, a special method called the destructor runs.

A stack allocated object is destroyed when it goes out of scope. A heap allocated object is detroyed when it is deleted.

A class only has 1, zero parameter destructor. Again, like the ctor, there is no specified return type. You call the destructor as well by invoking ```~``` as a unary operator.

A default destructor calls the default destructor for all fields that are objects.

The same sort of problem exists with the destructor as the copy constructor with the deep/shallow copy. If you write your own ctor, then you bettwe write your own dtor

**Example for node**
```cpp
struct Node{
	int data;
	Node *next;
	~Node(){
		delete next;
	}
}
```
This isn't as simple, you can't keep calling because eventually it will cause stack overflow. The other interesting question is to delete for a circular linked list.

If you ever dynamically allocate memory within an object, it is your job to destroy that memory too. Calling deletion on NULL is safe.

#### Separate Compilation
*Recall*, ```.h``` files include type definitions, and ```.cc``` file includes the function implementations.

In the header, include method prototypes, and they are inside a class. Now, the ```.cc``` files have also method implementations as well.

You can use the scope resolution operator (```::```) to tell the compiler it is a method rather than a function.
It is one of the operators you cannot overload. It tells you it is inside that class, as a method.
**Example:**
```cpp
int Node::getData()
```
The return type always occurs before the declaration. 

*Note:* Never use ```using namespace Node```. This will cause ambiguity and actually isn't allowed for the compiler.
*Note:* You must also implement all of the methods so you don't have as much dependencies.

#### Assignment operator

```cpp 
Student bobby( billy ); 	// copy ctor
Student jane;				// default ctor
jane = billy;				// assignment operator
```
It is called to update an existing object to a copy of an existing object.
