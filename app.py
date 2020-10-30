from flask import Flask, request, abort, jsonify
from funcs.user_funcs import register_user, login_user

app = Flask(__name__)

@app.route('/register', methods = ['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if not register_user(username, password):
        abort(409)
    # potentially send a cookie to save info?
    return jsonify({ 'username': username }), 201

@app.route('/login', methods = ['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    token = login_user(username, password)
    if not token:
        abort(401) # existing user
    # potentially send a cookie to save info?
    return jsonify({ 'token': token }), 200

if __name__ == '__main__':
    app.run(debug=True)