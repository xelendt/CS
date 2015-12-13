# CS246

## Lecture 4 - Permissions/Variables/Shell scripts

#### File Permissions

```ls -l``` <- Long listing

```-rwxrw-r-- 	1		nanaeem		staff	123		date	abc.txt```
- file permissions
  - 0th: type, most often used for directory
  - first 3: user bits, owner's permissions
  - next 3: group bits, given to all users within the 
  - last 3: all other users, given to people *not* in the group
  - r = read, w = wrtie, x = execute
- links
- owner
- group 
- filesize
- last modified
- filename

| permission | Ordinary file 	| Directory			|
|------------|------------------|-------------------|
| r			 | read contents eg. cat    | see contents, globbing, tab completion  	|
| w 		 | write contents |	add/remove files | 
| x | Run the file as a program | navigate into directory |

#### Changing Permissions
The owner is the only one, aside from admin, who can change file permissions.
There is no other permission that the owner can give to other people that lets them change permissions.
However, the owner can always change permissions no matter what permissions are on the file.

Command: ```$> chmod <mode>```.
Describing the mode:
- ownership class
  - ```u``` user
  - ```g``` group
  - ```o``` others
  - ```a``` all
- operator
  - ```+``` add
  - ```-``` remove
  - ```=``` set exactly
- permission
  - ```r``` read
  - ```w``` write 
  - ```x``` execute

**Example:** Give others read permission -> ```$> chmod o+r $FILE``` 

**Example:** Revoke exec permission from group -> ```$> chmod g-x $FILE```

**Example:** Make everyone's permission rw -> ```$> chmod a=rw $FILE```

It can also be done in binary (*voodoo hacker*) -> ```$> chmod 644 $FILE```. Each number in there is a binary for rwx.

#### Shell Variables
```$> x=1``` -> This will create a variable of value 1, but the value is a string. They are local to the current session. 

To print out values, use ```$> echo $x```, but it is good practice to use ```${x}``` to properly dereference it.

**NOTE** there needs to be an absence of spaces. This is because otherwise, it would look for a program called x with the parameters called ```x``` with parameters ```=``` and ```1```.

So there is a special variable called ```${PATH}```. So when there is a program called, like ```ls```, it will search, not through your entire directories, but only through your ```${PATH}```

#### Shell scripts
Scripts are text files that contain linux commands executed as a program

Format of a good shell script:

```
#!/bin/bash			#hashbang/shebang line
pwd
whoami
date
```

To run the script, use ```./$SCRIPTNAME```. Before doing so, however, you must set the execute bit.

To create a script with command line arguments, when you run the script, add parameters:

```
./script arg1 arg2 arg3
^ $0 	 ^ $1 ^ $2 ^ $3 
```

The ```shift``` function will shift the ```$2``` to ```$1```. It is nice to use when you are looping over lists of parameters because having them hardcoded is sometimes really bad.

---

**Example:** Check whether a given word is in the dictionary. Usage: ```./isItAWord word```

```
#!/bin/bash
egrep "^${1}$" /usr/share/dict/words
```

---

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
All programs return a status code. 0 is success, non-zero for failure. This smart because there is only 1 way to succeed, thus 0, and then there can be a number of ways in which the program can fail.
grep has status code 0 if grep has any matches, and will set 1 if there are no matches.

For usage of if statements, use Google, dimwit. Also, you need to use ```fi``` at the end.
