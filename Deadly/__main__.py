
import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle

from Deadly import (LOG_ID, STRING1, STRING2, STRING3, STRING4)
from Deadly import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, BOT_ID, BOT_NAME, 
                   OWNER_ID, app)

from Deadly.calls.Freya import (Plugin1, Plugin2, 
                                Plugin3, Plugin4)


loop = asyncio.get_event_loop()

async def initiate_bot():
    a = await app.get_chat_member(LOG_ID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot as Admin in Logger Channel")
        print(f"Stopping Bot")
        return
    print(f"Bot Started as {BOT_NAME}!")
    print(f"ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                LOG_ID,
                "<b>Congrats!! Assistant Client 1  has started successfully!</b>",
            )
        except Exception as e:
            print(
                "Assistant Account 1 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            print(f"Stopping Bot")
            return
        try:
            await ASS_CLI_1.join_chat("TheDeadlyBots")
            await ASS_CLI_1.join_chat("TheBotUpdates")
        except:
            pass
        print(f"Assistant 1 Started as {ASSNAME1}!")
        print(f"ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_ID,
                "<b>Congrats!! Assistant Client 2 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "Assistant Account 2 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            print(f"Stopping Bot")
            return
        try:
            await ASS_CLI_2.join_chat("TheDeadlyBots")
            await ASS_CLI_2.join_chat("TheBotUpdates")
        except:
            pass
        print(f"Assistant 2 Started as {ASSNAME2}!")
        print(f"ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_ID,
                "<b>Congrats!! Assistant Client 3 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "Assistant Account 3 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            print(f"Stopping Bot")
            return
        try:
            await ASS_CLI_3.join_chat("TheDeadlyBots")
            await ASS_CLI_3.join_chat("TheBotUpdates")
        except:
            pass
        print(f"Assistant 3 Started as {ASSNAME3}!")
        print(f"ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_ID,
                "<b>Congrats!! Assistant Client 4 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 4 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            print(f"Stopping Bot")
            return
        try:
            await ASS_CLI_4.join_chat("TheDeadlyBots")
            await ASS_CLI_4.join_chat("TheBotUpdates")
        except:
            pass
    print(f"Assistant 4 Started as {ASSNAME4}!")
    print(f"ID :- {ASSID4}!")
    print("Finalizing Booting...")
    print(f"Music Bot Boot Completed.")
    if STRING1 != "None":
        await Plugin1.start()
    if STRING2 != "None":
        await Plugin2.start()
    if STRING3 != "None":
        await Plugin3.start()
    if STRING4 != "None":
        await Plugin4.start()    
    await idle() 

    print(
        "Congrats!! Music Bot has started successfully!\n"
    )
    try:
        await app.send_message(
            LOG_ID,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )
    except Exception as e:
        print(
            "\nBot has failed to access the log Channel. Make sure that you have added your bot to your log channel and promoted as admin!"
        )
        print(f"Stopping Bot")
        return
   
if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
    
