import asyncio
from pytgcalls import idle
from Deadly import *



loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
