#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    EmailField,
    StringField,
    IntField,
    EmbeddedDocument
)


class Aluno(EmbeddedDocument):
    '''
    Entidade Aluno
    '''
    meta = {
        'ordering': ['matricula']
    }
    nome = StringField(required=True)
    email = EmailField(max_length=50, default='')
    matricula = IntField(required=True)
    grupo = StringField(default='')
