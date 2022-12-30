import time

import psutil
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from Deadly import BOT_NAME, PING_URL
from Deadly import bot as app, _boot_
from Deadly import bot as app
from Deadly import call_py as Akki
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


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_URL,
        caption="**Pinging. . . **"
    )
    start = datetime.now()
    pytgping = await Yukki.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(f"{BOT_NAME} ɪs ᴡᴏʀᴋɪɴɢ ɢᴏᴏᴅ ᴡɪᴛʜ ᴀ ᴘɪɴɢ ᴏғ  {resp}ᴍs.\n\nʙᴏᴛ's ᴜᴘᴛɪᴍᴇ: {UP}\n\nᴛᴏᴛᴀʟ ᴏғ  {DISK} sᴇʀᴠᴇʀ's sᴛᴏʀᴀɢᴇ.\n\nᴄᴘᴜ ʟᴏᴀᴅ ɪs ᴀʙᴏᴜᴛ {CPU} \n\nᴡɪᴛʜ ᴀ ᴄᴏɴsᴜᴍᴘᴛɪᴏɴ ᴏғ {RAM} ʀᴀᴍ. \nᴘʏ-ᴛɢᴄᴀʟʟs ᴄʟɪᴇɴᴛ ʜᴀᴠɪɴɢ ᴘɪɴɢ ᴏғ {pytgping} ᴍs.")

