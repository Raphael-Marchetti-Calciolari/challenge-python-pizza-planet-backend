from random import randint
from ..common import utils

def order_mock(clients, ingredients, sizes) -> dict:
    return {
        **utils.get_random_choice(clients),
        'ingredients': utils.get_random_choices(ingredients),
        'size_id': randint(1, len(sizes))
    }