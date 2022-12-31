import time
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls, idle

_boot_ = time.time()

""" config area """

if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}




#REQUIRED
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID")
DB_URL = getenv("DB_URL", None) 
LOG_ID = int(getenv("LOG_ID")) 

# STRING

SESSION1 = getenv("SESSION_NAME", None) 
SESSION2 = getenv("SESSION_NAME2", None) 
SESSION3 = getenv("SESSION_NAME3", None) 

#SUPPPORT LIST
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))


#EXTRA
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Elric-xD/DeadlyVC")


#IMAGES
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
PING_URL = getenv(" PING_URL", "https://te.legra.ph/file/abfcbebb3d9d8efbb7762.jpg") 






""" client area """

bot = Client("Freya", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Deadly.modules"))


if not SESSION1:
   ASSISTANT_1 = None
else:   
   ASSISTANT_1 = Client(SESSION1, api_id=API_ID, api_hash=API_HASH)
   

if not SESSION2:
   user = None
else:
   user = Client(SESSION2, api_id=API_ID, api_hash=API_HASH)
   

if not SESSION3:
   user3 = None
else:
   user3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH)




with Client(":musicfreya:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
    BOT_NAME = me_bot.first_name
    BOT_USERNAME = me_bot.username
    BOT_ID = me_bot.id

LODER = ASSISTANT_1
ASSISTANT_2 = user

if not SESSION1:
   call_py = None
else:   
   call_py = PyTgCalls(ASSISTANT_1)

if not SESSION2:
   user = None
else:
   call_py2 = PyTgCalls(user)

if not SESSION3:
   user3 = None
else:
   call_py3 = PyTgCalls(user3)



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
total_assistant = []



with Client("Freya", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    Freya = app.get_me()
    BOT_NAME = Freya.first_name
    BOT_USERNAME = Freya.username


async def start_bot():
    print("[INFO]: Starting Freya Music. . .")
    await bot.start()
    await bot.send_message(LOG_ID, "Starting Assistant Client. . ") 
# STARTING CLIENT1
    if SESSION1 != "None":
       await LODER.start()
       await call_py.start()
       await LODER.send_message(LOG_ID, f"Assistant One Successfully Started as {ASSNAME1}") 
       total_assistant.append(1)
# STARTING CLIENT2
    if STRING2 != "None":
       await user.start()
       await call_py2.start()
       await user.send_message(LOG_ID, f"Assistant Two Successfully Started as {ASSNAME2}") 
       total_assistant.append(2)
# STARTING CLIENT3
    if STRING3 != "None":
       await user3.start() 
       await call_py3.start()
       await user3.send_message(LOG_ID, f"Assistant Three Started as {ASSNAME3}") 
       total_assistant.append(3)
       total_assistant.append(4) 
    print("[INFO]: Your MusicBot Has been started")
    await idle()
    await bot.send_message(LOG_ID, "Your Music Bot Successfully Started") 



