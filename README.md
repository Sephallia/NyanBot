# NyanBot

A bot for Discord based on the (unofficial) Discord Python API. A Discord server I frequent is big on Fanart. As a result, I thought it'd be cool to have a bot that searched through my Fanart folder based on a specific keyword and uploaded a random piece of fanart that I've saved.

##Restriction
You must have your folders and files sorted and named appropriately for your task. 

##Changelist
v0.01 - Initial Commit. Functional Code that responds to discord messages that begin with ]nyan and can search through a directory and upload a random image related to the keyword.
v0.02 - If the bot can't find an image with the keyword, it uploads a "consolation" image.
v0.03 - Added an "approved list". If you intend to "approve" a lot of users to use the bot's search functions, perhaps this should be reversed with a "banned list".

#Configuring
The program relies on NyanConfig.txt existing in the same directory. NyanConfig.txt is using JSON for ease of use and expandability. Below is an example of what NyanConfig.txt muist have.
```
{
    "username": "discord_email@example.com",
    "password": "discord_password",
    "directory": "/directory/to/fanart",
    "dankrectory": "/directory/to/dank"
    "catch": "catch file name.extension"
    "searchapproved": ["list", "of", "approved", "ids"]
}
```
Catch file should be in "directory" and will be used as "consolation" if the search returns no results.
The log file will contain IDs of users that have been rejected of their search. You can use this if you need to find an ID to add to the list.

Perhaps this should be made more clear somehow, but...
```
]nyan search will look in "directory"
]nyan dank will look in "dankrectory"
```

#TODO
Currently "responses" and special search "keywords" (*girls_names*, relevant to the fanart that I collect) are hardcoded. Add appropriate capability to have these "configurations" in the config file. This will allow the code to be moreso about accomplishing a "general task" rather than the "specific mission" that I had in mind when I started the project.
