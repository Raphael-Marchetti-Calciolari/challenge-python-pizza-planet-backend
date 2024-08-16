from flask import jsonify, Request
from ..controllers.base import BaseController
from typing import Tuple, Any

class BaseService:
    def create(request: Request, controller: BaseController):
        return BaseService.check_response(*controller.create(request.json))


    def update(request: Request, controller: BaseController):
        return BaseService.check_response(*controller.update(request.json))


    def delete_by_id(_id: int, controller: BaseController):
        return BaseService.check_response(*controller.delete(_id))


    def get_by_id(_id: int, controller: BaseController):
        return BaseService.check_response(*controller.get_by_id(_id))


    def get_all(controller: BaseController):
        return BaseService.check_response(*controller.get_all())
    

    def check_response(data: Tuple[Any, str], error):
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code
