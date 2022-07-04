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

### How to use it

Run the console

syntax:
	(hbbd) command <BaseModel> id

## Example:

```
(hbdb) help

Documented commands (type help <topic>):
========================================
EOE  all  create  destroy  help  quit  show  update
```

```
(hbdb) create BaseModel
702e8662-8eae-4781-bf8f-a09d06fe1055
```

```
(hbdb) create BaseModel
8779ea41-c044-40d7-a212-8ac48941b2e2
(hbdb) destroy BaseModel 8779ea41-c044-40d7-a212-8ac48941b2e2
(hbdb) show BaseModel 8779ea41-c044-40d7-a212-8ac48941b2e2
** no instance found **
(hbdb) create BaseModel
ac8b9ffe-af76-4dee-9812-c90a1d627f30
(hbdb) show BaseModel ac8b9ffe-af76-4dee-9812-c90a1d627f30
*[BaseModel](ac8b9ffe-af76-4dee-9812-c90a1d627f30) {'id': 'ac8b9ffe-af76-4dee-9812-c90a1d6
27f30', 'created_at': datetime.datetime(2022, 7, 4, 23, 23, 53, 537703),
'update_at': datetime.datetime(2022, 7, 4, 23, 23, 53, 537708)}
(hbdb)
```
![hbnh](https://i.imgur.com/LrSQ55j.png)
