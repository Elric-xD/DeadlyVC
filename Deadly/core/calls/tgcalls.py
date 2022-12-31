

import asyncio
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from Deadly import bot as app



class Call(PyTgCalls):
    def __init__(self):
        self.userbot1 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING1),
        )
        self.one = PyTgCalls(
            self.userbot1,
            cache_duration=100,
        )
        self.userbot2 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING2),
        )
        self.two = PyTgCalls(
            self.userbot2,
            cache_duration=100,
        )
        self.userbot3 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING3),
        )
        self.three = PyTgCalls(
            self.userbot3,
            cache_duration=100,
        )
        self.userbot4 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING4),
        )
        self.four = PyTgCalls(
            self.userbot4,
            cache_duration=100,
        )
        self.userbot5 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING5),
        )
        self.five = PyTgCalls(
            self.userbot5,
            cache_duration=100,
        )
        self.userbot6 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING6),
        )
        self.six = PyTgCalls(
            self.userbot6,
            cache_duration=100,
        )
        self.userbot7 = Client(
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=str(STRING7),
        )
        self.seven = PyTgCalls(
            self.userbot7,
            cache_duration=100,
        )
        

Freya = Call()
