import os
from pyrogram import Client 
from pyrogram.types import Message
from pyrogram import filters
from Deadly import(
 BOT_NAME, OWNER_ID,
 BOT_NAME, BOT_USERNAME
) 
from Deadly import app


ALIVE_PIC = "https://te.legra.ph/file/404503e13fac593ada12d.jpg"

alive_txt = f"""

เน ๐๐๐๐๐ฅ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐๐จ๐ญ เน

เน ๐๐จ๐ฎ๐ซ @{BOT_USERNAME} ๐ข๐ฌ ๐๐ง๐ฅ๐ข๐ง๐ ๐ฅ

โโโโโโโโโโโโโโโโโโ
๐๐ข๐ง ๐๐๐ง๐๐๐๐ฆ:
๐๐๐๐: {BOT_NAME}
๐๐๐๐๐๐๐๐: @{BOT_USERNAME}

โโโโโโโโโโโโโโโโโโ
๐๐๐๐๐: {OWNER_ID}
โโโโโโโโโโโโโโโโโโ
"""

@app.on_message(filters.command("alive") & ~filters.edited)
async def alive(client, m: Message):  
    await m.delete() 
    chat_id = m.chat.id
    sj = await m.reply_text("๐๐ซ๐๐๐ญ๐ข๐ง๐  ๐๐ฅ๐ข๐ฏ๐ ๐๐๐ฌ๐ฌ๐๐ ๐. . .")    
    owner = "ELRIC-XD" #JUST FOR FUN
    await sj.delete() 
    msg = await app.send_photo(
        chat_id=chat_id, 
        photo=ALIVE_PIC, 
        caption=alive_txt
    )
    
