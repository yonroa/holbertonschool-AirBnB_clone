# The Console 💻

<h2> CONSOLE <img src = "https://i.stack.imgur.com/sY3N5.gif" </h2>

## Objective ✔️

- Create a new object (ex: a new User or a new Place) 
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Installation 💫


```sh
https://github.com/yonroa/holbertonschool-AirBnB_clone
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


## Commands and their function ⌨️

| Commands | Functions |
| ------ | ------ |
| Create ✅ | Creates a new instance(```BaseModel, User, City...```)|
| All ✅ | Display all instance of class(```all BaseModel``` or ```all```) |
| Show ✅ | Prints the string representation of an instance based on the class name and id (```show BaseModel 1234-1234-1234```)|
| Update ✅ | Updates an instance based on the class name and id by adding or updating attribute(```update BaseModel 1234-1234-1234 email "aibnb@mail.com"```) |
| Destroy ✅ | Deletes an instance based on the class name and id (```destroy BaseModel 1234-1234-1234```) |
| Help ✅ | shows the updated commands |
| Quit ✅ | and EOF to exit the program |


# Authors 🤖

### Viktor Krill - @ViktorKrill <a href="https://www.twitter.com/Dev_Vikk" rel="nofollow"> <img width="18px" align="center" src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg" style="max-width: 100%;"></a> <a href="https://www.github.com/viktorkrill"> <img width="18px" align="center" src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg" style="max-width: 100%;"></a>

### Yompa - @Kadzahk <a href="https://www.twitter.com/yompa_0" rel="nofollow"> <img width="18px" align="center" src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg" style="max-width: 100%;"></a> <a href="https://www.github.com/yonroa"> <img width="18px" align="center" src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg" style="max-width: 100%;"></a>
