from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient

from utils.logger import get_logger

load_dotenv()

MONGODB_URL = getenv('MONGODB_URL')
MONGODB_DATABASE = getenv('MONGODB_DATABASE')

logger = get_logger(__name__)

def get_database():
    client = MongoClient(MONGODB_URL)
    database = client.get_database(MONGODB_DATABASE)
    return database

def get_collection(collection_name: str):
    database = get_database()
    return database.get_collection(collection_name)

def migrate():
    database = get_database()

    turnover_collection = database.get_collection('turnover')
    logger.info('Check index date_1 on turnover')
    if 'date_1' not in turnover_collection.index_information():
        logger.info('Create index date_1 on turnover')
        turnover_collection.create_index('date', unique=True)
