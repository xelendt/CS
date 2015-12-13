# CS246

## Lecture 11 - Preprocessor, separate compilation

#### Last time

```#include``` and ```#define VAR VALUE```

As well, running ```$>g++ -E -P file.cc``` to show what the preprocessor sends out

#### Conditional Compilation

For native windows applications, it needed a ```winMain``` function

For Linux, you need main.

They, you can use ```#if``` and ```#elif``` and ```#else``` and ```#endif``` to generate the conditionals. The issue with this is that you have to manually change the definition of the OS. There is a way to use command line args as preprocessor -> ```$> g++ [...] -DOS=Unix``` and it will give a define in the program.

You can just use ```#defime VAR``` to enable ```#ifdef``` and ```#ifndef```. 

**GOOD POINT:** you can you use a ```#ifdef DEBUG``` to enable debugging.

#### Separate compilation

Interface file ( header, .h )
 - type definitions
 - function headers

Implementation files ( source, .cc .cpp .C )
 - implementation of functions
 - standard convention is to put the main file into its own file

To compile multiple files: 
 - g++ *.cc
 - g++ main.cc vector.cc
 - never compile a ```.h``` file

The order g++ works in -> preprocessor -> compiler -> linker

The ```-c``` will only compile and not link. It will produce a ```.o``` file that contains:
 - compiled code
 - lists the NEEDS
 - lists the HAVES (definition)

The keyword ```extern``` tells that a global variable will be defined at some point.

Finally, include guards are based.
