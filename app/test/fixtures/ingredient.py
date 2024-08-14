import pytest

from ..utils.functions import (
    get_random_price,
    get_random_ingredient_name
)


def ingredient_mock() -> dict:
    return {
        'name': get_random_ingredient_name().capitalize(),
        'price': get_random_price(0.30, 10)
    }


@pytest.fixture
def ingredient_uri():
    return '/ingredient/'


@pytest.fixture
def ingredient():
    return ingredient_mock()


@pytest.fixture
def ingredients():
    return [ingredient_mock() for _ in range(5)]


@pytest.fixture
def create_ingredient(client, ingredient_uri) -> dict:
    response = client.post(ingredient_uri, json=ingredient_mock())
    return response


@pytest.fixture
def create_ingredients(client, ingredient_uri) -> list:
    ingredients = []
    for _ in range(10):
        new_ingredient = client.post(ingredient_uri, json=ingredient_mock())
        ingredients.append(new_ingredient.json)
    return ingredients
