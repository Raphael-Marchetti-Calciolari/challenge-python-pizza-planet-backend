from ..common import utils

def ingredient_mock() -> dict:
    return {
        'name': utils.get_random_ingredient_name().capitalize(),
        'price': utils.get_random_price(0.30, 10)
    }