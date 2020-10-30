from flask import Blueprint, request, abort, jsonify, Response
from functools import wraps
from app.services.user import authenticate_user
from app.services.league import league_data

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
def get_league_data(user_id):
    res = league_data(user_id)

    if (not res['success']):
        abort(401)

    return jsonify(res['data']), 200