import sys
from pyrogram import Client
from Deadly import STRING1, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7
assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING5),
            no_updates=True,
        )
        self.six = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING6),
            no_updates=True,
        )
         self.seven = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING7),
            no_updates=True,
        )

    async def start(self):
        print("Starting Assistant.")  
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("TheDeadlyBots")
                await self.one.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(1) 
            get_me = await self.one.get_me()
            self.one.name = get_me.first_name
            try:
                await self.one.send_message(
                    config.LOG_ID, f"Assistant one Started as {self.one.name}"
                )
            except:
                print(f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!")
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            print(f"Assistant Started as {self.one.name}")
# STRING 2
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("TheDeadlyBots")
                await self.two.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(2) 
            get_me = await self.two.get_me()
            self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    LOG_ID, f"Assistant Two Started as {self.two.name}"
                )
            except:
                print(f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! ")
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            print(f"Assistant Two Started as {self.two.name}")
# STRING 3
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("TheDeadlyBots")
                await self.three.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    LOG_ID, f"Assistant Three Started as {self.three.name}"
                )
            except:
                print(f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! ") 
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            print(f"Assistant Three Started as {self.three.name}")
# STRING 4
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("TheDeadlyBots")
                await self.four.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    LOG_ID, f"Assistant Four Started as {self.four.name}"
                )
            except:
                print(f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! ")
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            print(f"Assistant Four Started as {self.four.name}")
# STRING 5
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("TheDeadlyBots")
                await self.five.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    LOG_ID, f"Assistant Five Started as {self.five.name}"
                )
            except:
                print(f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! ")
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            print(f"Assistant Five Started as {self.four.name}")

# STRING 6
        if config.STRING6:
            await self.six.start()
            try:
                await self.six.join_chat("TheDeadlyBots")
                await self.six.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(6)
            get_me = await self.six.get_me()
            self.six.name = get_me.first_name
            try:
                await self.six.send_message(
                    LOG_ID, f"Assistant Six Started as {self.six.name}"
                )
            except:
                print(f"Assistant Account 6 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! ")
                sys.exit()
            get_me = await self.six.get_me()
            self.six.username = get_me.username
            self.six.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.six.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.six.name = get_me.first_name
            print(f"Assistant Six Started as {self.four.name}")
# STRING 7
        if config.STRING7:
            await self.seven.start()
            try:
                await self.seven.join_chat("TheDeadlyBots")
                await self.seven.join_chat("TheBotUpdates")
            except:
                pass
            assistants.append(7)
            get_me = await self.seven.get_me()
            self.seven.name = get_me.first_name
            try:
                await self.seven.send_message(
                    LOG_ID, f"Assistant Seven Started as {self.seven.name}"
                )
            except:
                print(f"Assistant Account 7 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! ")
                sys.exit()
            get_me = await self.seven.get_me()
            self.seven.username = get_me.username
            self.seven.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.seven.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.seven.name = get_me.first_name
            print(f"Assistant Seven Started as {self.four.name}")
