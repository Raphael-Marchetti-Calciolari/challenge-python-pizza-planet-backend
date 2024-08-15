from .ingredient import ingredient_mock
from .size import size_mock
from .client import client_data_mock
from .order import order_mock

class DataIngestor:
    ingredients = []
    sizes = []
    costumers = []

    def __init__(self, ingredients, sizes, costumers):
        self.ingredients = ingredients
        self.sizes = sizes
        self.costumers = costumers

    def __str__(self) -> str:
        return f'Ingredients: {self.ingredients}\nSizes: {self.sizes}\nCostumers: {self.costumers}'

def load_data():
    mock_ingredients = []
    mock_sizes = []
    mock_costumers = []

    for i in range(10):
        mock_ingredients.append(ingredient_mock())

    for i in range(5):
        mock_sizes.append(size_mock())

    for i in range(20):
        mock_costumers.append(client_data_mock())

    return DataIngestor(
        mock_ingredients,
        mock_sizes,
        mock_costumers
    )