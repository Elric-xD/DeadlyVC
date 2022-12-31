
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
LOG_ID = int(getenv("LOG_ID")) 

SESSION_NAME = getenv("SESSION_NAME", None)
OWNER_NAME = getenv("OWNER_NAME", None)
DB_URL = getenv("DB_URL", None) 
ALIVE_NAME = getenv("ALIVE_NAME", None)

#SUPPPORT LIST
GROUP_SUPPORT = getenv("GROUP_SUPPORT", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))


#EXTRA
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")


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

bot = Client(
    "Deadly",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Deadly.modules"),
    )

blaze = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(blaze,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(blaze, overload_quiet_mode=True)

with Client("Deadly", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    asbot = app.get_me()
    BOT_NAME = asbot.first_name
    BOT_USERNAME = asbot.username

with blaze as app:
    asid = app.get_me()
    ASSISTANT_ID = asid.id
    ASSISTANT_NAME = asid.first_name 
    ASSISTANT_USERNAME = asid.username
