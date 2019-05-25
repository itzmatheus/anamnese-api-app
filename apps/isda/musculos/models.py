#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class Musculos(EmbeddedDocument):
    '''
    Entidade Musculos
    '''
    meta = {
        'ordering': ['dor']
    }
    atrofia_muscular = StringField(max_length=250)
    dificuldade_andar = StringField(max_length=250)
    fraqueza_muscular = StringField(max_length=250)
    dor = StringField(max_length=250)
    caibras = StringField(max_length=250)
    espasmos_musculares = StringField(max_length=250)
