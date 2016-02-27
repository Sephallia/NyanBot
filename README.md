#A bot for Discord based on the (unofficial) Discord Python API.

A Discord server I frequent is big on Fanart. As a result, I thought it'd be cool to have a bot that searched through my Fanart folder based on a specific keyword and uploaded a random piece of fanart that I've saved.

##Restriction
You must have your folders and files sorted and named appropriately for your task. 

##Changelist
v0.01 - Initial Commit. Functional Code that responds to discord messages that begin with ]nyan and can search through a directory and upload a random image related to the keyword.

#Configuring
The program relies on NyanConfig.txt existing in the same directory. NyanConfig.txt is using JSON for ease of use and expandability. Below is an example of what NyanConfig.txt muist have.
```
{
    "username": "discord_email@example.com",
    "password": "discord_password",
    "directory": "/directory/to/fanart",
    "dankrectory": "/directory/to/dank"
}
```
Perhaps this should be made more clear somehow, but...
```
]nyan search will look in "directory"
]nyan dank will look in "dankrectory"
```

#TODO
Currently "responses" and special search "keywords" (*girls_names*, relevant to the fanart that I collect) are hardcoded. Add appropriate capability to have these "configurations" in the config file. This will allow the code to be moreso about accomplishing a "general task" rather than the "specific mission" that I had in mind when I started the project.
