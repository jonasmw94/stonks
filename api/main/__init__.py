from flask import Flask, jsonify, request, make_response
import datetime
import markdown
import os
from api.token import generate_token, decode_token, token_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRET!!!!!!!!'

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

    if auth and auth.password == 'password':
        return generate_token(auth.username, app.config['SECRET_KEY'])
    return make_response('Could not verify!', 401, { 'WWW-Authenticate' : 'Basic realm="Login required"' })