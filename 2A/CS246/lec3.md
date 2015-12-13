# CS246

## Lecture 3 - pipes, grep

#### Review

stdin -> prog 	-> stdout
				-> stderr

Stdout is buffered, stderr is not buffered. Since drawing to the console is expensive, there is a buffer that only draws to screen occasionally. Therefore, it will have improved performance. Stderr is used if you want to have no delay.

#### Pipes

**Example:** need the how many words occur in the first 10 lines in the file sample.txt. A useful command is ```$> head -10 sample.txt``` and that will return the first 10 lines. *For more info on head, ```$> man head```*. Instead of creating a temporary file, you can use a linux pipe ```$> prog1 | prog2```. Piping connects the output of stdout of the first program to the stdin of the second program. Therefore, with pipes, the problem can easily be solved using ```$> head -10 sample.txt | wc -w```. Any collection of commands strung together using pipes is called a pipeline.Therefore, with pipes, the problem can easily be solved using ```$> head -10 sample.txt | wc -w```. 

#### Uniq and sort
**Example:** Suppose files ```words.txt``` and ```words2.txt``` contain a list of words, 1 per line. Print a duplicate free list of words from both files. 

There is a command called ```sort``` and ```unique``` that do exactly what you think they would do. Therefore, to solve the problem at hand, use the command ```$> cat words*.txt | sort | uniq ```. There is also a parameter to remove the duplicates on the sort command.

#### Inserting commands into plain text
So for example, you want to do ```$> echo Today is date and I am whoami```. You can do this by adding back ticks ```$> echo `date` and `whoami` ``` or by using ```$> echo $(date)```. The ```date``` function returns the date while the ```whoami``` will give the name of the current user.

Now, you can wrap the argument within double quotes ```""```, and it will do all the commands and then send the one argument to echo. **MIDTERM** single quotes won't work in this case, however. It is a good habit to get into using double quotes always.

#### grep
The version we will be using is egrep (*extended global regular expression pattern*).

**Usage**: The usage is generally ```$> egrep pattern file```. 

**Output**: Prints every line in file that contains the pattern.

useful grep args:
- ```-i``` is case insensitive
- ```-n``` is print the line number

#### Using regex
To match a special character, escape is using a ```'\'``` except within a ```[]``` where characters do not have special meaning.

You can also do ```$> grep "^cs246"``` and that will match the pattern only if it is at the start of the line, ```$> grep "cs246$"``` to find the lines that end in cs246. Used in conjunction, find the lines with only cs 246.
