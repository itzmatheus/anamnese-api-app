#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument

)


class Torax(EmbeddedDocument):
    '''
    Entidade Torax
    '''
    meta = {
        'ordering': ['traqueia_dor']
    }
    traqueia_dor = StringField(max_length=250)
    traqueia_tosse = StringField(max_length=250)
    traqueia_expectoracao = StringField(max_length=250)
    traqueia_hemoptise = StringField(max_length=250)
    traqueia_vomica = StringField(max_length=250)
    traqueia_chieira = StringField(max_length=250)
    traqueia_estridor = StringField(max_length=250)
    traqueia_triagem = StringField(max_length=250)
    parede_toraxica_dor = StringField(max_length=250)
    parede_toraxica_dispineia = StringField(max_length=250)
    mamas_dor = StringField(max_length=250)
    mamas_nodulo = StringField(max_length=250)
    mamas_secrecao = StringField(max_length=250)
    diafragma_dor = StringField(max_length=250)
    diafragma_soluco = StringField(max_length=250)
    diafragma_sintomas_compressao = StringField(max_length=250)
    coracao_dor = StringField(max_length=250)
    coracao_palpitacoes = StringField(max_length=250)
    coracao_intolerancia_esforcos = StringField(max_length=250)
    coracao_desmaio_esforco = StringField(max_length=250)
    coracao_cianose = StringField(max_length=250)
    coracao_edema = StringField(max_length=250)
    coracao_astenia = StringField(max_length=250)
    coracao_alteracoes_sono = StringField(max_length=250)
    esofago_dor = StringField(max_length=250)
    esofago_disfagia = StringField(max_length=250)
    esofago_odinofagia = StringField(max_length=250)
    esofago_pirose = StringField(max_length=250)
    esofago_regurgitacao = StringField(max_length=250)
    esofago_hematemese = StringField(max_length=250)
