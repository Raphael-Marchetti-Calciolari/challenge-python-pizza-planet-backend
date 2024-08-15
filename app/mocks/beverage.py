from ..common import utils

def beverage_mock() -> dict:
    return {
        'name': utils.get_random_beverage_name().capitalize(),
        'price': utils.get_random_price(0.30, 10)
    }