'''API V0 module'''
from flask import Blueprint

bp = Blueprint('api_v0', __name__)

from api.v0 import routes
