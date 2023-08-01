from flask import Blueprint

ping_blueprint = Blueprint('ping', __name__, url_prefix='/ping')

from . import routes
