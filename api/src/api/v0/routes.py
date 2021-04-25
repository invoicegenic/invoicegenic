'''
API V0 routes
'''
from flask import Blueprint

from api import common as common_services
from .services import users


bp = Blueprint('api_v0', __name__)


# -----------------------------------------------------------------------------
# Users routes
# -----------------------------------------------------------------------------
@bp.route('/users/<string:_id>', methods=['GET'])
def get_user(_id: str):
    return users.get_user(_id)


@bp.route('/users', methods=['POST'])
def create_user():
    return users.create_user()


@bp.route('/users/<string:_id>', methods=['PUT'])
@bp.route('/users/<string:_id>', methods=['DELETE'])
def test():
    pass


# -----------------------------------------------------------------------------
# Common routes
# -----------------------------------------------------------------------------
@bp.route('/')
def index():
    return common_services.index()


# @bp.errorhandler(500)
# def internal_error(error):
#     return errors.server_error('Failed to retrieving data due to server error')
