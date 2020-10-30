from flask import Blueprint, request, abort, jsonify, Response
from app.services.user import register_user, login_user

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/register', methods = ['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if not register_user(username, password):
        abort(409)
    # potentially send a cookie to save info?
    return jsonify({ 'username': username }), 201

@auth_api.route('/login', methods = ['POST'])
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
