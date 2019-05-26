#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    IntField,
    EmbeddedDocument
)


class Cardiovascular(EmbeddedDocument):
    '''
    Entidade Cardiovascular
    '''
    meta = {
        'ordering': ['cardiovascular_inspecaoepalpacao_tipo_polpa_digital']
    }
    cardiovascular_inspecaoepalpacao_tipo_polpa_digital = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_presenca_de_abaulamento = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_turgencia_jugular = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_lesoes_elementares = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_situacao_do_ciclo = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_intensidade = IntField()
    cardiovascular_inspecaoepalpacao_localizacao_fremito = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_polpas_digitais = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_valor = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_localizacao = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_situacao_ciclo_cardiaco = StringField(max_length=250)
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_intensidade = IntField()
    cardiovascular_auscultacardiaca_ritmo_cardiaco = StringField(max_length=250)
    cardiovascular_auscultacardiaca_intensidade_do_som = IntField()
    cardiovascular_auscultacardiaca_frequencia_cardiaca = IntField()
    cardiovascular_soprocardiaco_foco = StringField(max_length=250)
    cardiovascular_soprocardiaco_intensidade = IntField()
    cardiovascular_soprocardiaco_relacao_ciclo_cardiaco = StringField(max_length=250)
    cardiovascular_auscultacarotidea_presenca_de_sopro = StringField(max_length=250)
