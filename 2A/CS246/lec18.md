# CS246

## Lecture 18 - Design Patterns, Observer, Decorator, Factory
( I don't like OOP very much )

#### Observer
You have 2 types of people:
- Publisher/Subject - generates data
- Subscriber/Observer - consumes data

If you have a class that doesn't do anything, you want it to be ```abstract```. It has no data of its own, as well, it should be abstract. By making the destructor pure virtual, it makes it abstract. This is good because for each child class, it will have its own data which it has to delete.
Since you have no objects on an abstract class, you need no dtor!

We go back and change the definition of *pure virtual*. Previously it only meant it had no implementation, as you are allowed to do so. In the case of a dtor, you must implement it though!
A pure virtual method must be implemented by a subclass to be considered concrete.

#### Decorator
Adds to a pre-existing object

We have a base class which is an abstract class.


#### Factory Method Pattern

Works by creating things to allow for clearer code in the main loops. 

This works well for singletons.


#### CODE EXAMPLES
check under SE on the 
