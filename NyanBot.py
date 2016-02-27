# The MIT License (MIT) / https://opensource.org/licenses/MIT
# Author: Sephallia (Dennis N / https://github.com/Sephallia)
# Date: Feb 26, 2016

from datetime import datetime
from random import randint
import discord
import os, os.path
import json
import requests
import aiohttp
import asyncio

client = discord.Client()
user = discord.User()
message = discord.Message()
directory = None
log_file = None
girl_names = ["rin", "hanayo", "maki", "honoka", "umi", "kotori", "eri", "nozomi", "nico"]
nyansponses = ["Nyan?", "にゃん!", "(✿◠‿◠)〜 ITSUDEMOO (✿◠‿◠)〜", "Nyaa~", "(✿◠‿◠)〜 いつでも (✿◠‿◠)〜"]

@client.event
async def on_message(message):
    try:
        currentMessage = message.content
        #list of commands here
        if client.user in message.mentions:
            if message.author.id == client.user.id:
                return
            else:
                msg = "[WIP] Remind Seph-nyan to write this!~"
                await client.send_message(message.channel, msg)
            return
        
        if currentMessage.startswith("]にゃん"):
            msg = "日本語で何のつもりですかい？！"
            await client.send_message(message.channel, msg)
        if currentMessage.startswith("]nyan"):
            await write_log("{} CALLED: {}".format(message.author.name, currentMessage))
            currentMessage = currentMessage.split(" ")
            if len(currentMessage) == 1:
                await client.send_message(message.channel, nyansponses[randint(0, len(nyansponses)-1)])
            else:
                if currentMessage[1] == "todo":
                    if str(message.author.id) == "126439705934954497":
                        msg = "Seph-nyan should figure out what to do!" 
                        await client.send_message(message.channel, msg)
                    else:
                        msg = "You're not my Seph-nyan!"
                        await client.send_message(message.channel, msg)
                elif currentMessage[1] == "search":
                    if len(currentMessage) == 3 and str.isalpha(currentMessage[2]):
                        searchTerm = currentMessage[2].lower()
                        
                        result, msg = await search(directory, searchTerm, message.author.id)
                        if (result != ""):
                            msg = message.author.mention + " " + msg
                            await client.send_file(message.channel, result, content=msg)
                        else:
                            await client.send_message(message.channel, msg)
                    else:
                        msg = "```Usage: ]nyan search <term>\n\tTerm may only be alphabetical!\n\tPlease don't try to break me-nyaa~```"
                        await client.send_message(message.channel, msg)
                            
                elif currentMessage[1] == "dank":
                    if len(currentMessage) == 3 and str.isalpha(currentMessage[2]):
                        searchTerm = currentMessage[2].lower()
                        
                        result, msg = await search(dankrectory, searchTerm, message.author.id)
                        if (result != ""):
                            msg = message.author.mention + " " + msg
                            await client.send_file(message.channel, result, content=msg)
                        else:
                            await client.send_message(message.channel, msg)
                    else:
                        msg = "```Usage: ]nyan dank <term>\n\tTerm may only be alphabetical!\n\tPlease don't try to break me-nyaa~```"
                        await client.send_message(message.channel, msg)
                    
    except Exception as ex:
        await write_log("ERROR: " + str(ex))

async def search(directory, searchTerm, callerId):
    
    if (callerId == client.user.id):
        result = ""
        msg = ""
        searchResults = []
        for root, _, files in os.walk(directory):
            if searchTerm in girl_names:
                # If the searchTerm is a girl's name and girl's name is not in the directory we're looking in, head to the next directory, theoretically.
                if searchTerm not in root.lower():
                    continue
            for f in files:
                if searchTerm in f.lower():
                    searchResults.append(os.path.join(root, f))
        if len(searchResults) > 0:
            msg = "Found something! Are you pleased with NyanBot-nya?"
            await write_log("FOUND!")
            return searchResults[randint(0, len(searchResults)-1)], msg
        else:
            msg = "Could not find '{}'. Nyanbot is sorry nyan~".format(searchTerm)
            await write_log("NOTHING FOUND")
            return "", msg
    else:
        result = ""
        msg = "```For the sake of bandwidth, NyanBot's search features\nare only available for Seph-nyan. Please contact Seph-nyan\nif you would like to make use of these features.```"
    return result, msg
        
#client.change_status(game=discord.Game(name="your custom game here"))
async def write_log(msg):
    global log_file
    if (log_file == None):
        log_file = open("log.txt", "a+")
        log_file.write("\n> " + str(datetime.now()) +"\n")
    log_file.write("\t(" + msg + ")\n")
    log_file.flush()

@client.event
async def on_ready():
    await write_log("Logged in as")
    await write_log(client.user.name)
    await write_log(client.user.id)
    await write_log("Looking in dir: " + directory)
    await write_log("Dank in dir: " + dankrectory)
    
if __name__ == "__main__":
    global directory
    global dankrectory
    
    docs = open("NyanConfig.txt")
    ConfigDic = json.load(docs)
    directory = ConfigDic["directory"]
    dankrectory = ConfigDic["dankrectory"]
    client.run(ConfigDic["username"], ConfigDic["password"])