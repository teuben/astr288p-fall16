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
If you need more, download the full **Anaconda** version. See https://www.continuum.io

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

```


