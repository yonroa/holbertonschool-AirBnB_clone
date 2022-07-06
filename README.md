## Installation


```sh
https://github.com/Yonroa/AirBnB_clone.git
```

## Execution
 🔑 Interactive mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

🔑 Non-interactive mode:
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


## Commands and their function

| Commands | Functions |
| ------ | ------ |
| create | Creates a new instance(```BaseModel, User, City...```)|
| all | Display all instance of class(```all BaseModel``` or ```all```) |
| show | Prints the string representation of an instance based on the class name and id (```show BaseModel 1234-1234-1234```)|
| update | Updates an instance based on the class name and id by adding or updating attribute(```update BaseModel 1234-1234-1234 email "aibnb@mail.com"```) |
| destroy | Deletes an instance based on the class name and id (```destroy BaseModel 1234-1234-1234```) |
| help | shows the updated commands |
| quit | and EOF to exit the program |