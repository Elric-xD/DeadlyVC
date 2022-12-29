"""
async def createcall(client, message):
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
