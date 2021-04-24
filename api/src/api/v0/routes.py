'''
API V0 routes
'''
from .services import users
from flask import Blueprint
from api import common as common_services


bp = Blueprint('api_v0', __name__)


# -----------------------------------------------------------------------------
# Users routes
# -----------------------------------------------------------------------------
@bp.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)


@bp.route('/users', methods=['POST'])
@bp.route('/users/<string:id>', methods=['PUT'])
@bp.route('/users/<string:id>', methods=['DELETE'])
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
