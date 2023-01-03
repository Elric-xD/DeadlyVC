
import random

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from config import COMMAND_PREFIXES as ASSISTANT_PREFIX, SUDO_USERS as SUDOERS
from Deadly import app, random_assistant
from Deadly.database import assistantdb
from Deadly.core.assistant import get_assistant_details

ASSISTANT_HELP = f"""
/checkassistant
- Check the alloted assistant of your chat
**Note:**
- Only for Sudo Users
{ASSISTANT_PREFIX[0]}block [ Reply to a User Message] 
- Blocks the User from Assistant Account.
{ASSISTANT_PREFIX[0]}unblock [ Reply to a User Message] 
- Unblocks the User from Assistant Account.
{ASSISTANT_PREFIX[0]}pfp [ Reply to a Photo] 
- Changes Assistant account PFP.
{ASSISTANT_PREFIX[0]}bio [Bio text] 
- Changes Bio of Assistant Account.
/changeassistant [ASS NUMBER]
- Change the previoius alloted assistant to new one.
/setassistant [ASS NUMBER or Random]
- Set a assistant account for chat. 
"""


ass_num_list = ["1", "2", "3", "4"]


@app.on_message(filters.command("changeassistant") & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**Usage:**\n/changeassistant [ASS_NO]\n\nSelect from them\n{' | '.join(ass_num_list)}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    num = message.text.split(None, 1)[1].strip()
    if num not in ass_num_list:
        return await message.reply_text(usage)
    ass_num = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /setassistant"
        )
    else:
        ass = _assistant["saveassistant"]
    assis = {
        "saveassistant": ass_num,
    }
    await save_assistant(message.chat.id, "assistant", assis)
    await message.reply_text(
        f"**Changed Assistant**\n\nChanged Assistant Account from **{ass}** to Assistant Number **{ass_num}**"
    )


ass_num_list2 = ["1", "2", "3", "4", "Random"]


@app.on_message(filters.command("setassistant") & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**Usage:**\n/setassistant [ASS_NO or Random]\n\nSelect from them\n{' | '.join(ass_num_list2)}\n\nUse 'Random' to set random Assistant"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    query = message.text.split(None, 1)[1].strip()
    if query not in ass_num_list2:
        return await message.reply_text(usage)
    if str(query) == "Random":
        ran_ass = random.choice(random_assistant)
    else:
        ran_ass = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        await message.reply_text(
            f"**__Yukki Music Bot Assistant Alloted__**\n\nAssistant No. **{ran_ass}**"
        )
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(message.chat.id, "assistant", assis)
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"Pre-Saved Assistant Number {ass} Found.\n\nYou can change Assistant Via /changeassistant"
        )


@app.on_message(filters.command("checkassistant") & filters.group)
async def check_ass(_, message: Message):
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /play"
        )
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"Pre-Saved Assistant Found\n\nAssistanty Number {ass} "
        )
