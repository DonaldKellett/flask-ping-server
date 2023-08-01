from flask import Flask
from project.ping import ping_blueprint
from project.version import version_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ping_blueprint)
    app.register_blueprint(version_blueprint)
    return app
