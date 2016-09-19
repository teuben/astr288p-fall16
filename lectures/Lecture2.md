# Lecture 2:  UNIX

## Command Line unix vs. desktop unix (Graphical User Interface)

  - GUI: a dime a dozen (and new ones keep coming...)
  - GUI: Mac (aqua) and Linux (X11)
  - GUI: Linux has many many window managers
         (twm, fvwm, enlightenment, gnome, kde, unity, plasma)
  - GUI: Linux is changing from using X11 to Wayland
  - CLI: one and only one (though minor differences do remain between Mac and Linux)

The notes below loosely follow the tutorials in
    http://www.ee.surrey.ac.uk/Teaching/Unix/
you are recommended to walk yourself through these.

## Login shell in a terminal:  ("chicken or egg")
  - xterm                  (probably the oldest terminal in X11)
  - gnome-terminal         (Gnome Terminal)
  - xfce4-terminal         (XFCE4 terminal)
  - konsole                (KDE terminal)
  - emacs "M-x shell"      (yes, you can run a terminal inside of emacs)

## Shell options (as defined in /etc/passwd, see /etc/shells)
CAVEAT: MacOS does not seem to use /etc/passwd (see http://docstore.mik.ua/orelly/unix3/mac/ch03_08.htm)

  - bash  (sh: bourne shell)
  - tcsh  (csh: C-shell)
  - ksh   (korn shell)
  - xonsh (pythonesque shell, cf. ipython)

   Q1: how do you know which shell you are running

   A1: as is often in UNIX, several answers possible
	* **echo $SHELL**
	* **grep $USER /etc/passwd**
	* **ps**

   Q2: What are the allowed shells on your unix system
   
   A2: **cat /etc/shells**

   Q3: If a shell is not listed in **/etc/shells**, can I still use it

   A3: yes, simply run it from the current shell (a shell within a shell)


## Persistent shells with session management (cf. VNC)
If you don't need a full graphical interface, and still want to login to server (e.g. ursa) and maintain your session,
use any of the following programs

  - screen        (often comes with UNIX)
  - tmux          (and there are more)



## bash
We differentiate between an *interactive*  vs. *login* shell. 
   * login:
      * /etc/profile
      * ~/.bash_profile
      * ~/.bash_login
      * ~/.profile
   * interactive
     * /etc/bash.bashrc
     * ~/.bashrc

  Some of your personal files may already be present when your account was activated. Use
  the **ls -a** command to see these hidden (files starting with a dot) files.

  Q1:  With the **ls -a** command you will also see **.** and **..**    what are those?

  A1:  The current directory **.** and the parent directory **..**

### Mac and Linux philosophy on interactive and login shells


```
  linux>  ssh localhost                                 # login
  	  -> .bash_profile
  linux>  xterm (or open a gnome-terminal)              # interactice
  	  -> .bashrc

  mac> ssh localhost                                    # login (enable in System Preferences -> Sharing -> Remote Login)
       -> .bash_profile

  mac> Terminal  (CMD-N)                                # login
       -> .bash_profile                                 # if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
       bash                                             # interactive
       -> .bashrc 
```

If you use the **csh** variety, the **.login** and **.cshrc** files control which one is read for what type of session.

## Files and Directories - Part 1:

```
  ls                  LiSt files
  pwd                 Print Working Directory
  whoami              Isn't that obvious?
```

## How to get more help:

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

## Files:  the "ls" command

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


## Directories:

```
  pwd
  mkdir ASTR288P
  cd ASTR288P            (try typing just 'A' or "AS" and then <TAB>-complete)
  pwd
```

## git: sharing your codes: a first encounter

We will come back to **git**, but the following commands will download the "astr288p" repository of codes and documentation
that are helpful for this class.
```
  git clone https://github.com/teuben/astr288p
  ls
  cd astr288p
  pwd
  less lectures/Lecture2.md
```
This **Lecture2.md** file is the file you are reading now. Most humans can read it, but it does read a little nicer once it has
been formatted by a web browser, instead of straight to the terminal! Or you can read it directly on github on
https://github.com/teuben/astr288p/blob/master/lectures/Lecture2.md

## Creating Files:

Although it does not matter where you do this, let us keep files in **~/ASTR288P**:
```
  cd ~/ASTR288P
```
  1) **touch**   (Zero Length file)
```
     touch Data0.txt
     mkdir data0.txt          (testing case sensitivity)
```
  Notice on a Mac this last **mkdir** may have failed. Can you see why?
  
  2) **echo**
```
     echo Hello1   >  Data1.txt
     echo Hello2   >  Data1.txt
     echo Hello3  >>  Data1.txt
```
  3) **cat**
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
  4) your favorite **$EDITOR**
```
     emacs     (C-x C-c)  or:   ^x^c  to exit
     vi        ( ':q!"  or "ZZ" to exit, the latter one also saves the file!!!)
     pico      (^X to exit)
     gedit     (^Q or ^W) to exit, or click on File->Quit
```
     Many editors keep a backup copy, often with a tilde (~) appended to the filename


## Viewing Files:

Many ways to view a file on the terminal:

     cat       
     more      ('q' to get out, '?' to get help)
     less      (/FOO   to search for the word FOO)
     tac       (reverses the lines)

     head
     tail

## Extracting/Reducing files:


     wc        WordCount (and line and character) count
     sum       check sum (see also md5sum)
     grep      show lines that match some pattern (cf. google and googling)

## Other File Operations:

     cp        CoPy files
     mv        MoVe files (also renaming if it's not going to another directory)
     rm        ReMove files (directories would need the -r flag, but see also mkdir)
     ln        LiNk between files (symbolic/soft vs. hard link)

Linking files is like have a convenient shortcut available, e.g.

```
	ln -s /etc/passwd               # soft link (can go across devices)
	ls -l passwd
	head passwd

	rm passwd
	ln /etc/passwd                  # hard link (must be on same device)
```
Did you get an error in the last attempt?  if you, you are likely trying this across to another device. The **df** command
tells your devices, or on what device a file lives
```
	df .
	df /etc/passwd

	df
```
Lets try this again
```
	ls -l ~/.bashrc 
	ln ~/.bashrc dot-bashrc
	ls -l ~/.bashrc 
```
See something interesting in the second file listing?

## Scripting:

Scripting in UNIX is nothing more than a few shell commands in a text file, which you can execute directly using
the shell (the interpreter):

```
     echo "echo hello world" > hello
     bash hello
     ls -l hello

     chmod +x hello
     ls -l hello	
     hello
     echo $PATH
     ./hello
```

## Finding files:

   1) 'locate'    (but:   "**sudo updatedb**" - normally not enabled on Mac)

       locate -i poster

      
   2)  find       (arguably one of the more complex UNIX commands)
     
       find $HOME/Talks -name "*oster*"


## Adding to your own $PATH:
```
    cd                        # move to your home directory
    mkdir bin                 # create
    cp ASTR288P/astr288p/bin/*  bin
    echo $PATH                # is ~/bin already in your path? else edit your ~/.bashrc file now!
    lfind                     # check if the new 'lfind' is seen
    which lfind               # it should be in ~/bin now
    lfind lfind               # there should be two now !
```    
for example, the 
```
    export PATH=~/bin:$PATH
```
can be added to either the .bashrc or .bash_profile file.

## VNC

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


## GRIP

GitHub Readme Instant Preview (GRIP): a command that allows you to preview your
[*MarkDown*](https://en.wikipedia.org/wiki/Markdown) files (README.md
by default) in a web browser. These lecture notes are in md
(*MarkDown*) format, they are simple text files that are a lightweight markup
language, and they format nicely in a web brosers.

Install and use it as follows
```
   pip install grip
   grip Lecture2.md
```
Because python also has a built-in http (web) server, you can now open a URL on
[http://localhost:6419](http://localhost:6419)
