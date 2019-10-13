from flask import Flask, jsonify, request, make_response
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRET!!!!!!!!'
app.config["MONGO_URI"] = "mongodb://localhost:27017/stonks"

import datetime
import markdown
import os
from token_handler.utils import generate_token, decode_token, jsonify_token_response, token_required
from database.utils import check_user_login, insert_user
import json



app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRET!!!!!!!!'
app.config["MONGO_URI"] = "mongodb://localhost:27017/stonks"

@app.route("/", methods=['GET'])
def index():
    ''' Present some documentation'''
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

@app.route("/register", methods=['PUT'])
def register_user():
    if not request.is_json:
        return make_response('Could not execute!', 401)

    request_body = request.get_json()
    res = insert_user(request_body['username'], request_body['password'])

    if not res:
        return make_response('Could not execute!', 401)

    return make_response('', 204)


@app.route('/protected', methods=['GET'])
@token_required
def protected_route():
    return jsonify({ 'message': 'Only valid tokens :))))' })

@app.route('/login', methods=['POST'])
def login():
    body = request.json


    if body != None:
        user = check_user_login(body['username'], body['password'])

        if user != None:
            return jsonify_token_response(generate_token(body['username'], app.config['SECRET_KEY']))
    return make_response('Could not verify!', 401, { 'WWW-Authenticate' : 'Basic realm="Login required"' })