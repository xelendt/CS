# CS246

## Lecture 1 - The linux shell

#### Linux Shell
The way to talk to the operating system is through a shell, it is the interface. It is how to tell the operating system to do whatever. 

All OS come with a **Graphical Shell**. It is typically controled using a mouse or keyboard. The big advantage is that it is intuitive to use. As soon as you try to do things that it is not designed to do, it becomes near impossible to do that.

**Command-line shell**: There is a screen in which you type in commands. It is not intuitive and there is a steep initial learning curve where you learn a handful of commands. Once you learn about 10-20 commands, they become building blocks and together can be super powerful.

#### History of Linux Shell
"The shell" was the original shell, and it was the only shell. It was made by Stephen Bourne. Other popular shells include:
- C Shell (tsch)
- Korn Shell

Eventually, updated Bourne Shell to the Bourne Again SHell (bash).

#### Linux file system
Tree structure comprised of files, directories etc.

Directories are considered files, but they just are capable of containing other files. Ordinary files are not directories.

To view the tree structure, type "tree $DIR" in bash on linux.

The base is called root directory. Absolute path is the location of a file starting from the root directory. Using the absolute path, any given file can be pinpointed.

**Homework:** look at what cd and pwd do
