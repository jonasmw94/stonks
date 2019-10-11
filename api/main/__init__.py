from flask import Flask, jsonify, request, make_response
import jwt
import datetime
import markdown
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRET!!!!!!!!'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({ 'message': 'Token is missing' }), 403
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({ 'message': 'Token is invalid' }), 403

        return f(*args, **kwargs)

    return decorated


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
        token = jwt.encode({ 'user': auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})
    return make_response('Could not verify!', 401, { 'WWW-Authenticate' : 'Basic realm="Login required"' })