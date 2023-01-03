
from inspect import getfullargspec
from pyrogram import Client, filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from Deadly import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4,
                   BOT_ID, BOT_USERNAME, LOG_ID, GROUP_SUPPORT
                   BOT_NAME, SUDO_USERS, app)

flood = {}



@Client.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client, message):
    chat_id = message.chat.id
    await client.send_message(
        message.chat.id,
        f"Hi there, This is a music assistant service .\n\n❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here\nJoin Our Support: @{GROUP_SUPPORT}\n\n",
    )
    return

@Client.on_message(
    filters.command("block", prefixes=".")
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def block_user_func(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user's message to block.")
    user_id = message.reply_to_message.from_user.id
    await message.reply_text("Successfully blocked the user")
    await client.block_user(user_id)


@Client.on_message(
    filters.command("unblock", prefixes=".")
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def unblock_user_func(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user's message to unblock.")
    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await message.reply_text("Successfully unblocked the user")


@Client.on_message(
    filters.command("pfp", prefixes=".")
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_pfp(client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text("Reply to a photo.")
    photo = await message.reply_to_message.download()
    try:
        await client.set_profile_photo(photo=photo)
        await message.reply_text("Successfully Changed PFP.")
    except Exception as e:
        await message.reply_text(f"**ERROR**: {e}")


@Client.on_message(
    filters.command("bio", prefixes=".")
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_bio(client, message):
    if len(message.command) == 1:
        return await message.reply_text("Give some text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await message.reply_text("Changed Bio.")
        except Exception as e:
            await message.reply_text(f"**ERROR**: {e}")
    else:
        return await message.reply_text("Give some text to set as bio.")
