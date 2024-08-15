from app.common.http_methods import GET, POST, PUT, DELETE
from flask import Blueprint, jsonify, request

from ..controllers import OrderController

from .base_service import BaseService

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    order, error = OrderController.create(request.json)
    response = order if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@order.route('/', methods=PUT)
def update_order():
    return BaseService.update(request, OrderController)


@order.route('/id/<_id>', methods=DELETE)
def delete_order_by_id(_id: int):
    return BaseService.delete_by_id(_id, OrderController)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return BaseService.get_by_id(_id, OrderController)


@order.route('/', methods=GET)
def get_orders():
    return BaseService.get_all(OrderController)