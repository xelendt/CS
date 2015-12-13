# CS246 

## Lecture 5: Shell Scripts - Testing

#### Recall example from last class

**Example:** Answer whether a given word is a good password, yes or no

```
#!/bin/bash
# Returns whether the password given was good

egrep "^${1}$" /usr/share/dict/words > /dev/null # this is a black hole to throw away

if[ $? -eq 0 ]; then
	echo "Not a good password!"
else
	echo "Maybe a good password..."
fi
```

```$#``` gives the number of arguments to a script. 
A good example to add the previous script is to add a feature where you can check to see if the usage is correct:

```
usage () {
	echo "Usage: $0 password" #reminder: the $0 is the name of the script, the first argument
	exit 1
}

#calls a function
if [ ${#} -ne 1]; then
	usage
fi
```

To **call a function**, simply write the function as is with the arguments space delimited.

#### While loops

**Example:** print form 1 to $1

```
x = 1
while [ ${x} -le $1 ]; do #le is less than or equal to
	echo ${x}
	x = $((x+1))
done
```

As well, using ```1>&2``` changes the stdout to the stderr??

One way to run the script is ```./count 2> err.log```. This is a way to redirect the stderr and write to the ```err.log``` file.

#### For loops

**Example:** Rename all .C files to .cc

```$> mv hello.C hello.cc``` in essence moves the file ```hello.C``` to ```hello.cc``` and essentially renames it. 
Script to do that (*based assignment question*)

```
file = hello.C
mv ${file} ${file%C}cc
```

The ```%C``` cuts out the ```C``` at the end of the file name. 
So ```%``` followed by a suffix will remove that suffix from the end of the variable, and ```#``` will remove from a sufix.

**For loop syntax**

```
for name in *.C; do 
	mv ${name} ${name%C}cc
done
```

*Cool thing* look at how to change the delimiter type, for example to read a csv
Unfortunately, it can all be done in one line.

**Example:** How many times does $1 appear in file $2?

```
x = 0
for word in (cat "$2"); do
	if [ ${word} = "${1}" ]; then
		x = $((x + 1))
	fi
done
echo ${x}
```

#### Other functions

```$> cal``` will give the calendar as a month.
Then, say if you want the last Friday of the month, use ```$>cal | awk '{print $6}' | egrep [0-9] | tail -1```

All of the cool important scirpts can be found in the /files folder.

#### Testing
In a2 to a4, we will get a bunch of test cases we have to write.

There are different types of testing:
- Black box testing 
	- writing tests before coding 
- Functional testing
	- tests features
	- edge cases: boundaries of a range

#### Marking for a2 to a4
The way you create test files, you make t1.in, the input, and t1.out, which will be the output.

Due date 1:

public test: correct solutions

private tests: buggy1, buggy2. It should happen that one of the test that the bug will be triggered. Therefore the output of the first correct one that will be wrong. If the output is different, you catch that bug.

secret tests: superbugs!! You need to actually need to think about the test cases.

Due date 2:

This time, we need to give our own correct solution. If you come up with some exotic bug, then you can still fail.
