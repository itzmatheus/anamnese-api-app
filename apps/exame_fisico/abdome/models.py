
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)

class Abdome(EmbeddedDocument):
    '''
    Entidade Abdome
    '''
    abdome_inspecao_tipo_do_abdome = StringField(max_lenght=250, default='')
    abdome_inspecao_cicatriz_cirurgica = StringField(max_lenght=250, default='')
    abdome_inspecao_tipo_cicatriz_umbilical = StringField(max_lenght=250, default='')
    abdome_inspecao_sinal_de_gray_turner = StringField(max_lenght=250, default='')
    abdome_inspecao_sinal_de_culen = StringField(max_lenght=250, default='')
    abdome_inspecao_presenca_de_retratacoes = StringField(max_lenght=250, default='')
    abdome_inspecao_cicatriz_umbilical = StringField(max_lenght=250, default='')
    abdome_inspecao_pulsatilidade_da_aorta = StringField(max_lenght=250, default='')
    abdome_inspecao_presenca_circulacao_colateral = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_manobra_de_shuster_palpavel = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_sinal_de_murphy = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_sinal_de_blemberg = StringField(max_lenght=250, default='')
    abdome_percussao_som = StringField(max_lenght=250, default='')
    abdome_percussao_presenca_de_massas = StringField(max_lenght=250, default='')
    abdome_percussao_hepatomegalia = StringField(max_lenght=250, default='')
    abdome_percussao_esplenomegalia = StringField(max_lenght=250, default='')
    abdome_percussao_macizez_movel_de_decubito = StringField(max_lenght=250, default='')
    abdome_percussao_sinal_de_piparote = StringField(max_lenght=250, default='')
    abdome_palpacao_dor = StringField(max_lenght=250, default='')
    abdome_palpacao_massas_abdominais = StringField(max_lenght=250, default='')
    abdome_palpacao_tensao_abdominal = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_lemostorres_palpavel = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_lemostorres_consistencia = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_lemostorres_borda = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_lemostorres_dolorosa = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_lemostorres_superficie = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_mathieu_palpavel = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_mathieu_consistencia = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_mathieu_borda = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_mathieu_dolorosa = StringField(max_lenght=250, default='')
    abdome_manobrasespeciais_mathieu_superficie = StringField(max_lenght=250, default='')
    abdome_inspecao_cicatriz_cirurgica_descricao = StringField(max_lenght=250, default='')
    abdome_inspecao_presenca_de_retratacoes_descricao = StringField(max_lenght=250, default='')
    abdome_inspecao_presenca_circulacao_colateral_descricao = StringField(max_lenght=250, default='')
    abdome_percussao_presenca_de_massas_descricao = StringField(max_lenght=250, default='')
    abdome_percussao_hepatomegalia_descricao = StringField(max_lenght=250, default='')
    abdome_percussao_esplenomegalia_descricao = StringField(max_lenght=250, default='')
    abdome_palpacao_dor_descricao = StringField(max_lenght=250, default='')
    abdome_palpacao_massas_abdominais_descricao = StringField(max_lenght=250, default='')