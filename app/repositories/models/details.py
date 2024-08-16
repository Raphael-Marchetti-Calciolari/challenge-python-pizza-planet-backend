from ..models import db


class IngredientOrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    ingredient_price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'))
    ingredient = db.relationship('Ingredient', backref=db.backref('ingredient'))


class BeverageOrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    beverage_price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage._id'))
    beverage = db.relationship('Beverage', backref=db.backref('beverage'))