from app.common.http_methods import GET
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/months', methods=GET)
def get_months_report():
    res, error = ReportController.get_report_per_month()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/ingredients', methods=GET)
def get_ingredients_report():
    res, error = ReportController.get_ordered_ingredients_count()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/customers', methods=GET)
def get_customers_report():
    res, error = ReportController.get_costumers_order_count()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/weekdays', methods=GET)
def get_weekdays_report():
    res, error = ReportController.get_report_per_weekday()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/hours', methods=GET)
def get_hours_report():
    res, error = ReportController.get_report_per_hours()
    response = res if not error else {'error': error}
    status_code = 200 if res else 404 if not error else 400
    return jsonify(response), status_code