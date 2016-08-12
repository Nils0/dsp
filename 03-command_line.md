# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd = Print working directory  
mkdir = make directory  
cd = change directory  
ls = list of elements on current directory  	
cp = copy a file or directory  
pipe: | = takes the output from the comand from the right and „pipes“ it to the command on the right  
">" = take the output from the command on the left side and writes it tot he file on the right  
"*" = matches anything in a wildcard like *.txt  
find . –name  „ „ = find in pwd files with respetive name (e.g. „*.txt“)  
cat > somefile = cat reads whatever you type and write it to somefile  


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls = list all files and foldes in pwd  
ls -a = same as ls but also showing hidden file beginning with a dot  
ls -l = Detailed list incl. date of last changes and file size  
ls -lh = Detailed list, human readable (very similar to ls -l but with unit suffixes)  
ls -lah = similar as ls -lh but now including the hidden files beginning with a dot  
ls -t = list files and folders and sort by time modified (most recently modified first) before sorting the operands by lexicographical order  
ls -Glp = once again the list but with colourized output (G), detailed lsit (l) and write a "/" after each file if that file is a directory (p)


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -d = show directories only  
ls -m = displays names as a comma seperate list  
ls -R = displays subdirectories as well
ls -u = displays files by the file access times
ls -1 = displays each enty on a line  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs can be used to buid and execute commands from standard input. Example:  
  
$ find / -name '*.text* | xargs rm  
  
This removes all the text files.

 

