Lecture 3:  UNIX
================


## Updating your *astr288p* repo
Any time you need to update your **astr288p** git repo, the **git pull** command will do this:
```
   cd ~/ASTR288P/astr288p      # make sure you are in one of the 'astr288p' directories
   git status                  # first make  sure you don't have anything modified
   git pull                    # warnings are possible here if there are conflicts
```
it would actually warn you if you had modified files that are also modified on the server. It will
attempt a merge and warn you.  Files that you modified and are not modified on the server

## UNIX PATH

Any command typed in the terminal will find this from an executable file along the
directories in the $PATH environment variable:

```
   echo $PATH
   
   which ls
   which man
   which ds9
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
   

## PYTHON

The python language often comes natively on your UNIX system.
Try the following commands in **ipython** (or **python** if you don't have **ipython** yet):
```
   LAPTOP> which python
   LAPTOP> which ipython
   LAPTOP> ipython
   In [1]:  import numpy
   In [2]:  import scipy
   In [3]:  import astropy
   In [4]:  import astroML
   In [5]:  import admit
   In [6]:  quit
```
At some point you might see the message **no module named**.


   
## Anaconda and Miniconda

**Miniconda** is a very barebones version of python which you can then tailor to your own needs. See also
http://conda.pydata.org/miniconda.html.
If you need more, download the full **Anaconda** version. With this you also get a nice graphical install.
See https://www.continuum.io

### On Linux:
```
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh 
  bash Miniconda3-latest-Linux-x86_64.sh
```
### On Mac:
```
  curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > Miniconda3-latest-MacOSX-x86_64.sh 
  bash Miniconda3-latest-MacOSX-x86_64.sh
```
and now in common to both Linux and Mac you will answer some questions and at the end
a modification to your **~/.bashrc** file will be made.
```
  export PATH="$HOME/miniconda3/bin:$PATH"
```
And now make sure your shell is looking at this new python (e.g. **source ~/.bashrc** for your current shell, or open a new shell):
```
  which python
```
Now continue installing some modules that we will need for future lectures
```
  conda install ipython numpy scipy matplotlib notebook ipywidgets networkx
  conda install astropy
  conda install jupyter

```

See what modules you have installed:
```
  conda list
```


### Hello World! in python

```
	echo 'print("Hello World!")' > hello.py
	python hello.py
```	

Following on our previous **"#!"** example we can avoid having to type the name **python** :
```
	#! /usr/bin/python
	#
	print("Hello World!")
```
or even more general
```
	#! /usr/bin/env python
	#
	print("Hello World!")
```

### plotting example
Previously we created a small dataset **Data2.txt** in the **ASTR288P** directory. This is how it should plot
on your screen

```
	astr288p/python/tabplot.py Data2.txt
```


### C compiler hello world

```
	cat hello.c

#include <stdio.h>

void main() 
{
  printf("Hello World from C!\n");
}

	gcc -o helloc hello.c
	ls -l hello.c
	ls -l helloc
	helloc
	more helloc
	cat helloc

```

Q1:  cut and paste the C code into your own hello.c and compile and run this program

Q2:  observe the difference between **more** and **cat**
