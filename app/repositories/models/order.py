from ..models import db
from datetime import datetime


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))

    size = db.relationship('Size', backref=db.backref('size'))
    ingredient_detail = db.relationship('IngredientOrderDetail', backref=db.backref('ingredient_order_detail'))
    beverage_detail = db.relationship('BeverageOrderDetail', backref=db.backref('beverage_order_detail'))