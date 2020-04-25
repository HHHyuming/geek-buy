from flask_restful import Resource, marshal_with
from flask_restful.reqparse import RequestParser

from models.User import *
from api.fields_map import *
from script.db import MysqlPool


class UserResource(Resource):
    def __init__(self):
        user_parse = RequestParser()
        user_parse.add_argument('username')
        user_parse.add_argument('password')

    def post(self):
        pass


class RotationChart(Resource):
    @marshal_with(shop)
    def get(self):

        with MysqlPool() as db:
            sql = 'select * from shop where category="{0}" limit 4'.format('上衣')
            db.cursor.execute(sql)
            result = db.cursor.fetchall()
        print(result)
        return result
