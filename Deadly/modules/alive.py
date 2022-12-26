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

๏ 𝐘𝐨𝐮𝐫 @{BOT_USERNAME} 𝐢𝐬 𝐎𝐧𝐥𝐢𝐧𝐞 🔥

──────────────────
𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 𝗗𝗘𝗧𝗔𝗜𝗟𝗦: 

𝐈𝐃: {ASSISTANT_ID}
𝐍𝐀𝐌𝐄: {ASSISTANT_NAME}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{ASSISTANT_USERNAME}
──────────────────
𝗕𝗢𝗧 𝗗𝗘𝗧𝗔𝗜𝗟𝗦:
𝐍𝐀𝐌𝐄: {BOT_NAME}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{BOT_USERNAME}

──────────────────
𝐎𝐖𝐍𝐄𝐑: {OWNER_NAME}
──────────────────
"""

@app.on_message(filters.command("alive") & ~filters.edited)
async def alive(client, m: Message):  
    await m.delete() 
    sj = await message.reply_text("𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐀𝐥𝐢𝐯𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞. . .")    
    owner = "ELRIC-XD #JUST FOR FUN
    await sj.delete() 
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=ALIVE_PIC, 
        caption=alive_txt
    )
    
