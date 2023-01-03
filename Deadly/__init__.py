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
from Clients.client import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, 
                                    ASS_CLI_4, app)


_boot_ = time.time()

""" config area """

load_dotenv()
admins = {}

#REQUIRED
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
BOT_TOKEN = getenv("BOT_TOKEN")
LOG_ID = int(getenv("LOG_ID")) 
OWNER_ID = int(getenv("OWNER_ID"))

SESSION_NAME = getenv("SESSION_NAME", None)
OWNER_NAME = getenv("OWNER_NAME", None)
DB_URL = getenv("DB_URL", None) 
ALIVE_NAME = getenv("ALIVE_NAME", None)

#SUPPPORT LIST
GROUP_SUPPORT = getenv("GROUP_SUPPORT", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)

#EXTRA
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Elric-xD/DeadlyVC")


#IMAGES
START_IMG = getenv("START_IMG", None) 
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/1fe6ea0b46335debc49e6.png") # FOR TELEGRAM STREAMING
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
PING_URL = getenv(" PING_URL", "https://te.legra.ph/file/abfcbebb3d9d8efbb7762.jpg") 




"""
--------------------------------------------------------------DON'T EDIT FROM HERE------------------------------------------------------------------------------------------
"""
loop = asyncio.get_event_loop()

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

# STARTING BOT

async def initiate_bot():
    global SUDO_USERS, OWNER_ID, ASSIDS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID1, ASSNAME1, ASSMENTION1, ASSUSERNAME1
    global ASSID2, ASSNAME2, ASSMENTION2, ASSUSERNAME2
    global ASSID3, ASSNAME3, ASSMENTION3, ASSUSERNAME3
    global ASSID4, ASSNAME4, ASSMENTION4, ASSUSERNAME4        
    os.system("clear")
    header = "Starting Deadly Music. . . "
    print(header)      
    print("Deadly Music Bot Booting...") 
    print("Booting Up The Clients...\n")
        await app.start()
    print("Booted Bot Client")
    print("Booting Up The Assistant Clients...")
        if STRING1 != "None":
            await ASS_CLI_1.start()
            random_assistant.append(1)
    print("Booted Assistant Client")
        if STRING2 != "None":
            await ASS_CLI_2.start()
            random_assistant.append(2)
    print("Booted Assistant Client 2")
        if STRING3 != "None":
            await ASS_CLI_3.start()
            random_assistant.append(3)
            console.print("├ [yellow]Booted Assistant Client 3")
        if STRING4 != "None":
            await ASS_CLI_4.start()
            random_assistant.append(4)
    print("Booted Assistant Client 4")
    print("Assistant Clients Booted Successfully!")
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "Cache" not in listdir():
            mkdir("Cache")
    print("Loading Clients Information...")
        getme = await app.get_me()
        BOT_ID = getme.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
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
        print("Loaded Clients Information!")
        print("Loading Sudo Users...")
        sudoersdb = db.sudoers
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in SUDOERS:
            if user_id not in sudoers:
                sudoers.append(user_id)
                await sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        SUDO_USERS = (SUDOERS + sudoers + OWNER_ID) if sudoers else SUDOERS
        print("Loaded Sudo Users Successfully!")

loop.run_until_complete(initiate_bot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
