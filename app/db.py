from pymongo import MongoClient
from config import settings


def get_mongo_db():
    client = MongoClient(settings.MONGO_DB_URI)
    db = client[settings.MONGO_DATABASE]
    yield db
    client.close()
