# -*- coding:utf-8 -*-

# Third
from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {'status': 'OK'}
