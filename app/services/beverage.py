from app.common.http_methods import GET, POST, PUT, DELETE
from flask import Blueprint, request

from ..controllers import BeverageController

from .base_service import BaseService

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    return BaseService.create(request, BeverageController)


@beverage.route('/id/<_id>', methods=PUT)
def update_beverage():
    return BaseService.update(request, BeverageController)


@beverage.route('/id/<_id>', methods=DELETE)
def delete_beverage_by_id(_id: int):
    return BaseService.delete_by_id(_id, BeverageController)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return BaseService.get_by_id(_id, BeverageController)


@beverage.route('/', methods=GET)
def get_beverages():
    return BaseService.get_all(BeverageController)
