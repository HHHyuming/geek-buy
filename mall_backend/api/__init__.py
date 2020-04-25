from flask_restful import Api
from api.UserResource import *
from api.HomeResource import *
api = Api()


api.add_resource(RotationChart, '/rotation_chart')
api.add_resource(HomeResource, '/home/data')