from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

from Deadly import DB_URI

_mongo_async_ = _mongo_client_(DB_URI)
_mongo_sync_ = MongoClient(DB_URI)
mongodb = _mongo_async_.Deadly
pymongodb = _mongo_sync_.Deadly
