# CS246

## Final review session

#### Working with classes

Premise:

```
class BinTree{
	int data;
	BinTree *left, *right;
}

class BinTreeI: BinTree{
	int data;
}

class BinTreeS: BinTree{
	std::string data;
}
```

How to make the equals operator:

```
BinTree &BinTree::operator=( const BinTree &other ){
	if( &other == this ){
		return *this;
	}
	// ...
	left = other.left ? new BinTree( other.left ): 0;

	return left;
}
```

If there is an exception that is thrown, it will return an exception to the stack frame above it and so on and so forth until it is caught. If it is not caught the program will terminate with a non-zero exit status.
One important thing to remember is that destructors will still be called when the stack frame is exited by stack unwinding.

There is something called Resrouce Allocation Is Initialization. This means that something on the stack should always be responsible for the heap allocated memory. The best way to do this is using smart pointers, ```auto_ptr``` means the memory belongs to the pointer and will be deleted automatically whenever it goes out of scope.

#### Exception guarentees

- No-throw: I promise not to throw any exceptions
- Strong: Either it works or it throws an exception, not both
- Basic: Data still make sense and is safe
- No guarentee: lazy, nothing

Going back to the equals operator, you delete the stuff before assigning it. Currently, it has no guarentee. To modify it so that it has basic guarentee, what you do is delay the delete by making a temporary variable: ```BTree tmpl = left;``` and then delete temp after.

```
//...
try{
	tmp2 = ... ? new ... : ... ;
}
catch( ... ){
	delete tmp;
	throw;
}
//...
```

You also might want to do copy and swap instead.

#### Mixed/Partial assignment

Just learn it.

#### Casting

Like don't.

#### Design Patterns

- ask you to describe it
- ask you to code it
- ask you what someone else does
