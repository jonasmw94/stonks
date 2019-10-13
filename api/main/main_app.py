from flask import Flask, jsonify, request, make_response
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRET!!!!!!!!'
app.config["MONGO_URI"] = "mongodb://localhost:27017/stonks"

import datetime
import markdown
import os
from token_handler.utils import generate_token, decode_token, jsonify_token_response, token_required
from database.utils import check_user_login



app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRET!!!!!!!!'
app.config["MONGO_URI"] = "mongodb://localhost:27017/stonks"

@app.route("/")
def index():
    ''' Present some documentation'''
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

@app.route('/protected')
@token_required
def protected_route():
    return jsonify({ 'message': 'Only valid tokens :))))' })

@app.route('/login')
def login():
    auth = request.authorization

    if auth:
        user = check_user_login(auth.username, auth.password)

        if user != None:
            return jsonify_token_response(generate_token(auth.username, app.config['SECRET_KEY']))
    return make_response('Could not verify!', 401, { 'WWW-Authenticate' : 'Basic realm="Login required"' })