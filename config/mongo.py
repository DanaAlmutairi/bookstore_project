from pymongo import MongoClient
from django.conf import settings

_client = None

def get_reviews_collection():
    global _client
    if _client is None:
        _client = MongoClient(settings.MONGO_URI)
    db = _client[settings.MONGO_DB_NAME]
    return db[settings.MONGO_REVIEWS_COLLECTION]


