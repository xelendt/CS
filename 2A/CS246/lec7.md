# CS246

## Lecture 7 - Who knows I got to class late

---

#### IO
If a read fails, then ```cin.fail()``` will return ```true```.
If however, a read fails because of an EOF, then ```cin.eof()``` will be ```true```.

*Interesting points*: There is an implicit conversion from ```istream``` to ```void*```

So the clasic ```if( cin >> n )``` means it will convert the ```n``` to a ```void*``` and make sure the value of it will be non-zero, iff ```cin.fail()``` is false.

Rather than being the bitshift operator, with ```>>``` the operator overloads from the bitshift operators to the input/output operators for streams.

When you use ```cin >> n >> m >> n```, you are *cascading* operators -> it evaluates to a ```cin```.

When you get a mismatched type, you must do a ```cin.clear()```, then ```cin.ignore```.

#### std::string
Remember, always using teh include is best practice.

There is a good function, ```getLine(cin, s)``` to grab the string line from the first non-white space character up until the next Newline.

#### files as input
Here is a program to read in all of the words from a file:

```cpp
#include <iostream>
#include <ftream>

int main() {
	ifstream file( "suite.txt" );
	std::string s;
	while( file >> s ){
		cout << s << endl;
	}
}
```

To close the file, just let the destructor be called once the thing goes out of scope.
