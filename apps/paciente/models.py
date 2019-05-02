#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Third
from mongoengine import (
    DateTimeField,
    StringField,
    IntField,
    EmbeddedDocument
)


class Paciente(EmbeddedDocument):
    '''
    Entidade Paciente
    '''
    meta = {
        'ordering': ['nome']
    }
    nome = StringField(required=True, max_length=150)
    sexo = StringField(default='')
    leito = StringField(default='')
    queixa_principal = StringField(default='')
    profissao = StringField(default='')
    cor = StringField(default='')
    estado_civil = StringField(default='')
    religiao = StringField(default='')
    posicionamento_sexual = StringField(default='')
    nacionalidade = StringField(default='')
    hora_inicio = DateTimeField()
    idade = IntField()
    enfermaria = StringField(default='')

    def __str__(self):
        return self.nome
