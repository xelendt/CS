# CS246

## Lecture 19 - Template Method Pattern, C++ Templates

#### Template pattern

If there are any things that can be generalized, they can be put in a base class. 

**Example:**
```cpp

class Turtle: public Animal
{
public:
	void draw(){
		this->drawHead();
		this->drawShell();
		this->drawTail();
	}
private:
	void drawHead(){ ... }
	void drawTail(){ ... }
	virtual void drawShell() = 0;
}

class Red: public Turtle{
	void drawShell(){
		// draw specifics for the subclass
	}
}
```

#### C++ Templates

These are the most useful things in the world.

A *template* class is a generalization by parameterizing a class on one or more types.
This can also be done for functions.

**Example:**
```cpp
template <typename T>
class Node{
	T data;
	Node<T>* next;
public:
	Node( T data, Node<T>* next ){ ... }
	T getData() const{ return data; }
}

// to create
Node<int>* intList = new Node<int>(2, new Node<int>(3, NULL ) );
Node<char>* intList = new Node<char>('a', new Node<char>('b', NULL ) );
```

Terminology: *Specializing a template*

Need to have ```Node< Node<int> > *listOfLists``` in C++ 03.

#### Standard Template Library (STL)

A godsend.

Can be split up into template classes, iterators and functions.

Most useful classes:
 - ```std::vector<T>```. When doing random access, you can do *no range checked* where you do ```myVector[i]``` versus ```v.at(i)``` which is *range checked*. the ```at()``` method will check at runtime that the value at ```i``` will raise an exception if it tries to access outside of the bounds of the array.
	- To iterate over a vector, use the following
	```cpp
	for( vector<int>::iterator it = v.begin(); i != v.end(); ++it ){
		// access ith element, dereference the iterator
		cout << *it << endl;
	}
	```
	- To reverse iterator
	```cpp
	for( vector<int>::reverse_iterator it = v.rbegin(); it != v.rend(); ++it ){
		cout << *it << endl;
	}
	```
 - ```std::map<KEYTPE, DATA>``` is a generalization of the array where instead of having an ```int``` key, it can be anything
 - to use these, include ```<map>``` and ```<vector>```
