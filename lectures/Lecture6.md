Lecture 6:  ASTROPY
===================


## Updating your *astr288p* repo 

As always, update your git repo. If you modified your notebooks, you will notice some conflicts.
Is there a better solution to this?
```
   cd ~/ASTR288P/astr288p      # make sure you are in one of the 'astr288p' directories
   git status                  # notice something was modified?
   git pull                    # warnings are possible here if there are conflicts
   git stash                   # those modified files are "stashed"
   git pull                    # now get the updates
```

One possible option is to always work on your notebooks in a backup:
```
   git pull
   cp -a notebooks notebooks-trials    # copy to a trials tree
   jupiter notebook                    # work in the notebooks-trials
```   

Another option is to work in a git branch:
```
   git branch trials                   # create a new branch
   git branch                          # see which branches you have
   git branch -r                       # or which branches are on the remote
   git checkout trials                 # go to the new branch
   jupiter notebooks                   # work in the current notebooks (branch)

   
   git checkout master                 # go back to the master version
   git pull                            # get the official updates
```

## testing your modules in python

A new pure-python script was added to the ```notebooks``` directory to identify potential problems
before you start a notebook (although some of them are on purpose):

```
cd astr288p/notebooks
./testing.py
```

## ASTROPY

A community Python Library...

### Official references

* Home page:   http://www.astropy.org/
* Affiliated packages:  http://www.astropy.org/affiliated/
* Developers (git) : http://docs.astropy.org/en/stable/development/workflow/development_workflow.html



### Astronomical Data


* Images:  FITS files.  (a new file **ngc6503.cube.fits** was added to your astr288p/data directory)
  * ds9: http://ds9.si.edu/site/Download.html
  * ginga: https://ginga.readthedocs.io/en/latest/
  
* Tables  (astropy http://docs.astropy.org/en/stable/io/unified.html)
  * ascii tables
  * FITS tables
  * VO tables
* 


### Reminder on installing software in python:

Various ways, in increasing complexity and varying degrees of success:

* conda
```
	conda install ginga
```
* pip
```
	pip install ginga
```
* source
```
	git clone https://github.com/ejeschke/ginga.git
	cd ginga
	python setup.py install
```

## Today's notebooks:

* **n6503-case1** : analyzing the new ngc6503.cube.fits using astropy
* **n6503-case2** : analyzing the new ngc6503.cube.fits using radio-astro-tools (experimental)
* **n6503-orbits** : theoretical models what to expect of a galactic velocity field

