from app.common.http_methods import GET
from flask import Blueprint, jsonify, request

from ..controllers import MockController

mock = Blueprint('mock', __name__)


@mock.route('/', methods=GET)
def populate_database():
    print("Received request on service mock")
    res, error = MockController.populate_database()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code
