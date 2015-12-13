# CS246

## Lecture 20 - Visitor Design Pattern, Compilation Dependencies

#### Visitor

What if we want to have a situation where we want to design a dynamic dispatch on methods but also parameters.

```cpp
class Enemy{
public:
	virtual void strike( weapon &w ) = 0;
};

class Turtle: public Enemy{
public:
	void strike( weapon &w ){
		w.useOn( *this );		// at compile time, it will be known to be a turtle
	}
};

// we want this because we need different implementations for each type
class Weapon{
public:
	virtual void useOn( Turtle *t ) = 0;
	virtual void useOn( Bullet *b ) = 0;
};
```

*"Using the visitor design pattern to achieve double dispatch"*

Basing our choice of method to execute on the runtime of 2 pointers.

**Separation of concern** is when the there are two things that don't really relate to each other. There is in a sense no separation of concerns.

We can "prep" the class to accept Visitors.

```cpp
class Book{
public:
	virtual void accept( bookVisitor &b ){
		v.visit( *this );
	}
}
```

Forward declaring classes: just put a line with ```class className;```. Use this to avoid includes -> also makes the compiler go faster.
