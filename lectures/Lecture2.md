Lecture 2:  UNIX
================

Command Line unix vs. desktop unix (Graphical User Interface)
-------------------------------------------------------------
  - GUI: a dime a dozen (and new ones keep coming...)
  - GUI: Mac (aqua) and Linux (X11)
  - GUI: Linux has many many window managers
         (twm, fvwm, enlightenment, gnome, kde, unity, plasma)
  - GUI: Linux is changing from using X11 to Wayland
  - CLI: one and only one (though minor differences do remain between Mac and Linux)

The notes below loosely follow the tutorials in
    http://www.ee.surrey.ac.uk/Teaching/Unix/
you are recommended to walk yourself through these.

Login shell in a terminal:  ("chicken or egg")
----------------------------------------------
  - xterm                  (probably the oldest terminal in X11)
  - gnome-terminal         (Gnome Terminal)
  - xfce4-terminal         (XFCE4 terminal)
  - konsole                (KDE terminal)
  - emacs "M-x shell"      (yes, you can run a terminal inside of emacs)

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

  Some of your personal files may already be present when your account was activated. Use
  the **ls -a** command to see these hidden (files starting with a dot) files.

  Q1:  With the **ls -a** command you will also see **.** and **..**    what are those?

  A1:  The current directory **.** and the parent directory **..**


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
Many ways to view a file on the terminal:

     cat       
     more      ('q' to get out, '?' to get help)
     less      (/FOO   to search for the word FOO)
     tac       (reverses the lines)

     head
     tail

Extracting/Reducing files:
--------------------------

     wc        WordCount (and line and character) count
     sum       check sum (see also md5sum)
     grep      show lines that match some pattern (cf. google and googling)

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
Virtual Network Computing (VNC) allows you to run persistent graphical sessions to
a server and run a full windowing system on your local machine. 
```
     LAPTOP> ssh teuben288@ursa.astro.umd.edu
```
On the server (ursa) you need to only once  start/stop (and note with display it is using  (:1 in this example)):
```
     SERVER> vncserver -geometry 1600x900
     	       (controlled by ~/.vnc/xstartup )
     	       New 'ursa.astro.umd.edu:1 (teuben288)' desktop is ursa.astro.umd.edu:1
     SERVER> vncserver -kill :1
```     
then from any other client you will be able to connect to this server (implying multiple people can connect)
```
     LAPTOP> vncviewer ursa.astro.umd.edu:1
```
or if you are lucky on a mac, open this URL **vnc://ursa.astro.umd.edu:1** or from the Finder *"CMD + K"*


GRIP:
-----

GitHub Readme Instant Preview - allows you to preview your *MarkDown* files (README.md 
by default) in a web browser. These lecture notes are in md (*MarkDown*) format, simple
text files that are a lightweight markup language, and they format nicely in a web brosers.

Install and use it as follows
```
   sudo pip install grip
   grip Lecture2.md
```
