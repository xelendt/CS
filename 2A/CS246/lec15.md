# CS246

## Lecture 15 - const, static, Singleton Design Pattern, Encapsulation

#### const methods

```cpp
struct Student{
	int assgns,mt,final;
	mutable int numcalls; 
	float grade()
	{
		numcalls++;
		return assgn*0.4+mt*0.2+final*0.4;
	}

}

const Student billy(60, 70, 80);

billy.grade();
```

We see that ```Billy``` is a constant object, so we might run into a problem, because the method has access to all of the fields in the class.
To show that we won't change anything, we make a const method by putting const after the definiton. (```const``` applies to the thing on the left)
```const``` mehods are checked by the compilers so that they don't get assigned.

You can only call ```const``` methods on ```const``` objects.

```mutable``` fields can be changed by ```const``` methods, and can be assigned in ```const``` objects.

#### Static

It associates the field with the class and not with the object of the class.

This can be used for things such as knowing how many objects exist, so we keep a ```static``` count within the class.
When objects are instantiated, we must ask who is reserving the space for the ```static``` fields.
Therefore, ```static``` fields must be defined external to the type's definition.
When assigning it, you must also use the scope resolution operator:

```cpp
int Student::numObjects = 0;
```

**Static Member Functions**

They do not have access to the ```this``` pointer means you can't access any fields that are not static.

A static member function can only call other static member functions and access static fields.

```cpp

int main(){
	Student s1( --- );
	Student s2( --- );
	Student::printNumObjects();
}
```

The above code will print ```2``` because it is attached to the ```Student``` class.

#### Singleton design pattern
We have a class C, and we want our program to create only one object of this kind.

**Examples:** A logger, a wallet etc.

The ```<cstlib>``` has a function ```atexit``` which takes a pointer to a function as an argument.
- will run the registered function at exit
- multiple calls to ```atexit``` *stack up*, LIFO.
- good practice to push ```atexit``` right after creating a singleton

#### Encapsulation

- treat objects like black boxes (capsules)
- hide implementation

We want clients acess functionality using an exposed interface.

```cpp
Struct vec{
	Vec( int x, int y )
	{
	.
	.
	.
	}

	private:
		int x, y;
	public:
		Vec operator+( const Vec& v1 )
		{
			// private is access is to any code in the class
			// we have access to v1 x and y since it is inside the class
			Vec v( x + v1.x, y + v1.y );
			return v;
		}

}
```

We would rather have default visibility as ```private```, so they invented the ```class``` keyword.
A class invariant shoudl be maintained by your class at all times.

There are getters and setters that are good at supplying code invariants. This prvides flexibility to change implementation *eg: switching to polar coords*
