# NyanBot

A bot for Discord based on the (unofficial) Discord Python API. A Discord server I frequent is big on Fanart. As a result, I thought it'd be cool to have a bot that searched through my Fanart folder based on a specific keyword and uploaded a random piece of fanart that I've saved.

##Restriction
You must have your folders and files sorted and named appropriately for your task. 

##Changelist
- Listed the currently available commands on the readme.
- Added commands to modify approved channels without needing to edit the config file manually.
- Removed the "approved list". Instead, NyanBot keeps track of users by their id. Once they've used up their searches, I put them on a half hour cooldown. Bans are now tracked on a per user basis. Unfortunately, bans are currently reset if you restart NyanBot. A separate"NyanUser" class was created for organization and separation.
- Added an "approved list". If you intend to "approve" a lot of users to use the bot's search functions, perhaps this should be reversed with a "banned list".
- If the bot can't find an image with the keyword, it uploads a "consolation" image.
- Initial Commit. Functional Code that responds to discord messages that begin with ]nyan and can search through a directory and upload a random image related to the keyword.

##Configuring
The program relies on NyanConfig.txt existing in the same directory. NyanConfig.txt is using JSON for ease of use and expandability. Below is an example of what NyanConfig.txt muist have.
```
{
    "admin": ["list", "of", "ids", "for", "admins"]
    "username": "discord_email@example.com",
    "password": "discord_password",
    "directory": "/directory/to/fanart",
    "dankrectory": "/directory/to/dank"
    "catch": "catch file name.extension"
    "approvedchannels": ["list", "of", "channel", "ids"]
}
```
Catch file should be in "directory" and will be used as "consolation" if the search returns no results.
List of approved channels added to the config in case the server you intend to use this on is restrictive about only allowing bots in certain channels.

##Command List
NyanBot offers two command layers.
```
]nyan commands - can be used by anyone in the channel

]nyan - Ping the bot, response is randomized
]nyan search <term> - searches "directory" for files matching <term> and chooses a random file to upload. <term> must be alphabetic.
]nyan dank <term> - similar to search but looks in the dankrectory.
```

```
+nyan commands - can be used by anyone who's id is specified in the admin list in config.

+nyan id <@mentions> - pulls the id of anyone you @mention.
+nyan ban <@mentions> - bans people from using the search functions
+nyan unban <@mentions> - lifts the ban.
+nyan AddChannel - adds the current channel to the list of approved channels
+nyan RemoveChannel - removes the current channel from the list of approved channels
```
#TODO
- Currently "responses" and special search "keywords" (*girls_names*, relevant to the fanart that I collect) are hardcoded. Add appropriate capability to have these "configurations" in the config file. This will allow the code to be moreso about accomplishing a "general task" rather than the "specific mission" that I had in mind when I started the project.
- Add the capability to use admin commands to modify the config without manually having to do it.
- Add bans to the Config so that they may persist on bot restart.
