from app.common.http_methods import GET, POST, PUT, DELETE
from flask import Blueprint, jsonify, request

from ..controllers import SizeController

from .base_service import BaseService

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return BaseService.create(request, SizeController)


@size.route('/', methods=PUT)
def update_size():
    return BaseService.update(request, SizeController)


@size.route('/id/<_id>', methods=DELETE)
def delete_size_by_id(_id: int):
    return BaseService.delete_by_id(_id, SizeController)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return BaseService.get_by_id(_id, SizeController)


@size.route('/', methods=GET)
def get_sizes():
    return BaseService.get_all(SizeController)