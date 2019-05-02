#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from main.config import config
from main.routes import addResources
from main.db.db import db


def create_app(config_name):
    app = Flask('api-anamnese')

    app.config.from_object(config[config_name])

    # Inicializando mongodb
    db.init_app(app)

    # Adicionando rotas na aplicacao
    addResources(app)

    return app
