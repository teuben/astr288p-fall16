Lecture 4:  PYTHON
==================


## Updating your *astr288p* repo

Always update your git repo for this class. New material is more than likely present every week.
```
   cd ~/ASTR288P/astr288p      # make sure you are in one of the 'astr288p' directories
   git status                  # first make  sure you don't have anything modified
   git pull                    # warnings are possible here if there are conflicts
```

## Python flavors

* python: the script interpreter

```
	python
```

* ipython: interactive python
```
	ipython
```	

* jupyter: web interface

```
	ipython notebook
	
```	


## UNIX SCRIPTS

recall: a UNIX script is nothing more than a few shell commands in a text file, which you can execute directly using
the shell (the interpreter). You do need to make that text file executable (**chmod +x**)

Recall from the previous lecture:
```
   echo echo hello world > hello
   chmod +x hello
   hello
```
Q1:  what happens if you left out the 2nd *echo* in the command that created the script?

Q2: the following shell commands do something very convoluted. How would you achive the same result?
```
   echo '#! /bin/bash' >> hello
   tac hello  > hello1
   mv hello1 hello
   chmod +x hello
```   
   
