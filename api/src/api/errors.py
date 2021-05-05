'''
Errors module
'''
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
# from werkzeug.exceptions import HTTPException


def error_response(status_code, message=None):
    payload = {
        'code': status_code,
        'error_name': HTTP_STATUS_CODES.get(status_code, 'Unknown error'),
    }
    if message:
        payload['message'] = message

    response = jsonify(payload)
    response.status_code = status_code

    return response


def bad_request(message):
    return error_response(400, message)


def not_found(message):
    return error_response(404, message)


def gone(message):
    return error_response(410, message)


def unauthorized(message):
    return error_response(401, message)


# def server_error(message):
#     return error_response(500, message)

def server_error(_):
    return error_response(500, 'Failed to retrieving data due to server error')
