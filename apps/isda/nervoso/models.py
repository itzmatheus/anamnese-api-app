#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class Nervoso(EmbeddedDocument):
    '''
    Entidade Nervoso
    '''
    meta = {
        'ordering': ['disturbios_consciencia']
    }
    disturbios_consciencia = StringField(max_length=250)
    cefaleia = StringField(max_length=250)
    tontura_vertigem = StringField(max_length=250)
    ausencias = StringField(max_length=250)
    convusoes = StringField(max_length=250)
    automatismos = StringField(max_length=250)
    amnesia = StringField(max_length=250)
    disturbios_visuais = StringField(max_length=250)
    disturbios_auditivos = StringField(max_length=250)
    disturbios_mancha = StringField(max_length=250)
    disturbios_motricidade = StringField(max_length=250)
    disturbios_esfincterianos = StringField(max_length=250)
    disturbios_sono = StringField(max_length=250)
    disturbios_funcoes = StringField(max_length=250)
    outros = StringField(max_length=250)
