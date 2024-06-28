from os import getenv

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = getenv('MONGODB_URL')
MONGODB_AUTH = getenv('MONGODB_AUTH')
CONNECT_STRING = f'mongodb+srv://{MONGODB_AUTH}@{MONGODB_URL}'
MONGODB_DATABASE = getenv('MONGODB_DATABASE')

def get_database():
    client = motor.motor_asyncio.AsyncIOMotorClient(CONNECT_STRING)
    database = client.get_database(MONGODB_DATABASE)
    return database

def get_collection(collection_name: str):
    database = get_database()
    return database.get_collection(collection_name)
