# CS246

## Tutorial - make

Examples are contained within ```/tutorials/tutorial9/make/```

#### What is a Makefile
Structure of a make file:

```
variables

all:
	commands
	commands
	commands
```

Anything that is tabbed is a rule, need a colon after the rule name.

```
variables

all: book.o
	commands
	commands
	commands

book.o:
	commands
	commands
```

```all``` is dependent on ```book.o```

If there is no rule present, it is just expected to exist in the directory.

It is intelligent where it only compiles where it needs to.

**make clean**

Usually, there are lots of random crappy files that we don't want.
```
variables

main: main.o book.o textbook.o ...
	g++ main.o ... main

main.o
	g++ -c main.cc
.
.
.

clean
	rm *.o main

.PHONY: clean
```

The ```.PHONY``` makes sure that you don't treat a string as a filename, but as a command instead.

**Using variables**

```CXX``` traditionally is the compiler
```CXXFLAGS``` traditionally is the compiler flags

```
CXX = g++
CXXFLAGS = -Wall -g

main: main.o book.o ...
	${CXX} ${CXXFLAGS} main.o ......

.
.
.
.

.PHONY: clean
clean:
	rm *.o main

```

gcc is rather smart in that it understands that a ```.o``` file needs to be compiled by ```CXX```.

Other common variables
- ```${EXEC}``` for the executable
- ```${OBJECTS}``` list of the object files
- ```${DEPENDS}```

``
CXX
CXXFLAGS = -Wall -MMD -g
EXEC = main
OBJECTS = main.o book.o ........
DEPENDS = ${OJBECTS:.o=.d}

-include: ${DEPEND}

.PHONY: clean

clean: 
	rm ${OJBECTS} ${EXEC} ${DEPENDS}
```

