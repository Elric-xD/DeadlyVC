import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

from Deadly import BOT_NAME, bot as app
loop = asyncio.get_running_loop()


@app.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_comm(client, message: Message, _):
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**Video Track Information**__
❇️**Title:** {title}
⏳**Duration:** {duration} Mins
👀**Views:** `{views}`
⏰**Published Time:** {published}
🎥**Channel Name:** {channel}
📎**Channel Link:** [Visit From Here]({channellink})
🔗**Video Link:** [Link]({link})
⚡️ __Searched Powered By {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch ", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🔄 Close", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            await app.send_message(
                LOG_ID,
               f"{message.from_user.mention} has just started bot to check <code>VIDEO INFORMATION</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
