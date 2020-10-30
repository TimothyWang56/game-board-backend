from flask import Blueprint, request, abort, jsonify, Response
from functools import wraps
from app.services.user import authenticate_user

league_api = Blueprint('league_api', __name__)

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers['Authorization']
        auth = authenticate_user(token)
        print("auth: ", auth)
        if (not auth['authorized']):
            return Response('Authorization failed', 401)
        return f(*args, **kwargs)
    return wrapper

@league_api.route('/<string:user_id>', methods=['GET'])
@authenticate
def getLeagueData(user_id):
    print(user_id)
    return jsonify({'hi': 'hi'}), 200