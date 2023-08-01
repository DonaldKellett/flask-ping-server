from . import version_blueprint
from flask import Response
import json

APP_VERSION='0.0.1'

@version_blueprint.route('/')
def get_app_version():
    return Response(json.dumps({ "version": APP_VERSION }), mimetype='application/json')
