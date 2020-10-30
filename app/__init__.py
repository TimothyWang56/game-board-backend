from flask import Flask
from app.routes import auth_routes, league_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_routes.auth_api, url_prefix='/auth')
    app.register_blueprint(league_routes.league_api, url_prefix='/leagues')
    return app