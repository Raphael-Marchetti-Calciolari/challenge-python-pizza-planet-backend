from app.common.http_methods import GET, DELETE
from flask import Blueprint

from ..controllers import MockController

from .base_service import BaseService

mock = Blueprint('mock', __name__)


@mock.route('/', methods=GET)
def fill_mock_data():
    return BaseService.check_response(*MockController.fill_mock_data())


@mock.route('/', methods=DELETE)
def clear_mock_data():
    return BaseService.check_response(*MockController.clear_mock_data())