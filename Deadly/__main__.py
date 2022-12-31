import asyncio
from pytgcalls import idle
from Deadly import call_py, bot, LOG_ID, BOT_NAME, ASSISTANT_NAME, blaze

async def start_bot():
    print("Starting Music Bot")
    await bot.start()
    await bot.send_message(LOG_ID, f"Starting Music Bot") 
    print("Booting UserBot and Pytgcalls Client")
    await blaze.start() 
    await blaze.send_message(LOG_ID, f"Started Assistant as {ASSISTANT_NAME}") 
    await call_py.start()
    await bot.send_message(LOG_ID, f"Started Music Bot\n BOT NAME:{BOT_NAME}\nASS NAME: {ASSISTANT_NAME}") 
    await idle()
    print("Music Bot Stopped. . .")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
