import motor.motor_asyncio
from .env import *

MONGO_DETAILS = "mongodb://{}:{}@{}:{}".format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, serverSelectionTimeoutMS=SERVER_SELECTION_TIMEOUT_MS)

database = client["{}".format(DB_DATABASE)]
