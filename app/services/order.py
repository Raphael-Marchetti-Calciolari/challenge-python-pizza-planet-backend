from app.common.http_methods import GET, POST, PUT, DELETE
from flask import Blueprint, request

from ..controllers import OrderController

from .base_service import BaseService

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return BaseService.check_response(*OrderController.create(request.json))


@order.route('/id/<_id>', methods=PUT)
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