import pytest

from faker import Faker
from random import randint
from ..utils.functions import (
    get_random_sequence,
    get_random_phone,
    get_random_address,
    get_random_name,
    get_random_faker,
    get_random_choice,
    get_random_choices
)


def client_data_mock(chosen_faker:Faker = None) -> dict:
    faker = chosen_faker if chosen_faker else get_random_faker()
    return {
        'client_address': get_random_address(faker),
        'client_dni': get_random_sequence(),
        'client_name': get_random_name(faker),
        'client_phone': get_random_phone(faker)
    }


def order_mock(clients, ingredients, beverages, sizes) -> dict:
    return {
        **get_random_choice(clients),
        'ingredients': get_random_choices(ingredients),
        'beverages': get_random_choices(beverages),
        'size_id': randint(1, len(sizes))
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def create_order(client, order_uri, create_ingredients, create_beverages, create_sizes) -> dict:
    clients = [client_data_mock() for _ in range(10)]
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    sizes = [size.get('_id') for size in create_sizes]
    response = client.post(order_uri, json=order_mock(
        clients=clients,
        ingredients=ingredients,
        beverages=beverages,
        sizes=sizes
    ))
    return response


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_beverages, create_sizes) -> list:
    orders = []
    clients = [client_data_mock() for _ in range(10)]
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    sizes = [size.get('_id') for size in create_sizes]
    for _ in range(10):
        new_order = client.post(order_uri, json=order_mock(
            clients=clients,
            ingredients=ingredients,
            beverages=beverages,
            sizes=sizes
        ))
        orders.append(new_order.json)
    return orders
