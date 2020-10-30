from flask import Blueprint, request, abort, jsonify, Response
from functools import wraps

league_api = Blueprint('league_api', __name__)

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        #todo - authenticate
        return f(*args, **kwargs)
    return wrapper
    