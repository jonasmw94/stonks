from flask_pymongo import PyMongo
from api.main import app
from bcrypt import gensalt, hashpw

mongo = PyMongo(app)

def validate_username(username: str) -> bool:
    user = get_user(username)

    if user != None:
        return False
    
    if len(username) < 3:
        return False

    return True

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False

    return True

def get_user(username: str) -> str:
    collection = mongo.db['users']
    user = collection.find_one({ 'user': username })
    return user

def insert_user(username: str, password: str) -> bool:
    if not validate_password(password) or not validate_username(username):
        return False
    
    salt = gensalt()
    hashedpw = hashpw(password.encode("utf-8"), salt)
    collection = mongo.db['users']
    collection.insert_one({ 'user': username, 'salt': salt, 'hashedpw': hashedpw })

    return True
