from flask import jsonify, request
import jwt
import datetime
from functools import wraps
from main.main_app import app

def generate_token(username: str, secret: str) -> str:
    return jwt.encode({ 'user': username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=10) }, secret, algorithm='HS256').decode('UTF-8')

def decode_token(token, secret):
    return jwt.decode(token, secret, algorithms=['HS256'])

def jsonify_token_response(token):
    return jsonify({'token' : token})

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({ 'message': 'Token is missing' }), 403
        
        try:
            decode_token(token, app.config['SECRET_KEY'])
        except:
            return jsonify({ 'message': 'Token is invalid' }), 403

        return f(*args, **kwargs)

    return decorated