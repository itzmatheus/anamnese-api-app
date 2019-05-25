#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class SistemaHemolinfopetico(EmbeddedDocument):
    '''
    Entidade Sistema Hemolinfopetico
    '''
    meta = {
        'ordering': ['astenia']
    }
    astenia = StringField(max_length=250, default='')
    adenomegalia = StringField(max_length=250, default='')
    hepatomegalia = StringField(max_length=250, default='')
    esplenomegalia = StringField(max_length=250, default='')
    hemorragia = StringField(max_length=250, default='')
