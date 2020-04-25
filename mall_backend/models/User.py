from models import db

"""
未使用ORM，
"""

class UserModel(db.Model):
    __tablename__ = 'usermodel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(11))

    userprofile = db.relationship('UserProfile', backref=db.backref('usermodel'))


class UserProfile(db.Model):
    __tablename__ = 'userprofile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    balance = db.Column(db.DECIMAL(2), comment='用户余额')
    integral = db.Column(db.Integer, comment='用户积分')

    user_id = db.Column(db.ForeignKey('usermodel.id'))

    coupon = db.relationship('Coupon', backref='userprofile')
    messages = db.relationship('Message', backref='userprofile')
    shop_cart = db.relationship('ShopCart', backref='userprofile')
    order = db.relationship('Order', backref='userprofile')


class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL)
    category = db.Column(db.String(32))

    user_profile_id = db.Column(db.ForeignKey('userprofile.id'))


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    from_shop_name = db.Column(db.String(64))
    content = db.Column(db.Text)

    user_profile_id = db.Column(db.ForeignKey('userprofile.id'))


class ShopCart(db.Model):
    __tablename__ = 'shopcart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    shop_id = db.Column(db.ForeignKey('shop.id'))

    user_profile_id = db.Column(db.ForeignKey('userprofile.id'))


class Shop(db.Model):
    __tablename__ = 'shop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goods_name = db.Column(db.String(255))
    category = db.Column(db.String(32))
    img_link = db.Column(db.String(255))
    price = db.Column(db.DECIMAL)
    sales_num = db.Column(db.String(16))
    comment_num = db.Column(db.String(16))
    score = db.Column(db.String(16))
    services = db.Column(db.String(255))
    stock = db.Column(db.String(64))
    collections_num = db.Column(db.String(32))

    shop_cart = db.relationship('ShopCart', backref='shop')

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price_sum = db.Column(db.DECIMAL)
    order_num = db.Column(db.Integer)

    user_profile_id = db.Column(db.ForeignKey('userprofile.id'))


class Shop2Order(db.Model):
    __tablename__ = 'shop2order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    shop = db.Column(db.ForeignKey('shop.id'))
    order = db.Column(db.ForeignKey('order.id'))

