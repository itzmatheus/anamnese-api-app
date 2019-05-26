#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class Respiratorio(EmbeddedDocument):
    '''
    Entidade Respiratorio
    '''
    meta = {
        'ordering': ['respiratorio_presencacicatriz_valor']
    }
    respiratorio_presencacicatriz_valor = StringField(max_length=250)
    respiratorio_presencacicatriz_motivo = StringField(max_length=250)
    respiratorio_palpacao_ftv_valor = StringField(max_length=250)
    respiratorio_palpacao_ftv_localizacao = StringField(max_length=250)
    respiratorio_palpacao_submacico_localizacao = StringField(max_length=250)
    respiratorio_palpacao_submacico_valor =StringField(max_length=250)
    respiratorio_palpacao_manobra_de_lasengue = StringField(max_length=250)
    respiratorio_palpacao_manobra_de_ruault = StringField(max_length=250)
    respiratorio_palpacao_percussao = StringField(max_length=250)
    respiratorio_palpacao_localizacao_percussao = StringField(max_length=250)
    respiratorio_papacao_som_pulmonar = StringField(max_length=250)
    respiratorio_palpacao_timpanico = StringField(max_length=250)
    respiratorio_palpacao_macico = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_localizacao = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_tipo_da_dor = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_frenquencia_da_dor = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_intensidade_da_dor = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_fatores_que_pioram_a_dor = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_dorirradia_valor = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_dorirradia_frequencia = StringField(max_length=250)
    respiratorio_palpacao_presencadedor_intensidade = StringField(max_length=250)
    respiratorio_auscultapulmonar_murmurio_vesicular_presente = StringField(max_length=250)
    respiratorio_auscultapulmonar_murmurio_vesicular_sonoridade = StringField(max_length=250)
    respiratorio_auscultapulmonar_auscultavoz_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_auscultavoz_ressonancia_aumentada = StringField(max_length=250)
    respiratorio_auscultapulmonar_murmuriovesicular_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_murmuriovesicular_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_roncos_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_roncos_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_atritopleural_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_atritopleural_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_sopro_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_sopro_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_estritorgrosso_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_estritorgrosso_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_estritorfino_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_estritorfino_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_estritor_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_estritor_localizacao = StringField(max_length=250)
    respiratorio_auscultapulmonar_sibilos_valor = StringField(max_length=250)
    respiratorio_auscultapulmonar_sibilos_localizacao = StringField(max_length=250)
