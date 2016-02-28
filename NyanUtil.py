from datetime import datetime
import json
import asyncio

class NyanUtil:
    ConfigDic = None
    log_file = None
    
    def load_dic():
        with open("NyanConfig.txt", "r") as docs:
            NyanUtil.ConfigDic = json.load(docs)
    
    @staticmethod
    async def add_channel(channelId):
        if channelId not in NyanUtil.ConfigDic["approvedchannels"]:
            NyanUtil.ConfigDic["approvedchannels"].append(channelId)
            await NyanUtil.write_config()
            await NyanUtil.write_log("Config File Updated")
            await NyanUtil.write_log("{} removed".format(channelId))
    
    @staticmethod
    async def remove_channel(channelId):
        if channelId in NyanUtil.ConfigDic["approvedchannels"]:
            NyanUtil.ConfigDic["approvedchannels"].remove(channelId)
            await NyanUtil.write_config()
            await NyanUtil.write_log("{} removed".format(channelId))
    
    @staticmethod
    async def write_log(msg):
        if (NyanUtil.log_file == None):
            NyanUtil.log_file = open("log.txt", "a+")
            NyanUtil.log_file.write("\n> " + str(datetime.now()) +"\n")
        NyanUtil.log_file.write("\t(" + msg + ")\n")
        NyanUtil.log_file.flush()
    
    @staticmethod
    async def write_config():
        with open("NyanConfig.txt", "w+") as docs:
            json.dump(NyanUtil.ConfigDic, docs)
            await NyanUtil.write_log("Config File Updated")
    
    @staticmethod
    def clean_username(msg):
        retmsg = ""
        for char in msg:
            if char.isalpha():
                retmsg += char
        return retmsg