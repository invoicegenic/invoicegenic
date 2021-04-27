'''
Users service
'''
from flask import request, jsonify, url_for

from models import db, User
from api.errors import not_found, bad_request


def get_user(_id: str):
    user = User.query.get(_id)
    if user is None:
        return not_found('User is not found')
    if user.deleted_at is not None:
        return bad_request('User is already deleted')

    return jsonify(user.to_dict())


def create_user():
    payload = request.get_json() or {}

    if 'email' not in payload or 'password' not in payload:
        return bad_request('Either email or password is missing from the request data')

    user_exists = User.query.filter_by(email=payload['email']).first()
    if user_exists is not None:
        return bad_request('User with the same email is already registered')

    user = User()
    user.from_dict(payload, new_user=True)
    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('.get_user', _id=user.id)

    return response


def update_user(_id: str):
    user = User.query.get(_id)
    if user is None:
        return not_found('User is not found')

    payload = request.get_json() or {}
    user.from_dict(payload)
    db.session.commit()

    response = jsonify(user.to_dict())
    response.headers['Location'] = url_for('.get_user', _id=user.id)

    return response


def delete_user(_id: str):
    user = User.query.get(_id)
    if user is None:
        return not_found('User is not found')

    user.soft_delete()
    db.session.commit()

    response = jsonify(None)
    response.status_code = 204

    return response
