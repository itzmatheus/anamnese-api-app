#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class SintomasGerais(EmbeddedDocument):
    '''
    Entidade sintomasgerais
    '''
    meta = {
        'ordering': 'sintomas'
    }
    sintomas = StringField(max_length=250)
    tempo = StringField(max_length=250)
    sudoreses = StringField(max_length=250)
    calafrios = StringField(max_length=250)
    caibras = StringField(max_length=250)
    quantidade = StringField(max_length=250)
    alteracao_peso_presenca = StringField(max_length=250)
    alteracao_peso_valor = StringField(max_length=250)
    alteracao_peso_valor_peso = StringField(max_length=250)
    alteracao_peso_tempo = StringField(max_length=250)
    ouvidos_dor = StringField(max_length=250)
    ouvidos_otorreia = StringField(max_length=250)
    ouvido_otoragia = StringField(max_length=250)
    ouvidos_zumbidos = StringField(max_length=250)
    ouvidos_tontura = StringField(max_length=250)
    olhos_dor_ocular = StringField(max_length=250)
    olhos_prurido = StringField(max_length=250)
    olhos_queimacao = StringField(max_length=250)
    olhos_olho_seco = StringField(max_length=250)
    olhos_perda_visao = StringField(max_length=250)
    olhos_fotofobia = StringField(max_length=250)
    olhos_vermelhidao = StringField(max_length=250)
    faringe_dor_garganta = StringField(max_length=250)
    faringe_disfagia = StringField(max_length=250)
    faringe_tosse = StringField(max_length=250)
    faringe_halitose = StringField(max_length=250)
    faringe_pigarro = StringField(max_length=250)
    faringe_ronco = StringField(max_length=250)
    cavidade_bucal_silose = StringField(max_length=250)
    cavidade_bucal_halitose = StringField(max_length=250)
    cavidade_bucal_dor = StringField(max_length=250)
    cavidade_bucal_ulceracoes = StringField(max_length=250)
    nariz_prurido = StringField(max_length=250)
    nariz_dor = StringField(max_length=250)
    nariz_espirros = StringField(max_length=250)
    nariz_obstrucao_nasal = StringField(max_length=250)
    nariz_corrimento_nasal = StringField(max_length=250)
    nariz_epistaxe = StringField(max_length=250)
    nariz_dispneia = StringField(max_length=250)
    nariz_diminuicao_olfato = StringField(max_length=250)
    febre_presenca = StringField(max_length=250)
    febre_valor = StringField(max_length=250)
    febre_tempo = StringField(max_length=250)