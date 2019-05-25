#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class ColunaVertebral(EmbeddedDocument):
    '''
    Entidade Coluna Vertebral
    '''
    meta = {
        'ordering': ['dor']
    }
    dor = StringField(max_length=250)
    rigidez = StringField(max_length=250)
    sinais_inflamatorios = StringField(max_length=250)
    crepitacao_articular = StringField(max_length=250)
    manifestacao_sistemica = StringField(max_length=250)
