# CS246

## Lecture 14 - Assignment Operator, methods vs functions, arrays of objects

#### Last time

```cpp 
Student billy( 60, 70, 80 );
Student jane;
jane = billy; // this is like jane.operator=(billy);
```

So the ```=``` operator is defined as a method.

#### Assignment operator

The assignment operator is right associated, so it starts by equalling the stuff on the right (rather than things like ```cin >> x > y``` being left associated).
The 
Return the ```&``` when you want to return something that already exists, but you don't want to create a new copy.

The copy constructor does not create a new object, but alters an existing one.

```cpp
Node &Node::operator=( const Node& other ){
	
	if( this==&other ) return this;

	data = other.data;
	delete next;
	next = other.next;
	return *this;

}
```

There is this thing called *self assignment*: ```*np = *np;```. In the above code, if we don't have the top part, we could delete itself!

When you use delete, it does not make it NULL, the semantics could be undefined. You never want to ask for memory you just deleted.

To get 6/6 on final exam, you need to have exception safe code:

```cpp
Node &Node::operator=( ... )
{
	if( this == &node ){ ... }
	Node *tmp = next;
	next = other.next .......;
	data = other.data;
	delete tmp;
	return *this;
}
```

#### Copy and swap Idiom

```cpp
void Node::swap( Node &other )
{
	int tdata = data;
	data = other.data;
	other.data = tdata;

	Node *tnext = next;
	next = other.next;
	other.next = tnext;

}

Node &Node::operator=( const Node &other )
{
	Node tmp = other; // calls copy constructor
	swap ( tmp );
	return *this;
}
// dtor for tmp is called when out of scope
```

This is another way to do assignment.

```cpp
// if you want to be fancy, make swap return Node&, and just return *this
Node &Node::operator=( Node other )
{
	return swap( other );
}
```

#### Rule of three
If you need to write a version of 
 - copy ctor
 - dtor
 - operator=

You usually should implement all three of them.

#### Overloading operators - functions vs methods
operator= must be implemented as a method
As well, the following must be methods:
 - operator[]
 - operator->
 - operatorT()
 - operator()

When an operator is implemented as a method, the "this" parameter is used to access the LHS.

```cpp
Vec Vec::operator+( const Vec &rhs )
{
	Vec v( x+rhs.x, y+rhs.y );
	return Vec;
}

Vec Vec::operator*( int &rhs )
{
	Vec v( x*k, y*k );
}

Vec v5 = 5*v4; // this does NOT work , cannot use 5.operator*( v4 );
```

Us, by making it a method, we only need to pass in one parameter. Notice, this is stack allocated.

As well, the left associativity is why you implement the input and output operators as functions, not methods -> so that you don't have to do ugly code.

#### Arrays of objects
To create an array, everything needs to have the objects initialized.
Options:
1. Provide a 0 param ctor that will get called automatically
2. Stack allocated array: array initialization. ```Vec vectors[3] = { Vec (1, 2), Vec(3, 4), Vec(5, 6) };```. This is usually good for smaller arrays.
3. Heap allocated: don't create an array, but create an array of pointers to objects.

To create an array of pointers to objects:
```cpp
Vec *vectors[0]; // stack allocated mem of vec*
Vec** vecs = new Vec*[num]; // dynamcally allocated

vecs[0] = new Vec( 1, 2 );

for( auto i: vecs ) // delete every element in i, this is c++ 11 crap lol
	delete i;
delete []vecs;
```
