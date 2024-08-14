from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column

from .models import Ingredient, Order, OrderDetail, Size, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, ma)

from ..mocks import DataIngestor, load_data, order_mock

from datetime import datetime, timedelta, UTC
import random

class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)
    
    @classmethod
    def delete(cls, _id: Any):
        res = cls.session.query(cls.model).filter_by(_id=_id).delete()
        if res == 0:
            return None
        cls.session.commit()
        return "Deleted successfully"

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


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
        if cls.mock_data is not None:
            raise RuntimeError('Mock data already filled')
        cls.mock_data = load_data()
        new_ingredients = []
        for ingredient in cls.mock_data.ingredients:
            new_ingredients.append(
                IngredientManager.create(ingredient)
            )
        cls.mock_data.ingredients = new_ingredients
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
                cls.mock_data.sizes
            )
            order['date'] = cls.get_random_date()
            order_ingredients = order.pop('ingredients')
            new_orders.append(
                OrderManager.create(
                    order,
                    IngredientManager.get_by_id_list(order_ingredients)   
                )
            )
        cls.orders = new_orders

        return 'Filled mock data'
    
    @classmethod
    def clear_mock_data(cls):
        if cls.mock_data is None:
            raise RuntimeError('No mock data to clear')
        for ingredient in cls.mock_data.ingredients:
            IngredientManager.delete(ingredient['_id'])
        for size in cls.mock_data.sizes:
            SizeManager.delete(size['_id'])
        for order in cls.orders:
            OrderManager.delete(order['_id'])
        cls.mock_data = None
        return 'Mock data cleared'


class ReportManager(BaseManager):
    mock_data:DataIngestor = None
    orders: List[Order] = []

    @classmethod
    def get_report(cls):
        return "Called report"
