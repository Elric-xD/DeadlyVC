import time

import psutil
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from Deadly import BOT_NAME, PING_URL
from Deadly import bot as app, _boot_
from Deadly import bot as app
from Deadly.calls import  Freya
from Deadly.core.Cache.format import get_readable_time

# load
async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK

# run


@app.on_message(filters.command("ping") & ~filters.edited)
async def pingm(client, message: Message):
    await message.delete() 
    response = await message.reply_photo(
        photo=PING_URL,
        caption="**Pinging. . . **"
    )
    start = datetime.now()
    a1 = await Plugin1.ping
    a2 = await Plugin2.ping
    a3 = await Plugin3.ping
    a4 = await Plugin4.ping
    pytgping = f"{a1+a2+a3+a4}*
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(f"""
➽─────────────❥
{BOT_NAME} ɪs ʀᴇᴀᴅʏ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ 🎶
ᴡɪᴛʜ ᴘɪɴɢ ᴏғ: {resp}ms

 ╭⸻⸻⸻╮
 ◆ Uᴘᴛɪᴍᴇ ⊱ {UP}
 ◆ Cᴘᴜ ⊱ {CPU}
 ◆ Rᴀᴍ ⊱ {RAM}
 ◆ Pʏ- Tɢᴄᴀʟʟs Pɪɴɢ ⊱  {pytgping} ms
 ◆ Sᴛᴏʀᴀɢᴇ ᴜsᴇᴅ ⊱ {DISK}
 ╰⸻⸻⸻╯

➽─────────────❥
"""
) 
