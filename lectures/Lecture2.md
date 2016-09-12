Lecture 2:  UNIX
================

Command Line unix vs. desktop unix (Graphical User Interface)
  - GUI: a dime a dozen (and new ones keep coming...)
  - GUI: Mac (aqua) and Linux (X11)
  - GUI: Linux has many many window managers
         (twm, fvwm, enlightenment, gnome, kde, unity, plasma)
  - GUI: Linux is changing from using X11 to Wayland
  - CLI: one and only one (minor differences do remain between Mac and Linux)

The notes below loosely follow the tutorials in
    http://www.ee.surrey.ac.uk/Teaching/Unix/

Login shell in a terminal:  ("chicken or egg")
  - xterm
  - Gnome Terminal
  - emacs "M-x shell"

Shell options (as defined in /etc/passwd, see /etc/shells)    [does MacOS obey this?]
  - bash  (sh: bourne shell)
  - tcsh  (csh: C-shell)
  - ksh   (korn shell)
  - xonsh (pythonesque shell, cf. ipython)

   Q1: how do you know which shell you are running

   A1: echo $SHELL
       grep $USER /etc/passwd 
       ps

   Q2: What are the allowed shells on your unix system
   
   A2: cat /etc/shells


Persistent shells with session management (cf. VNC)
  - screen
  - tmux

bash:
  - interactive vs. login shell
  - login:
	/etc/profile
	~/.bash_profile
	~/.bash_login
	~/.profile
  - interactive
        /etc/bash.bashrc
	~/.bashrc

  Some of your personal files may already 


Files and Directories - Part 1:

  ls                  LiSt files
  pwd                 Print Working Directory
  whoami              Isn't that obvious?


How to get more help:
  COMMAND --help
  COMMAND --version
  man COMMAND
  info COMMAND

  which COMMAND
  whatis COMMAND
  apropos COMMAND
  <google>

  Q1: man pages have sections (the -s option) to narrow down search

Files:  the "ls" command

  ls -l
  ls -al
  ls -lt
  ls -ltr
  ls -lt | tac
  ls --full-time

  Q1:  what is the | symbol do

  Q2:  what is the 'tac' command?

  Q3:  what is all this "." and ".."


Directories:

  pwd
  mkdir ASTR288P
  cd ASTR288P            (try typing just 'A' or "AS" and then <TAB>-complete)
  pwd

git: sharing your codes, a first encounter

  git clone https://github.com/teuben/astr288p
  cd astr288p
  ls
  less astr288p/lectures/Lecture2.txt

    

 Files:   finding files
 
  https://www.howtoforge.com/tutorial/linux-search-files-from-the-terminal/

  1) 'locate'    (but:   "sudo updatedb")

     
  find . -name "*poster*"




VNC:

ssh teuben288@ursa.astro.umd.edu

only once to start/stop:
     vncserver -geometry 1600x900
     	       (controlled by ~/.vnc/xstartup )
     	       New 'ursa.astro.umd.edu:1 (teuben288)' desktop is ursa.astro.umd.edu:1
     vncserver -kill :1


vncviewer ursa.astro.umd.edu:1
