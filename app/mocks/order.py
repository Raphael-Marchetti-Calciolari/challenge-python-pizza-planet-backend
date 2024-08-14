from random import randint
from ..common import utils

def order_mock(clients, ingredients, sizes) -> dict:
    chosen_ingredients = clear_duplicates(
        utils.get_random_choices(ingredients)
    )
    print("\n", chosen_ingredients, "\n")
    chosen_size = utils.get_random_choice(sizes)

    ingredients_ids = [item['_id'] for item in chosen_ingredients]
    size_price = chosen_size['price']

    return {
        **utils.get_random_choice(clients),
        'ingredients': ingredients_ids,
        'size_id': chosen_size['_id'],
        'total_price': calculate_order_price(
            size_price,
            chosen_ingredients
        )
    }


def calculate_order_price(size_price: float, ingredients: list):
    price = size_price + sum(ingredient['price'] for ingredient in ingredients)
    return round(price, 2)


def clear_duplicates(ingredients) -> list:
    unique_ingredients = []
    for ingredient in ingredients:
        if ingredient not in unique_ingredients:
            unique_ingredients.append(ingredient)
    return unique_ingredients