# The MIT License (MIT) / https://opensource.org/licenses/MIT
# Author: Sephallia (Dennis N / https://github.com/Sephallia)
# Date: Feb 26, 2016

from datetime import datetime
from random import randint
from NyanUser import NyanUser
import discord
import os, os.path
import json
import requests
import aiohttp
import asyncio

client = discord.Client()
user = discord.User()
message = discord.Message()
UserDic = {}
ConfigDic = None
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
                msg = "NyanBot is still a Work In Progress! Please forgive her if she can't satisfy your needs. Seph-nyan is ~~diligently~~ working on her-nyaa!\n\n```For now, you may interact with NyanBot by using:\n\t]nyan```"
                await send_wrapper(message.channel, msg)
            return
        
        if currentMessage.startswith("]nyan"):
            await write_log("{} CALLED: {}".format(clean_username(message.author.name), currentMessage))
            currentMessage = currentMessage.split(" ")
            if len(currentMessage) == 1:
                await send_wrapper(message.channel, nyansponses[randint(0, len(nyansponses)-1)])
            else:
                if currentMessage[1] == "search":
                    if len(currentMessage) == 3 and str.isalpha(currentMessage[2]):
                        searchTerm = currentMessage[2].lower()
                        
                        filename, msg = await search(ConfigDic["directory"], searchTerm, message.author.id)
                        if (filename != ""):
                            msg = message.author.mention + " " + msg
                            await send_wrapper(message.channel, msg, file=filename)
                        else:
                            await send_wrapper(message.channel, msg)
                    else:
                        msg = "```Usage: ]nyan search <term>\n\tTerm may only be alphabetical!\n\tPlease don't try to break me-nyaa~```"
                        await send_wrapper(message.channel, msg)
                            
                elif currentMessage[1] == "dank":
                    if len(currentMessage) == 3 and str.isalpha(currentMessage[2]):
                        searchTerm = currentMessage[2].lower()
                        
                        filename, msg = await search(ConfigDic["dankrectory"], searchTerm, message.author.id)
                        if (filename != ""):
                            msg = message.author.mention + " " + msg
                            await send_wrapper(message.channel, msg, file=filename)
                        else:
                            await send_wrapper(message.channel, msg)
                    else:
                        msg = "```Usage: ]nyan dank <term>\n\tTerm may only be alphabetical!\n\tPlease don't try to break me-nyaa~```"
                        await send_wrapper(message.channel, msg)
                    
        elif currentMessage.startswith("+nyan"):
            await write_log("{} CALLED: {}".format(clean_username(message.author.name), currentMessage))
            currentMessage = currentMessage.split(" ")
            if str(message.author.id) in ConfigDic["admin"]:
                if currentMessage[1] == "todo":
                    msg = "Seph-nyan should figure out what to do!" 
                    await send_wrapper(message.channel, msg)
                elif currentMessage[1] == "id":
                    if len(message.mentions) == 0:
                        msg = "{} Here you are-nyan!".format(message.author.id)
                        await send_wrapper(message.channel, msg)
                    else:
                        for mentionedUser in message.mentions:
                            msg = "{} Here you are-nyan!".format(mentionedUser.id)
                            await send_wrapper(message.channel, msg)
                elif currentMessage[1] == "ban":
                    for mentionedUser in message.mentions:
                        if mentionedUser.id not in UserDic:
                            UserDic[mentionedUser.id] = NyanUser(mentionedUser.id)
                        UserDic[mentionedUser.id].banned = True
                        msg = "{} has been banned-nyan!".format(mentionedUser.name)
                        await send_wrapper(message.channel, msg)
                elif currentMessage[1] == "unban":
                    for mentionedUser in message.mentions:
                        if mentionedUser.id not in UserDic:
                            UserDic[mentionedUser.id] = NyanUser(mentionedUser.id)
                        UserDic[mentionedUser.id].banned = False
                        msg = "{} has been unbanned-nyan!".format(mentionedUser.name)
                        await send_wrapper(message.channel, msg)
        elif currentMessage.startswith("]にゃん"):
            msg = "日本語で何のつもりですかい？！"
            await send_wrapper(message.channel, msg)
        
    except Exception as ex:
        await write_log("ERROR: " + str(ex))

async def send_wrapper(channel, msg, file=None):
    if str(channel).startswith("Direct Message") or channel.id in ConfigDic["channelsapproved"]:
        if file == None:
            await client.send_message(channel, msg)
        else:
            await client.send_file(channel, file, content=msg)
    else:
        await write_log("{} is not an approved channel.".format(channel.id))
        
async def search(directory, searchTerm, callerId):
    if (callerId not in UserDic):
        UserDic[callerId] = NyanUser(callerId)

    # WIP / TODO currently disabled
    if (not UserDic[callerId].banned) and (UserDic[callerId].searches < 8) : # callerId not in ConfigDic["searchbanned"]
        UserDic[callerId].PerformedSearch()
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
            return os.path.join(directory, ConfigDic["catch"]), msg
    else:
        result = ""
        msg = "For the sake of bandwidth, you have been restricted from using this feature. Give NyanBot around an hour-nyaa~ If the problem persists after, perhaps you've been banned. Nyahaha~"
        await write_log("Search from {} rejected.".format(callerId))
    return result, msg
        
#client.change_status(game=discord.Game(name="your custom game here"))
async def write_log(msg):
    global log_file
    if (log_file == None):
        log_file = open("log.txt", "a+")
        log_file.write("\n> " + str(datetime.now()) +"\n")
    log_file.write("\t(" + msg + ")\n")
    log_file.flush()
    
def write_config():
    with open("NyanConfig.txt", "w+") as docs:
        json.dump(data, docs)
    
@client.event
async def on_ready():
    await write_log("Logged in as")
    await write_log(clean_username(client.user.name))
    await write_log(client.user.id)
    await write_log("Looking in dir: " + ConfigDic["directory"])
    await write_log("Dank in dir: " + ConfigDic["dankrectory"])
    
def clean_username(msg):
    retmsg = ""
    for char in msg:
        if char.isalpha():
            retmsg += char
    return retmsg
    
if __name__ == "__main__":
    global ConfigDic
    
    with open("NyanConfig.txt", "r") as docs:
        ConfigDic = json.load(docs)
        client.run(ConfigDic["username"], ConfigDic["password"])