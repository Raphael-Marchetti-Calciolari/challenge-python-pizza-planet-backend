from ..serializers import ma
from .details import IngredientOrderDetailSerializer, BeverageOrderDetailSerializer
from .size import SizeSerializer
from ..models import Order

class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    ingredient_detail = ma.Nested(IngredientOrderDetailSerializer, many=True)
    beverage_detail = ma.Nested(BeverageOrderDetailSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'ingredient_detail',
            'beverage_detail'
        )