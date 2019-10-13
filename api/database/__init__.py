from flask_pymongo import PyMongo
from api.main import app

mongo = PyMongo(app)

def get_user(username: str) -> str:
    collection = mongo.db['user']
    user = collection.find_one({ 'user': username })
    return user

def insert_user(username: str) -> None:
    collection = mongo.db['user']
    collection.insert_one({ 'user': username })
    