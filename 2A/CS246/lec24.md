# CS246

## Lecture 24 - Exception safety, how virtual works

#### C++ Guarantee: during stack unwinding, all stack allocated data is destroyed

DO NOT let dtors throw an exception. This can lead to multiple simultaneously live exceptions.

**RAII:** Resource Acquisition is initialization. 
Every resource should be wrapped ina stack allocated object whose job it is to release that resource.

What do we do about dynamic memory? 
C++ 03 provides a template class ```auto_ptr```. 
- ctor appends to dynamic memory
- dtor will call ```delete``` on the underlying ptr
- smart pointers are awesome

If you have two that are pointing to the same thing, they will 

```cpp
{ 
	auto_ptr<myclass> p ( new myClass );
	auto_ptr<myclass> q = p;
}
```

FINAL: assignment operator and operator= STEAL the field of RHS so that you can't pass it as const in order to set the RHS pointer to NULL

The c++ 11 version of this is ```unique_ptr```. It also has ```shared_ptr``` which uses reference counting so only the last one will delete it.

#### Levels of exception safety FINAL

1. Basic guarentee
 - if an exception occurs, the program continues to be in a valid state: no memory leaks, no dangling pointers
2. Strong guarentee
 - if an exception occurs while function *f* is called, it is like the call to *f* was never called.
3. No throw guarentee
 - function always succeeds. always.

```cpp
class A{...};
class B{...};
class C{
	A a;
	B b;
	void f(){
		a.g(); // these two give strong guarentee
		b.h();
	}
};
```

To go about solving these, start at the no throw and go down from there. If there are *non-local side effect (print to screen, launch rocket)* then it is donzeroni. If you assume that g & h only have local side effects.

To enforce the strong guarentee, use pointers to temporary variables.

```cpp
struct CImpl{
	A a;
	B b;
};

class C{
	auto_ptr<CImpl> pImpl;
	void f(){
		auto_ptr<CImpl> temp( new CImpl(*pImpl) );
		temp->a.g();
		temp->b.h();
		std::swap( pImpl, temp );
	}
};
```

#### How virtual works

Function call:
- loads the address of the memory containing the code
- jump to that address

Virtual method:
- Compiler creates a vtable
- the cost behind virtual is that you have to store the vptr and calling requires dereferencing the pointer
