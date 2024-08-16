from ..common import utils

def order_mock(clients, ingredients, beverages, sizes) -> dict:
    chosen_ingredients = clear_duplicates(
        utils.get_random_choices(ingredients)
    )
    chosen_beverages = clear_duplicates(
        utils.get_random_choices(beverages)
    )
    chosen_size = utils.get_random_choice(sizes)

    ingredients_ids = extract_ids(chosen_ingredients)
    beverages_ids = extract_ids(chosen_beverages)
    size_price = chosen_size['price']

    return {
        **utils.get_random_choice(clients),
        'ingredients': ingredients_ids,
        'beverages': beverages_ids,
        'size_id': chosen_size['_id'],
        'total_price': calculate_order_price(
            size_price,
            chosen_ingredients,
            chosen_beverages
        )
    }


def extract_ids(items: list):
    return [item['_id'] for item in items]


def calculate_order_price(size_price: float, ingredients: list, beverages: list):
    ingredients_sum = sum(ingredient['price'] for ingredient in ingredients)
    beverages_sum = sum(beverage['price'] for beverage in beverages)
    price = size_price + ingredients_sum + beverages_sum
    return round(price, 2)


def clear_duplicates(items) -> list:
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items