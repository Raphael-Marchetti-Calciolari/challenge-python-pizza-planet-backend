from app.controllers import (IngredientController, BeverageController, OrderController,
                             SizeController)
from app.controllers.base import BaseController
from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list, beverages: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for ingredient in items:
        created_item, _ = controller.create(ingredient)
        created_items.append(created_item)
    return created_items


def __create_models(ingredients: list, beverages: list, sizes: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_beverages = __create_items(beverages, BeverageController)
    created_sizes = __create_items(sizes, SizeController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients, created_beverages


def test_create(app, ingredients, beverages, size, client_data):
    created_size, created_ingredients, created_beverages = __create_models(ingredients, beverages, [size])
    order = __order(created_ingredients, created_beverages, created_size, client_data)
    created_order, error = OrderController.create(order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverages_ids = order.pop('beverages', [])
    assert(error is None)
    for param, value in order.items():
        assert(param in created_order)
        assert(value == created_order[param])
        assert(created_order['_id'])
        assert(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['ingredient_detail'])
        beverages_in_detail = set(item['beverage']['_id'] for item in created_order['beverage_detail'])
        assert(not ingredients_in_detail.difference(ingredient_ids))
        assert(not beverages_in_detail.difference(beverages_ids))


def test_calculate_order_price(app, ingredients, beverages, size, client_data):
    created_size, created_ingredients, created_beverages = __create_models(ingredients, beverages, [size])
    order = __order(created_ingredients, created_beverages, created_size, client_data)
    created_order, _ = OrderController.create(order)
    ingredients_sum = sum(ingredient['price'] for ingredient in created_ingredients)
    beverages_sum = sum(beverage['price'] for beverage in created_beverages)
    assert(created_order['total_price'] == round(created_size['price'] + ingredients_sum + beverages_sum, 2))


def test_get_by_id(app, ingredients, beverages, size, client_data):
    created_size, created_ingredients, created_beverages = __create_models(ingredients, beverages, [size])
    order = __order(created_ingredients, created_beverages, created_size, client_data)
    created_order, _ = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverage_ids = order.pop('beverages', [])
    assert(error is None)
    for param, value in created_order.items():
        assert(order_from_db[param] == value)
        assert(size_id == created_order['size']['_id'])

        ingredients_in_detail = set(item['ingredient']['_id'] for item in created_order['ingredient_detail'])
        beverages_in_detail = set(item['beverage']['_id'] for item in created_order['beverage_detail'])
        assert(not ingredients_in_detail.difference(ingredient_ids))
        assert(not beverages_in_detail.difference(beverage_ids))


def test_get_all(app, ingredients, beverages, sizes, client_data):
    created_sizes, created_ingredients, created_beverages = __create_models(ingredients, beverages, sizes)
    created_orders = []
    for _ in range(5):
        order = __order(
            shuffle_list(created_ingredients)[:3],
            shuffle_list(created_beverages)[:3],
            get_random_choice(created_sizes), client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)

    orders_from_db, error = OrderController.get_all()
    searchable_orders = {db_order['_id']: db_order for db_order in orders_from_db}
    assert(error is None)
    for created_order in created_orders:
        current_id = created_order['_id']
        assert current_id in searchable_orders
        for param, value in created_order.items():
            assert(searchable_orders[current_id][param] == value)
