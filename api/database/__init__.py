from flask_pymongo import PyMongo
from api.main import app

mongo = PyMongo(app)