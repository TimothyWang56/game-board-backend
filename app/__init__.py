from flask import Flask
from flask_cors import CORS
from app.routes import auth_routes, league_routes

def create_app():
    app = Flask(__name__)
    cors = CORS(app, supports_credentials=True)
    app.register_blueprint(auth_routes.auth_api, url_prefix='/auth')
    app.register_blueprint(league_routes.league_api, url_prefix='/leagues')
    return app