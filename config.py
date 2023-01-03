import os
from os import listdir, mkdir
from os import getenv
from dotenv import load_dotenv




""" config area """

load_dotenv()
admins = {}

#REQUIRED
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
LOG_ID = int(getenv("LOG_ID")) 
OWNER_ID = int(getenv("OWNER_ID"))

STRING1 = getenv("SESSION_NAME", None)
STRING2 = getenv("SESSION_NAME2", None)
STRING3 = getenv("SESSION_NAME3", None)
STRING4 = getenv("SESSION_NAME4", None)



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
