from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URL = getenv('MONGODB_URL')
MONGODB_DATABASE = getenv('MONGODB_DATABASE')

def get_database():
    client = MongoClient(MONGODB_URL)
    database = client.get_database(MONGODB_DATABASE)
    return database

def get_collection(collection_name: str):
    database = get_database()
    return database.get_collection(collection_name)
