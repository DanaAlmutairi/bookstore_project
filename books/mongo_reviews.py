from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["bookstore_reviews"]
reviews_collection = db["reviews"]

def add_review(book_id, user, rating, comment):
    doc = {
        "book_id": int(book_id),
        "user": user,
        "rating": int(rating),
        "comment": comment,
        "created_at": datetime.utcnow(),
    }
    reviews_collection.insert_one(doc)
    doc.pop("_id", None)
    # Convert datetime to string for JSON
    doc["created_at"] = doc["created_at"].isoformat() + "Z"
    return doc

def get_reviews(book_id):
    reviews = list(
        reviews_collection.find(
            {"book_id": int(book_id)},
            {"_id": 0}
        ).sort("created_at", -1)
    )   
    # Convert datetime to string for JSON
    for r in reviews:
        if "created_at" in r and hasattr(r["created_at"], "isoformat"):
            r["created_at"] = r["created_at"].isoformat() + "Z"
    return reviews