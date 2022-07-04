# 0x00. AirBnB clone - The console

## Description
In this project we develop a console. A console is an interpreter of commands,
which the user executes when performing different actions. For example, create a
user, destroy some location of a home etc.

The base code is called BaseModel. Which has three attributes that are id, update,
time created. All created objects inherit these three attributes. This is convenient 
when we have to control the objects that we are using.

Another very important file is FileSotrage. Essentially what it does is transform 
the new dictionaries into json files and store them in memory. If at any time we need
a specific object, this program is in charge of looking for it and returning it.

Last but not least is the console. Commands are executed in this file. For example 
create, destroy, show etc. For me this file is like the application engine. It is what 
allows everything to run.

## Command Interpreter:
Through the interpreter and with the correct commands we can execute create, destroy 
or even show objects.

### How to start it

`./ console.py `
### How to use i
```
(hbdb) help
Documented commands (type help <topic>):
========================================
EOE  all  create  destroy  help  quit  show  update
```

### Examples

![hbnh](https://i.imgur.com/LrSQ55j.png)
