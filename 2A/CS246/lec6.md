# CS246

## Lecture 6: Testing example, C++ Intro and I/O
*Disclaimer: Worlds is on, notes might be sparse.*

#### Testing in assignments

If there is no output, then there is no issue with the test.

**The most important thing is to properly read the assignment.**

You also have to run the thing to update the input. ```pico $filename```. You must do this for ```.in``` and ```.out```

You can use ```./runSuite tests ./buggy1``` to test out the things.

You MUST update your tests file.

#### C++
Invented by Bjarne Stroustrup, used to work in AT&T labs. This is the same place where Unix and C were developed. He was playing around with Simula67, the first object oriented programming language. He took the same principles that Simula67 had and created "*C with classes*".

This class is in C++03.

Hello world in C++:

```cpp
#include <iostream>

using namespace std;

int main()
{
	cout << "Hello, World!" << endl;
	return 0;
}
```

To compile, run ```$> g++ <filename(s)> [-o <exec.name>]


