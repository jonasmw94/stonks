from flask_pymongo import PyMongo
from api.main import app

mongo = PyMongo(app)

def get_user(username: str) -> str:
    collection = mongo.db['users']
    user = collection.find_one({ 'user': username })
    return user

def insert_user(username: str) -> None:
    collection = mongo.db['users']
    collection.insert_one({ 'user': username })
    