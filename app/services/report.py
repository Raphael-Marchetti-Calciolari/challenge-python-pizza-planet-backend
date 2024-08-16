from app.common.http_methods import GET
from flask import Blueprint

from ..controllers import ReportController

from .base_service import BaseService

report = Blueprint('report', __name__)


@report.route('/months', methods=GET)
def get_months_report():
    return BaseService.check_response(*ReportController.get_report_per_month())


@report.route('/ingredients', methods=GET)
def get_ingredients_report():
    return BaseService.check_response(*ReportController.get_ordered_ingredients_count())


@report.route('/customers', methods=GET)
def get_customers_report():
    return BaseService.check_response(*ReportController.get_costumers_order_count())


@report.route('/weekdays', methods=GET)
def get_weekdays_report():
    return BaseService.check_response(*ReportController.get_report_per_weekday())


@report.route('/hours', methods=GET)
def get_hours_report():
    return BaseService.check_response(*ReportController.get_report_per_hours())