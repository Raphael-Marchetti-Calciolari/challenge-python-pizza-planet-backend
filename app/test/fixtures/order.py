import pytest

from faker import Faker
from random import randint
from ..utils.functions import (
    get_random_sequence,
    shuffle_list,
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


def order_mock(clients, ingredients, sizes) -> dict:
    return {
        **get_random_choice(clients),
        'ingredients': get_random_choices(ingredients),
        'size_id': randint(1, len(sizes))
    }


@pytest.fixture
def order_uri():
    return '/order'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(create_ingredients, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    size_id = create_size.get('_id')
    return {
        **client_data_mock(),
        'ingredients': ingredients,
        'size_id': size_id
    }


@pytest.fixture
def create_orders(client, order_uri, create_ingredients, create_sizes) -> list:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    sizes = [size.get('_id') for size in create_sizes]
    orders = []
    for _ in range(10):
        new_order = client.post(order_uri, json={
            **client_data_mock(),
            'ingredients': shuffle_list(ingredients)[:5],
            'size_id': shuffle_list(sizes)[0]
        })
        orders.append(new_order)
    return orders
