from config import *
import asyncio
import time
import os
from os import listdir, mkdir
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as Bot
from aiohttp import ClientSession
from pytgcalls import PyTgCalls, idle


_boot_ = time.time()


"""
--------------------------------------------------------------DON'T EDIT FROM HERE------------------------------------------------------------------------------------------
"""


loop = asyncio.get_event_loop()



app = Client(
    "DeadlyVC",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Deadly.modules"), 
)


if not STRING1:
    ASS_CLI_1 = None
else:
    ASS_CLI_1 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING1,        
    )


if not STRING2:
    ASS_CLI_2 = None
else:
    ASS_CLI_2 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING2,        
    )


if not STRING3:
    ASS_CLI_3 = None
else:
    ASS_CLI_3 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING3,       
    )


if not STRING4:
    ASS_CLI_4 = None
else:
    ASS_CLI_4 = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING4,        
    )




# DATABASE

MONGODB_CLI = Bot(DB_URL)
db = MONGODB_CLI.Freya

### Bot Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""

### Client
app = app
ASS_CLI_1 = ASS_CLI_1
ASS_CLI_2 = ASS_CLI_2
ASS_CLI_3 = ASS_CLI_3
ASS_CLI_4 = ASS_CLI_4
aiohttpsession = ClientSession()

### Assistant Info
ASSIDS = []
ASSID1 = 0
ASSNAME1 = ""
ASSUSERNAME1 = ""
ASSMENTION1 = ""
ASSID2 = 0
ASSNAME2 = ""
ASSUSERNAME2 = ""
ASSMENTION2 = ""
ASSID3 = 0
ASSNAME3 = ""
ASSUSERNAME3 = ""
ASSMENTION3 = ""
ASSID4 = 0
ASSNAME4 = ""
ASSUSERNAME4 = ""
ASSMENTION4 = ""
random_assistant = []

# STARTING BOT XD

async def initiate_bot():
    print("Starting Music Bot...")
    await app.start() 
    print("Booting Assistant Client")
    if STRING1 != "None":
       await ASS_CLI_1.start()       
       random_assistant.append(1)
    print("Booted Assistant Client 1")
    if STRING2 != "None":
       await ASS_CLI_2.start()
       random_assistant.append(2)
    print("Booted Assistant Client 2")
    if STRING3 != "None":
       await ASS_CLI_3.start()
       random_assistant.append(3)
    print("Booted Assistant Client 3")
    if STRING4 != "None":
       await ASS_CLI_4.start()       
       random_assistant.append(4)
    print("Booted Assistant Client 4")
    print("Assistant Clients Booted Successfully!")
    if "downloads" not in listdir():
        mkdir("downloads")
    if "Cache" not in listdir():
        mkdir("Cache")
    print("Local File Created Again") 
    getme = await app.get_me()
    BOT_ID = getme.id
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
    print("Loading Clients Information...")
    if STRING1 != "None":
        getme1 = await ASS_CLI_1.get_me()
        ASSID1 = getme1.id
        ASSIDS.append(ASSID1)
        ASSNAME1 = (
            f"{getme1.first_name} {getme1.last_name}"
            if getme1.last_name
            else getme1.first_name
        )
        ASSUSERNAME1 = getme1.username
        ASSMENTION1 = getme1.mention
    if STRING2 != "None":
        getme2 = await ASS_CLI_2.get_me()
        ASSID2 = getme2.id
        ASSIDS.append(ASSID2)
        ASSNAME2 = (
            f"{getme2.first_name} {getme2.last_name}"
            if getme2.last_name
            else getme2.first_name
        )
        ASSUSERNAME2 = getme2.username
        ASSMENTION2 = getme2.mention
    if STRING3 != "None":
        getme3 = await ASS_CLI_3.get_me()
        ASSID3 = getme3.id
        ASSIDS.append(ASSID3)
        ASSNAME3 = (
            f"{getme3.first_name} {getme3.last_name}"
            if getme3.last_name
            else getme3.first_name
        )
        ASSUSERNAME3 = getme3.username
        ASSMENTION3 = getme3.mention
    if STRING4 != "None":
        getme4 = await ASS_CLI_4.get_me()
        ASSID4 = getme4.id
        ASSIDS.append(ASSID4)
        ASSNAME4 = (
            f"{getme4.first_name} {getme4.last_name}"
            if getme4.last_name
            else getme4.first_name
        )
        ASSUSERNAME4 = getme4.username
        ASSMENTION4 = getme4.mention     

loop.run_until_complete(initiate_bot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
