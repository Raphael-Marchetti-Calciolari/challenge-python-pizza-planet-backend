from typing import List
from .base import BaseManager
from .ingredient import IngredientManager
from .beverage import BeverageManager
from .size import SizeManager
from .order import OrderManager
from ..models import Order
from ...common import utils
from ...mocks import DataIngestor, gen_mock_data, order_mock
from datetime import datetime, timedelta, UTC
import random

class MockManager(BaseManager):
    mock_data:DataIngestor = None
    orders: List[Order] = []

    def get_random_date() -> datetime:
        start_date = datetime.now(UTC) - timedelta(days=365)
        end_date = datetime.now(UTC)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date

    @classmethod
    def fill_mock_data(cls):
        if cls.mock_data is None: 
            cls.mock_data = gen_mock_data()
            new_ingredients = []
            for ingredient in cls.mock_data.ingredients:
                new_ingredients.append(
                    IngredientManager.create(ingredient)
                )
            cls.mock_data.ingredients = new_ingredients
            new_beverages = []
            for beverage in cls.mock_data.beverages:
                new_beverages.append(
                    BeverageManager.create(beverage)
                )
            cls.mock_data.beverages = new_beverages
            new_sizes = []
            for size in cls.mock_data.sizes:
                new_sizes.append(
                    SizeManager.create(size)   
                )
            cls.mock_data.sizes = new_sizes

        new_orders = []
        for i in range(100):
            order = order_mock(
                cls.mock_data.costumers,
                cls.mock_data.ingredients,
                cls.mock_data.beverages,
                cls.mock_data.sizes
            )
            order['date'] = cls.get_random_date()
            order_ingredients = order.pop('ingredients')
            order_beverages = order.pop('beverages')
            new_orders.append(
                OrderManager.create(
                    order,
                    IngredientManager.get_by_id_list(order_ingredients),
                    BeverageManager.get_by_id_list(order_beverages)
                )
            )
        if cls.orders: cls.orders.extend(new_orders)
        else: cls.orders = new_orders

        return 'Filled mock data'
    
    @classmethod
    def clear_mock_data(cls):
        if cls.mock_data is None:
            raise RuntimeError('No mock data to clear')
        for ingredient in cls.mock_data.ingredients:
            utils.ingredients.append(ingredient['name'])
            IngredientManager.delete(ingredient['_id'])
        for beverage in cls.mock_data.beverages:
            utils.beverages.append(beverage['name'])
            BeverageManager.delete(beverage['_id'])
        for size in cls.mock_data.sizes:
            utils.sizes.append(size['name'])
            SizeManager.delete(size['_id'])
        for order in cls.orders:
            OrderManager.delete(order['_id'])
        cls.mock_data = None
        return 'Mock data cleared'
