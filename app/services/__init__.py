from .order import order
from .ingredient import ingredient
from .size import size
from .index import index

from ..test.fixtures import ingredient
from ..test.fixtures import size
from ..test.fixtures import order

from ..test.utils import functions

mock_ingredients = []
mock_sizes = []
mock_costumers = []
mock_orders = []

print('\n### Generating Ingredients ###')
for i in range(10):
    new_ingredient = ingredient.ingredient_mock()
    mock_ingredients.append(new_ingredient)
    print(new_ingredient)

print('\n### Generating Pizza Sizes ###')
for i in range(5):
    new_size = size.size_mock()
    mock_sizes.append(new_size)
    print(new_size)

print('\n### Generating Customers ###')
for i in range(20):
    new_costumer = order.client_data_mock()
    mock_costumers.append(new_costumer)
    print(new_costumer)

print('\n### Generating Orders ###')
for i in range(100):
    new_order = order.order_mock(
        mock_costumers,
        mock_ingredients,
        mock_sizes
    )
    mock_orders.append(new_order)
    print(new_order)
