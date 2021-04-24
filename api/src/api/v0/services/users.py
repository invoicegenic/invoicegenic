'''
Users service
'''
from models import User
from flask import jsonify
from api.errors import not_found


def get_user(id: str):
    user = User.query.get(id)
    if user is None:
        return not_found('User is not found')

    return jsonify(user.to_dict())


def create_user():
    pass


def update_user(id):
    pass


def delete_user(id):
    pass
