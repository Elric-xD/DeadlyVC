

import io
from os import path
from typing import Callable
from asyncio.queues import QueueEmpty
import os
import random
import re
import youtube_dl
import youtube_dl
import aiofiles
import aiohttp
from Deadly.converter import convert
import ffmpeg
import requests
from Deadly.core.fonts import CHAT_TITLE
from PIL import Image, ImageDraw, ImageFont
from Deadly.core.filters import command, other_filters
from Deadly.core import Queues 
from Deadly.calls import Freya
from Deadly.database.voicechatdb import *
from Deadly.core.utils import bash
from Deadly import bot as Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.types import Update
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioImagePiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import MediumQualityVideo
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch
from Deadly.core.thumbnail import gen_thumb as play_thumb, gen_qthumb as queue_thumb
from Deadly.core.keyboard import stream_markup, audio_markup
from Deadly import BOT_USERNAME, IMG_1, IMG_2, IMG_3, IMG_4, IMG_5, ASSISTANT_USERNAME

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format: str, link: str):
    stdout, stderr = await bash(f'yt-dlp --geo-bypass -g -f "[height<=?720][width<=?1280]" {link}')
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr

chat_id = None
DISABLED_GROUPS = []
useer = "NaN"
ACTV_CALLS = []

    
@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(c: Client, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    buttons = audio_markup(user_id)
    if m.sender_chat:
        return await m.reply_text("You're an __Anonymous__ Admin !\n\n» revert back to user account from admin rights.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"Error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 To use me, I need to be an **Administrator** with the following **permissions**:\n\n» ❌ __Delete messages__\n» ❌ __Add users__\n» ❌ __Manage video chat__\n\nData is **updated** automatically after you **promote me**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "Missing required permission:" + "\n\n» ❌ __Manage video chat__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "Missing required permission:" + "\n\n» ❌ __Delete messages__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("Missing required permission:" + "\n\n» ❌ __Add users__")
        return
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("Dᴏᴡɴʟᴏᴀᴅɪɴɢ..Pʟᴇᴀsᴇ Wᴀɪᴛ..!! 🍁💫")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else: 
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(  
                    photo="{IMG_1}",              
                    caption=f"⏳ Added to Queue at **#{pos}**\n\n💡Title: [{songname}]({link})\n\n\n👤Added By: {m.from_user.mention()}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
            else:
             try:
                if int(assistant) == 1:
                   await Plugin1.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 2:
                   await Plugin2.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 3:
                   await Plugin3.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                if int(assistant) == 4:
                   await Plugin4.join_group_call(
                       chat_id,
                       AudioPiped(
                           dl,
                       ),
                       stream_type=StreamType().local_stream,
                   )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(  
                    photo=f"{IMG_4}",        
                    caption=f"📡 Started Streaming 💡\n\n💡Title: [{songname}]({link})\n\n👤Added By: {requester}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
                await add_active_chat(chat_id)
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"🚫 error:\n\n» {e}")
        
    else:
        if len(m.command) < 2:
         await m.reply_photo(
                     photo="https://te.legra.ph/file/ffe011a199e84c329d265.jpg",
                    caption="Usage: /play [Music Name or Youtube Link or Reply to Audio]\n\nIf you want to play Music you need to Add bot as Admin.",
                      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Support🌐", url=f"https://t.me/TheDeadlyBots"),
                            InlineKeyboardButton("Channel🛰", url=f"https://t.me/TheBotUpdates"),
                        ], 
                        [                            
                            InlineKeyboardButton("Close🗑", callback_data="cls")
                        ]
                    ]
                )
            )
        else:
            suhu = await m.reply_text(         
        f"Sᴇᴀʀᴄʜɪɴɢ...Pʟᴇᴀsᴇ Wᴀɪᴛ...!! 🍁💫"
    )
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("Fᴀɪʟᴇᴅ Tᴏ Pʀᴏᴄᴇss Qᴜᴇʀʏ...!!")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                gcname = m.chat.title
                videoid = search[4]
                dlurl = f"https://www.youtubepp.com/watch?v={videoid}"
                info = f"https://t.me/{BOT_USERNAME}?start=info_{videoid}"
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                keyboard = stream_markup(user_id, videoid)
                playimg = await play_thumb(videoid)
                queueimg = await queue_thumb(videoid)
                format = "bestaudio"
                abhi, ytlink = await ytdl(format, url)
                if abhi == 0:
                    await suhu.edit(f"💬 yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=queueimg,
                            caption=f"⏳ Added to Queue at **#{pos}**\n\n💡Title: [{title}]({info})\n⏰ Duration: {duration}\n👤Added By: {requester}",
                            reply_markup=InlineKeyboardMarkup(keyboard),
                        )
                    else:
                        try:
                            if int(assistant) == 1:
                               await Plugin1.join_group_call(
                                   chat_id,
                                   AudioImagePiped(
                                             ytlink,
                                             playimg,
                                   video_parameters=HighQualityVideo(),
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 2:
                               await Plugin2.join_group_call(
                                   chat_id,
                                   AudioImagePiped(
                                             ytlink,
                                             playimg,
                                   video_parameters=HighQualityVideo(),
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                             if int(assistant) == 3:
                               await Plugin3.join_group_call(
                                   chat_id,
                                   AudioImagePiped(
                                             ytlink,
                                             playimg,
                                   video_parameters=HighQualityVideo(),
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            if int(assistant) == 4:
                               await Plugin4.join_group_call(
                                   chat_id,
                                   AudioImagePiped(
                                             ytlink,
                                             playimg,
                                   video_parameters=HighQualityVideo(),
                                   ),
                                   stream_type=StreamType().local_stream,
                               )
                            await m.reply_photo(
                                photo=playimg,
                                caption=f"📡 Started Streaming 💡\n\n💡Title: [{title}]({info})\n⏰ Duration: {duration}\n👤Added By: {requester}",
                                reply_markup=InlineKeyboardMarkup(keyboard),
                            )
                            await suhu.delete()
                            await add_active_chat(chat_id)
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"💬 error: `{ep}`")
                            
# STATUS CHECK

@Client.on_message(command(["maxvc", f"maxvc@{BOT_USERNAME}"]) & other_filters)
async def get_play_status(client: Client, message: Message):
    await message.delete()
    bc = call_py.get_max_voice_chat()
    await message.reply_text(f"Max VoiceChat Allowed: {bc}")

