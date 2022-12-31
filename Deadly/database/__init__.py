from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from Deadly import DB_URL
client = MongoClient(DB_URL)
dbd = client["Deadly"]
db = dbd

MONGODB_CLI = AsyncIOMotorClient(DB_URL)
dbb = MONGODB_CLI.program
