from .base import BaseManager
from .order import OrderManager
from datetime import datetime

class ReportManager(BaseManager):
    @classmethod
    def get_report_per_month(cls):
        orders = OrderManager.get_all()
        rev_per_month = {}
        for order in orders:
            if 'date' not in order: continue
            month = datetime.strptime(
                order['date'],"%Y-%m-%dT%H:%M:%S.%f").month
            revenue = order['total_price']
            if month not in rev_per_month:
                rev_per_month[month] = {
                    'revenue': revenue,
                    'orders': 1
                }
            else:
                rev_per_month[month] = {
                    'revenue': rev_per_month[month]['revenue'] + revenue,
                    'orders': rev_per_month[month]['orders'] + 1
                }
        for month in rev_per_month:
            rev_per_month[month]['revenue'] = round(rev_per_month[month]['revenue'], 2)
        return rev_per_month

    @classmethod
    def get_ordered_ingredients_count(cls):
        orders = OrderManager.get_all()
        ingredients_count = {}
        for order in orders:
            if 'ingredient_detail' not in order: continue
            for detail in order['ingredient_detail']:
                if 'ingredient' in detail:
                    ingredient = detail['ingredient']
                    if not ingredient: continue
                    if ingredient['name'] not in ingredients_count:
                        ingredients_count[ingredient['name']] = 1
                    else:
                        ingredients_count[ingredient['name']] += 1
        return ingredients_count

    @classmethod
    def get_costumers_order_count(cls):
        orders = OrderManager.get_all()
        costumers_count = {}
        for order in orders:
            if 'client_name' not in order: continue
            client_name = order['client_name']
            if client_name not in costumers_count:
                costumers_count[client_name] = 1
            else:
                costumers_count[client_name] += 1
        return costumers_count

    @classmethod
    def get_report_per_weekday(cls):
        orders = OrderManager.get_all()
        weekdays = [
            'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]
        orders_per_date = {}
        for order in orders:
            if 'date' not in order: continue
            weekday = weekdays[datetime.strptime(
                order['date'],"%Y-%m-%dT%H:%M:%S.%f").weekday()]
            if weekday not in orders_per_date:
                orders_per_date[weekday] = {
                    'revenue': order['total_price'],
                    'orders': 1
                }
            else:
                orders_per_date[weekday] = {
                    'revenue': orders_per_date[weekday]['revenue'] + order['total_price'],
                    'orders': orders_per_date[weekday]['orders'] + 1
                }
        for weekday in orders_per_date:
            orders_per_date[weekday]['revenue'] = round(orders_per_date[weekday]['revenue'], 2)
        return orders_per_date

    @classmethod
    def get_report_per_hours(cls):
        orders = OrderManager.get_all()
        orders_per_hour = {}
        for order in orders:
            if 'date' not in order: continue
            hour = datetime.strptime(
                order['date'],"%Y-%m-%dT%H:%M:%S.%f").hour
            if hour not in orders_per_hour:
                orders_per_hour[hour] = {
                    'revenue': order['total_price'],
                    'orders': 1
                }
            else:
                orders_per_hour[hour] = {
                    'revenue': orders_per_hour[hour]['revenue'] + order['total_price'],
                    'orders': orders_per_hour[hour]['orders'] + 1
                }
        for hour in orders_per_hour:
            orders_per_hour[hour]['revenue'] = round(orders_per_hour[hour]['revenue'], 2)
        return orders_per_hour