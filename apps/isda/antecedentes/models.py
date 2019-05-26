#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class Antecedentes(EmbeddedDocument):
    '''
    Entidade Antecedentes
    '''
    meta = {
        'ordering': ['familia_enxaqueca']
    }
    familia_enxaqueca = StringField(max_length=250)
    familia_diabetes = StringField(max_length=250)
    familia_has = StringField(max_length=250)
    familia_alzheimer = StringField(max_length=250)
    familia_outros = StringField(max_length=250)
    familia_cancer_valor = StringField(max_length=250)
    familia_cancer_especifique = StringField(max_length=250)
    familia_cancer_outros = StringField(max_length=250)
    pessoais_patologico_doencas_atuais = StringField(max_length=250)
    pessoais_patologico_alergias = StringField(max_length=250)
    pessoais_patologico_cirurgias = StringField(max_length=250)
    pessoais_patologico_transfusoes = StringField(max_length=250)
    pessoais_patologico_doencas_sofridas = StringField(max_length=250)
    pessoais_patologico_historia = StringField(max_length=250)
    pessoais_patologico_medicamentos_em_uso = StringField(max_length=250)
    pessoais_fisiologicos_gestacao_nascimento = StringField(max_length=250)
    pessoais_fisiologicos_desenvolvimento_psicomotor = StringField(max_length=250)
    pessoais_fisiologicos_desenvolvimento_sexual = StringField(max_length=250)
