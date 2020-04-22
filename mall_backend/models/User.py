from models import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(11))
    userprofile = db.relationship('UserProfile', back_populates='usermodel')


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    balance = db.Column(db.DECIMAL(2), comment='用户余额')
    integral = db.Column(db.Integer, comment='用户积分')


    usermodel = db.relationship('UserModel', back_populates='userprofile')
    coupon = db.relationship('Coupon', back_populates='userprofile')
    message = db.relationship('Message', back_populates='userprofile')

class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL)
    category = db.Column(db.String(32))

    userprofile = db.relationship('UserProfile', back_populates='coupon')


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    from_shop_name = db.Column(db.String(64))
    content = db.Column(db.Text)

    userprofile = db.relationship('UserProfile', back_populates='message')


class ShopCart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    shop = db.relationship('Shop', back_populates='shopcart')
    userprofile = db.relationship('UserProfile', back_populates='shopcart')


class Shop(db.Model):
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


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    price_sum = db.Column(db.DECIMAL)
    order_num = db.Column(db.Integer)

    goods_list = db.relationship('UserProfile', back_populates='order')
    userprofile = db.relationship('UserProfile', back_populates='order')
