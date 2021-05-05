'''
API V0 routes
'''
from flask import Blueprint, abort

from api import common as common_services
from .services import users, auth as auth_svc


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
def update_user(_id: str):
    return users.update_user(_id)


@bp.route('/users/<string:_id>', methods=['DELETE'])
def delete_user(_id: str):
    return users.delete_user(_id)


# -----------------------------------------------------------------------------
# Auth routes
# -----------------------------------------------------------------------------
@bp.route('/auth/<string:auth_type>', methods=['POST'])
def auth(auth_type: str):
    if auth_type == 'login':
        return auth_svc.login()
    elif auth_type == 'logout':
        return auth_svc.logout()
    else:
        abort(404)


# -----------------------------------------------------------------------------
# Common routes
# -----------------------------------------------------------------------------
@bp.route('/')
def index():
    return common_services.index()


# @bp.errorhandler(500)
# def internal_error(error):
#     return errors.server_error('Failed to retrieving data due to server error')
