import asyncio
import os
import time
from asyncio import QueueEmpty

from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import (AudioVideoPiped, InputAudioStream,
                                          InputStream)
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo,
                                                  LowQualityVideo,
                                                  MediumQualityVideo)
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded

from Deadly import STRING1, STRING2, STRING3, STRING4, get_queue
from Deadly import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4,
                   BOT_NAME, app)

from Deadly.core import Queues
from Deadly.converter import convert
from Deadly.database.assistantdb import *
from Deadly.database.voicechatdb import *

### Client
Plugin1 = PyTgCalls(ASS_CLI_1)
Plugin2 = PyTgCalls(ASS_CLI_2)
Plugin3 = PyTgCalls(ASS_CLI_3)
Plugin4 = PyTgCalls(ASS_CLI_4)

### Multi Assistant start



### admin cmd

async def pause_stream(chat_id: int):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await Plugin1.pause_stream(chat_id)
    elif int(assistant) == 2:
        await Plugin2.pause_stream(chat_id)
    elif int(assistant) == 3:
        await Plugin3.pause_stream(chat_id)
    elif int(assistant) == 4:
        await Plugin4.pause_stream(chat_id)


async def resume_stream(chat_id: int):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await Plugin1.resume_stream(chat_id)
    elif int(assistant) == 2:
        await Plugin2.resume_stream(chat_id)
    elif int(assistant) == 3:
        await Plugin3.resume_stream(chat_id)
    elif int(assistant) == 4:
        await Plugin4.resume_stream(chat_id)

async def stop_stream(chat_id: int):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if int(assistant) == 1:
        await Plugin1.leave_group_call(chat_id)
        await remove_active_chat(chat_id)
    elif int(assistant) == 2:
        await Plugin2.leave_group_call(chat_id)
        await remove_active_chat(chat_id)
    elif int(assistant) == 3:
        await Plugin3.leave_group_call(chat_id)
        await remove_active_chat(chat_id)
    elif int(assistant) == 4:
        await Plugin4.leave_group_call(chat_id)
        await remove_active_chat(chat_id)



# SKIPPING STREAM


keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data="cls"),
            ]
        ]
    )


async def skip_current_song(chat_id):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            if int(assistant) == 1:
               await Plugin1.leave_group_call(chat_id)
               await remove_active_chat(chat_id)
            if int(assistant) == 2:
               await Plugin2.leave_group_call(chat_id)
               await remove_active_chat(chat_id)
            if int(assistant) == 3:
               await Plugin3.leave_group_call(chat_id)
               await remove_active_chat(chat_id)
            if int(assistant) == 4:
               await Plugin4.leave_group_call(chat_id)
               await remove_active_chat(chat_id)
            clear_queue(chat_id)
            return 1
        else:
            try:
                songname = chat_queue[1][0]
                url = chat_queue[1][1]
                link = chat_queue[1][2]
                type = chat_queue[1][3]
                Q = chat_queue[1][4]
                if type == "Audio":
                    if int(assistant) == 1:
                       await Plugin1.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 2:
                       await Plugin2.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 3:
                       await Plugin3.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 4:
                       await Plugin4.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )                   
                elif type == "Video":
                    if Q == 720:
                        hm = HighQualityVideo()
                    elif Q == 480:
                        hm = MediumQualityVideo()
                    elif Q == 360:
                        hm = LowQualityVideo()
                    if int(assistant) == 1:
                       await Plugin1.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 2:
                       await Plugin2.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 3:
                       await Plugin3.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 4:
                       await Plugin4.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )     
                pop_an_item(chat_id)
                return [songname, link, type]
            except:
                if int(assistant) == 1:
                   await Plugin1.leave_group_call(chat_id)
                if int(assistant) == 2:
                   await Plugin2.leave_group_call(chat_id)
                if int(assistant) == 3:
                   await Plugin3.leave_group_call(chat_id)
                if int(assistant) == 4:
                   await Plugin4.leave_group_call(chat_id)
                clear_queue(chat_id)
                return 2
    else:
        return 0


async def skip_item(chat_id, h):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        try:
            x = int(h)
            songname = chat_queue[x][0]
            chat_queue.pop(x)
            return songname
        except Exception as e:
            print(e)
            return 0
    else:
        return 0



### QUEUE CLEARING
async def clear_queue(chat_id):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


### END STREAM. HANDLER

@Plugin1.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "Assistant left voice chat as no more queue or request found in the local playlist.")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass

@Plugin2.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "Assistant left voice chat as no more queue or request found in the local playlist.")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass

@Plugin3.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "Assistant left voice chat as no more queue or request found in the local playlist.")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass


@Plugin4.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "Assistant left voice chat as no more queue or request found in the local playlist.")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass

### ASSISTANT HANDLER ON KICK

@Plugin1.on_kicked()
async def kicked_handler1(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin2.on_kicked()
async def kicked_handler2(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin3.on_kicked()
async def kicked_handle3(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin4.on_kicked()
async def kicked_handler4(_, chat_id: int):
    await clear_queue(chat_id)


### ON PLAYBACK END


@Plugin1.on_closed_voice_chat()
async def closed_voice_chat_handler1(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin2.on_closed_voice_chat()
async def closed_voice_chat_handler2(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin3.on_closed_voice_chat()
async def closed_voice_chat_handler3(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin4.on_closed_voice_chat()
async def closed_voice_chat_handler4(_, chat_id: int):
    await clear_queue(chat_id)


### ON LEFTING GROUP/ VOICECHAT


@Plugin1.on_left()
async def left_handler1(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin2.on_left()
async def left_handler2(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin3.on_left()
async def left_handler3(_, chat_id: int):
    await clear_queue(chat_id)


@Plugin4.on_left()
async def left_handler4(_, chat_id: int):
    await clear_queue(chat_id)



