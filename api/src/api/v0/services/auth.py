'''
'''
from flask import request, jsonify

from models import db, User


def login():
    payload = request.get_json()
    return payload


def logout():
    return 'logout'
