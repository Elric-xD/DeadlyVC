import os
from program import Client 
from Deadly import(
 BOT_NAME, OWNER_NAME,
 ASSISTANT_ID, ASSISTANT_USERNAME,
 ASSISTANT_NAME, BOT_NAME, BOT_USERNAME
) 
from Deadly import bot


ALIVE_PIC = "https://te.legra.ph/file/404503e13fac593ada12d.jpg"

alive_txt = """

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

@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & other_filters)
async def alive(client, message):  
    await client.reply_photo(photo=ALIVE_PIC, caption=f{alive_txt})
