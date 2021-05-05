'''
'''
# from flask import current_app, jsonify


def index(version: str = 'v0'):
    '''
    Return API version to client.

    Params:
        str version: Version to be returned. Default is "v0"
    '''
    return f'<pre>InvoiceGenic API {version}</pre>'
