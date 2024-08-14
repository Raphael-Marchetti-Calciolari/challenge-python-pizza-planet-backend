from .ingredient import ingredient_mock
from .size import size_mock
from .client import client_data_mock
from .order import order_mock

class DataIngestor:
    ingredients = []
    sizes = []
    orders = []

    def __init__(self, ingredients, sizes, orders):
        self.ingredients = ingredients
        self.sizes = sizes
        self.orders = orders

def load_data():
    mock_ingredients = []
    mock_sizes = []
    mock_costumers = []
    mock_orders = []

    print('\n### Generating Ingredients ###')
    for i in range(10):
        new_ingredient = ingredient_mock()
        mock_ingredients.append(new_ingredient)
        print(new_ingredient)

    print('\n### Generating Pizza Sizes ###')
    for i in range(5):
        new_size = size_mock()
        mock_sizes.append(new_size)
        print(new_size)

    print('\n### Generating Customers ###')
    for i in range(20):
        new_costumer = client_data_mock()
        mock_costumers.append(new_costumer)
        print(new_costumer)

    print('\n### Generating Orders ###')
    for i in range(100):
        new_order = order_mock(
            mock_costumers,
            mock_ingredients,
            mock_sizes
        )
        mock_orders.append(new_order)
        print(new_order)

    return DataIngestor(
        mock_ingredients,
        mock_sizes,
        mock_orders
    )