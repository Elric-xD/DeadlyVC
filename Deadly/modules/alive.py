import os
from pyrogram import Client 
from pyrogram.types import Message
from pyrogram import filters
from Deadly import(
 BOT_NAME, OWNER_NAME,
 ASSISTANT_ID, ASSISTANT_USERNAME,
 ASSISTANT_NAME, BOT_NAME, BOT_USERNAME
) 
from Deadly import bot as app


ALIVE_PIC = "https://te.legra.ph/file/404503e13fac593ada12d.jpg"

alive_txt = f"""

๏ 𝐃𝐞𝐚𝐝𝐥𝐲 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ๏

๏ Your @{BOT_USERNAME} is Online

──────────────────
ASSISTANT DETAILS: 

ID: {ASSISTANT_ID}
NAME: {ASSISTANT_NAME}
USERNAME: @{ASSISTANT_USERNAME}
──────────────────
BOT DETAILS:
NAME: {BOT_NAME}
USERNAME: @{BOT_USERNAME}

──────────────────
OWNER: {OWNER_NAME}
──────────────────
"""

@app.on_message(filters.command("alive") & ~filters.edited)
async def alive(client, message):  
    m = await app.reply_text("**Hold On. . . **") 
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=ALIVE_PIC, 
        caption=alive_txt
    )
    await m.delete() 
