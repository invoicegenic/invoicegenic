from api.v0 import bp


@bp.route('/')
def index():
    return '<pre>InvoiceGenic API v0</pre>'
