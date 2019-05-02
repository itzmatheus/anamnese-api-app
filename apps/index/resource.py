# -*- coding:utf-8 -*-

# Third
from flask_restful import Resource
from datetime import datetime


class Index(Resource):
    def get(self):
        return {
            'status': 'OK',
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            "mensagem": "API Anamnese",
            "versão": '0.0.1'
        }
