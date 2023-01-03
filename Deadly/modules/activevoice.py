from pyrogram import filters
from pyrogram.types import Message

from Deadly import app as bot 
from Deadly import SUDO_USERS
from Deadly.database.voicechatdb import *

@bot.on_message(filters.command("activevoice") & filters.user(SUDO_USERS))
async def activevc(_, message: Message):
    await message.delete() 
    Semx = await message.reply_text(
        "Getting active voice chats. . ."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await bot.get_chat(x)).title
        except Exception:
            title = "Private Group"
        if (await bot.get_chat(x)).username:
            user = (await bot.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await Semx.edit_text("No Active Voice Chats Found")
    else:
        await Semx.edit_text(
            f"**Active Voice Chats:-**\n\n{text}",
            disable_web_page_preview=True,
        )
