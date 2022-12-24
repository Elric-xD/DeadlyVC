import asyncio
from pytgcalls import idle
from Deadly import call_py, bot
LOG = "TheDeadlyBots"

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    await bot.send_message(LOG, "Started DeadlyVC Successfully") 
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
