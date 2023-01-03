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

๏ 𝐃𝐞𝐚𝐝𝐥𝐲 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ๏

๏ 𝐘𝐨𝐮𝐫 @{BOT_USERNAME} 𝐢𝐬 𝐎𝐧𝐥𝐢𝐧𝐞 🔥

──────────────────
𝗕𝗢𝗧 𝗗𝗘𝗧𝗔𝗜𝗟𝗦:
𝐍𝐀𝐌𝐄: {BOT_NAME}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{BOT_USERNAME}

──────────────────
𝐎𝐖𝐍𝐄𝐑: {OWNER_ID}
──────────────────
"""

@app.on_message(filters.command("alive") & ~filters.edited)
async def alive(client, m: Message):  
    await m.delete() 
    chat_id = m.chat.id
    sj = await m.reply_text("𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐀𝐥𝐢𝐯𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞. . .")    
    owner = "ELRIC-XD" #JUST FOR FUN
    await sj.delete() 
    msg = await app.send_photo(
        chat_id=chat_id, 
        photo=ALIVE_PIC, 
        caption=alive_txt
    )
    
