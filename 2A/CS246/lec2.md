# CS246

## Lecture 2 - Directories

#### Current Directory
*The directory currently sitting in*. This can be found using the ```$> pwd``` command. As well, you can change directory using ```$> cd $ABOSLUTE PATH```

A relative path is one that is built upon the current directory; it is a path relative to the current directory. pwd + relative path = absolute path

#### Special Directories
1. . <- current directory
2. .. <- parent directory
3. ../../ <- grandparent directory
4. ~ <- tilde
5. ~userID <- goes to the root directory of whatever userID's home directory is.

As well you can just type ```$> cd ``` to go to the home directory. 

#### Listing Commands
*Displays content of the directory except for hidden files (files starting with a '.')*

Apparently, the extension in unix DGAF about the file extension. So a valid file could be foo.bar.hello.world

#### Wildcard matching
You can use REGEX from within commands to match things together. It is called a **globbing pattern**.

Was made called "glob" and did it all in the shell

#### >$ echo
*Prints out exactly what it sees*.

To confirm what the echo does, print ```$> echo *.txt``` and it will show you what all the globbing patterns will do.

To specify a string, use double or single quotes. Also, ot escape a character, use the ```'\'``` before.
** ON THE MIDTERM ** *"Single and double quotes will prevent the expansion of globbing patterns"*

#### Other commands

```$> cat /usr/share/dict/words``` is the dictionary. ```cat``` will print out stuff. ```$> cat``` will output whatever you type as a string literal, and just echo it. This is useful for capturing output to different files or programs.

The ```'>'``` character means take the output of the first command into the second command. For example, ```$> cat > output.txt``` will take any output and move it to the input of output.txt. As well, ```'>>'``` will append to the file rather than overwriting it. This is the equivalent of output redirection, and then you can use ```'<'``` for input redirection.

```CTRL+D``` is used to tell the program that no more input is expected. It generates a signal called eof to the input stream. It is a way to tell a program that no more input is expected.

Every unix process comes with 3 streams: stdin, stdout, stderr. To redirect stderr, use ```>>```
