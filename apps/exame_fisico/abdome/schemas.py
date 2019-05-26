# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Email, Str, Int


class AbdomeSchema(Schema):
    abdome_inspecao_tipo_do_abdome = Str()
    abdome_inspecao_cicatriz_cirurgica = Str()
    abdome_inspecao_tipo_cicatriz_umbilical = Str()
    abdome_inspecao_sinal_de_gray_turner = Str()
    abdome_inspecao_sinal_de_culen = Str()
    abdome_inspecao_presenca_de_retratacoes = Str()
    abdome_inspecao_cicatriz_umbilical = Str()
    abdome_inspecao_pulsatilidade_da_aorta = Str()
    abdome_inspecao_presenca_circulacao_colateral = Str()
    abdome_manobrasespeciais_manobra_de_shuster_palpavel = Str()
    abdome_manobrasespeciais_sinal_de_murphy = Str()
    abdome_manobrasespeciais_sinal_de_blemberg = Str()
    abdome_percussao_som = Str()
    abdome_percussao_presenca_de_massas = Str()
    abdome_percussao_hepatomegalia = Str()
    abdome_percussao_esplenomegalia = Str()
    abdome_percussao_macizez_movel_de_decubito = Str()
    abdome_percussao_sinal_de_piparote = Str()
    abdome_palpacao_dor = Str()
    abdome_palpacao_massas_abdominais = Str()
    abdome_palpacao_tensao_abdominal = Str()
    abdome_manobrasespeciais_lemostorres_palpavel = Str()
    abdome_manobrasespeciais_lemostorres_consistencia = Str()
    abdome_manobrasespeciais_lemostorres_borda = Str()
    abdome_manobrasespeciais_lemostorres_dolorosa = Str()
    abdome_manobrasespeciais_lemostorres_superficie = Str()
    abdome_manobrasespeciais_mathieu_palpavel = Str()
    abdome_manobrasespeciais_mathieu_consistencia = Str()
    abdome_manobrasespeciais_mathieu_borda = Str()
    abdome_manobrasespeciais_mathieu_dolorosa = Str()
    abdome_manobrasespeciais_mathieu_superficie = Str()
