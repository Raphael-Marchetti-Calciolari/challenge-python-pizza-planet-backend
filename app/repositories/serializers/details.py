from ..serializers import ma
from .ingredient import IngredientSerializer
from .beverage import BeverageSerializer
from ..models import IngredientOrderDetail, BeverageOrderDetail

class IngredientOrderDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = IngredientOrderDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )


class BeverageOrderDetailSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = BeverageOrderDetail
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )