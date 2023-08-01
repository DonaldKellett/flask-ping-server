from . import ping_blueprint
from flask import Response
import json

@ping_blueprint.route('/')
def pong():
    return Response(json.dumps({ "message": "pong" }), mimetype='application/json')
