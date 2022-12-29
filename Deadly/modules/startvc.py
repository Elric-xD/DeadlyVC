from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram import filters, Client
from Deadly import BOT_USERNAME
from Deadly.core.decorators import authorized_users_only
from pyrogram.types import (
    CallbackQuery,
    Message,
)


@Client.on_message(command([f"startvc@{BOT_USERNAME}", "startvc"]) & other_filters)
@authorized_users_only
async def createcall(client, message):
    await message.delete() 
    flags = " ".join(message.command[1:])
    semx = await message.reply_text("`Processing...`")
    if flags == "channel":
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    try:
        await client.send(
            CreateGroupCall(
                peer=(await client.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
            )
        )
        await semx.edit(f"Started group call in **Chat ID** : `{chat_id}`")
    except Exception as e:
        await semx.edit(f"**INFO:** `{e}`")

"""
From program docs
"""
