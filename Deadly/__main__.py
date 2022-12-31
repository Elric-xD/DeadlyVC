import asyncio
from pytgcalls import idle
from Deadly import (
ASSISTANT_1, call_py1,
ASSISTANT_2, call_py2,
ASSISTANT_3, call_py3,
ASSISTANT_4, call_py4,
ASSISTANT_5, call_py5,
ASSISTANT_6, call_py6,
ASSISTANT_7, call_py7, 
bot
) 



async def start_bot():
    print("[INFO]: Starting Freya Music. . .")
    await bot.start()
    await bot.send_message(LOG_ID, "Starting Assistant Client. . ") 
# STARTING CLIENT1
    if STRING1 != "None":
       await ASSISTANT_1.start()
       await call_py1.start()
       await ASSISTANT_1.send_message(LOG_ID, "Assistant One Successfully Started as {ASS_NAME1}") 
       MULTI_ASSISTANT.append(1)
# STARTING CLIENT2
    if STRING2 != "None":
       await ASSISTANT_2.start()
       await call_py2.start()
       await ASSISTANT_2.send_message(LOG_ID, "Assistant Two Successfully Started as {ASS_NAME2}") 
       MULTI_ASSISTANT.append(2)
# STARTING CLIENT3
    if STRING3 != "None":
       await ASSISTANT_3.start()
       await call_py3.start()
       await ASSISTANT_3.send_message(LOG_ID, "Assistant Three Started as {ASS_NAME3}") 
       MULTI_ASSISTANT.append(3)
# STARTING CLIENT4
    if STRING4 != "None":
       await ASSISTANT_4.start()
       await call_py4.start()
       await ASSISTANT_4.send_message(LOG_ID, "Assistant Four  Started as {ASS_NAME4}") 
       MULTI_ASSISTANT.append(4)
# STARTING CLIENT5
    if STRING5 != "None":
       await ASSISTANT_5.start()
       await call_py5.start()
       await ASSISTANT_5.send_message(LOG_ID, "Assistant Five  Started as {ASS_NAME5}") 
       MULTI_ASSISTANT.append(5)    
# STARTING CLIENT6
    if STRING6 != "None":
       await ASSISTANT_6.start()
       await call_py6.start()
       await ASSISTANT_6.send_message(LOG_ID, "Assistant Six Successfully Started as {ASS_NAME6}") 
       MULTI_ASSISTANT.append(6)
# STARTING CLIENT 7
    if STRING7 != "None":
       await ASSISTANT_7.start()
       await call_py7.start() 
       await ASSISTANT_7.send_message(LOG_ID, "Assistant Seven  Started as {ASS_NAME7}") 
       MULTI_ASSISTANT.append(7)
    print("[INFO]: Your MusicBot Has been started")
    await idle()
    await bot.send_message(LOG_ID, "Your Music Bot Successfully Started") 


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
