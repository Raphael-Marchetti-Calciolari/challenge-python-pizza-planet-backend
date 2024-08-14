from app.common.http_methods import GET, DELETE
from flask import Blueprint, jsonify, request

from ..controllers import MockController

mock = Blueprint('mock', __name__)


@mock.route('/', methods=GET)
def fill_mock_data():
    res, error = MockController.fill_mock_data()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code


@mock.route('/', methods=DELETE)
def clear_mock_data():
    res, error = MockController.clear_mock_data()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code