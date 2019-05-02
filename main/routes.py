#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Third
# Importamos as classes API e Resource
from flask_restful import Api

# Apps
from apps.aluno.resource import Index
from apps.anamnese.resource import addAnamnese

api = Api()


def addResources(app):

    api.add_resource(Index, '/')
    # Rota para anamnese
    api.add_resource(addAnamnese, '/anamnese')
    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
