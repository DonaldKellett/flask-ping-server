from flask import Blueprint

version_blueprint = Blueprint('version', __name__, url_prefix='/version')

from . import routes
