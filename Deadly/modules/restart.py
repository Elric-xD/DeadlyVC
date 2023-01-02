from pyrogram import Client, filters
from Deadly import SUDO_USERS, OWNER_ID
import os
import time

SUDOERS = SUDO_USERS + OWNER_ID

@Client.on_message(filters.command("reboot") & filters.user(SUDOERS))
async def reboot(_, m):
    ok = await m.reply("Rebooting. . .\nJust restarted your bot please wait for 3-4 mins before using this bot let this bot restart properly")
    time.sleep(3)
    await ok.delete()
    try:
        os.system(f"kill -9 {os.getpid()} && python3 -m Deadly")
    except Exception as e:
        await m.reply(e)
