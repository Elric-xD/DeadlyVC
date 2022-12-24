# DeadlyVC < https://github.com/Elric-xD/DeadlyVC >
# © ELRIC-XD
import os
import wget
import speedtest
import asyncio

from PIL import Image
from pyrogram.types import Message
from pyrogram import filters, Client

from Deadly import bot 
from Deadly import SUDO_USERS as SUDOERS

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ. . .**")
        test.download()
        m = m.edit("**ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ. . .**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ. . .**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def run_speedtest(_, message):
    userid = message.from_user.id
    m = await message.reply_text("Running Speed test")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴘ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴘᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴘɪɴɢ 🏓:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
