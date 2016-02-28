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