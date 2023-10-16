AirBnB clone project
This projects aims to create a simple copy of AirBnB website with some of its features
- This repository is the first step in the project which contains six steps:
* The console
* Web static
* MySQL storage
* Web framework - templating
* RESTful API
* Web dynamic
The console:
It's a command interpreter that manages creating, updating and deleting of objects in the project
-Starting the console is done using the command ./console then the prompt (hbnb) will appear.
-You can type help to the prompt to know the commands that exists in the console.
-Typing help then command will tell you what that command does
-Typing quit to the prompt will exit the console

Examples:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
$
----------------------------------------------
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
