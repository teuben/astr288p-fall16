Lecture 2:  UNIX
================

Command Line unix vs. desktop unix (Graphical User Interface)
-------------------------------------------------------------
  - GUI: a dime a dozen (and new ones keep coming...)
  - GUI: Mac (aqua) and Linux (X11)
  - GUI: Linux has many many window managers
         (twm, fvwm, enlightenment, gnome, kde, unity, plasma)
  - GUI: Linux is changing from using X11 to Wayland
  - CLI: one and only one (minor differences do remain between Mac and Linux)

The notes below loosely follow the tutorials in
    http://www.ee.surrey.ac.uk/Teaching/Unix/

Login shell in a terminal:  ("chicken or egg")
----------------------------------------------
  - xterm
  - Gnome Terminal
  - emacs "M-x shell"

Shell options (as defined in /etc/passwd, see /etc/shells)    [does MacOS obey this?]
----------------------------------------------------------
  - bash  (sh: bourne shell)
  - tcsh  (csh: C-shell)
  - ksh   (korn shell)
  - xonsh (pythonesque shell, cf. ipython)

   Q1: how do you know which shell you are running

   A1: **echo $SHELL**
       **grep $USER /etc/passwd **
       **ps**

   Q2: What are the allowed shells on your unix system
   
   A2: cat /etc/shells


Persistent shells with session management (cf. VNC)
---------------------------------------------------
  - screen
  - tmux

bash:
-----
  - interactive vs. login shell
  - login:
	- /etc/profile
	- ~/.bash_profile
	- ~/.bash_login
	- ~/.profile
	
  - interactive
  
        - /etc/bash.bashrc
	- ~/.bashrc

  Some of your personal files may already be present


Files and Directories - Part 1:
-------------------------------
```
  ls                  LiSt files
  pwd                 Print Working Directory
  whoami              Isn't that obvious?
```

How to get more help:
---------------------
```
  COMMAND --help
  COMMAND --version
  man COMMAND
  info COMMAND

  which COMMAND
  whatis COMMAND
  apropos COMMAND
  <google>
```  

  Q1: man pages have sections (the -s option) to narrow down search

Files:  the "ls" command
------------------------
```
  ls -l
  ls -al
  ls -lt
  ls -ltr
  ls -lt | tac
  ls --full-time
```
  Q1:  what is the | symbol do

  Q2:  what is the 'tac' command?

  Q3:  what is all this "." and ".."


Directories:
------------
```
  pwd
  mkdir ASTR288P
  cd ASTR288P            (try typing just 'A' or "AS" and then <TAB>-complete)
  pwd
```

git: sharing your codes, a first encounter
------------------------------------------
```
  git clone https://github.com/teuben/astr288p
  ls
  cd astr288p
  pwd
  less lectures/Lecture2.txt
```

Creating Files:
---------------
```
  cd ~/ASTR288P
  mkdir Lecture2
  cp ASTR288P/lectures/Lecture2.txt .
```
  1) touch   (Zero Length file)
```
     touch Data0.txt
     mkdir data0.txt          (testing case sensitivity)
```
  2) echo
```
     echo Hello1   >  Data1.txt
     echo Hello2   >  Data1.txt
     echo Hello3  >>  Data1.txt
```
  3) cat
```
     cat > Data2.txt
     1 2 3
     2 3 5
     3 4 7
     ^D                       (a.k.a. EOF - ^C also works, but ^Z will confuse you)
     cat >> Data2.txt
     4 5 9
     5 6 12
     6 7 14
     ^D
```
  4) your favorite $EDITOR
```
     emacs     (C-x C-c)  or:   ^x^c
     vi        ( ':q!"  or "ZZ" to exit, the latter one also saves the file!!!)
     pico      (^X to exit)
     gedit     (^Q or ^W)
```
     Many editors keep a backup copy, often with a tilde (~) appended to the filename


Viewing Files:
--------------
     cat       
     more
     less
     tac

     head
     tail

Extracting/Reducing files:
--------------------------

     wc
     sum
     grep         

Other File Operations:
----------------------
     cp        CoPy files
     mv        MoVe files (also renaming if it's not going to another directory)
     rm        ReMove files
     ln        LiNk between files (symbolic/soft vs. hard link)


Scripting:
----------
     echo "echo hello world" > hello
     bash hello
     ls -l hello

     chmod +x hello
     ls -l hello	
     hello
     echo $PATH
     ./hello

 Finding files:
 --------------
   1) 'locate'    (but:   "sudo updatedb" - normally not enabled on Mac)

       locate -i poster

      
   2)  find       (arguably one of the more complex UNIX commands)
     
       find $HOME/Talks -name "*oster*"


Adding to your own PATH:
------------------------
    cd                        # move to your home directory
    mkdir bin                 # create
    cp astr288p/bin/*  bin
    echo $PATH                # check if ~/bin is already in your path
    lfind                     # check if the new 'lfind' is seen
    lfind lfind               # there should be two now !
    


VNC:
----
```
ssh teuben288@ursa.astro.umd.edu
```
only once to start/stop:
```
     vncserver -geometry 1600x900
     	       (controlled by ~/.vnc/xstartup )
     	       New 'ursa.astro.umd.edu:1 (teuben288)' desktop is ursa.astro.umd.edu:1
     vncserver -kill :1
```     

```
vncviewer ursa.astro.umd.edu:1
```
