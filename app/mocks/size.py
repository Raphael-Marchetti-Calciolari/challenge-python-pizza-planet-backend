from ..common import utils

def size_mock() -> dict:
    return {
        'name': utils.get_random_size_name().capitalize(),
        'price': utils.get_random_price(1.99, 30)
    }