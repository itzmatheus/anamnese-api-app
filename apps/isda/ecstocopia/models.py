#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    EmailField,
    StringField,
    IntField,
    EmbeddedDocument
)


class Ecstocopia(EmbeddedDocument):
    '''
    Entidade Ecstocopia
    '''
    meta = {
        'ordering': ['postura_atitude']
    }
    postura_atitude = StringField(default='', max_lenght=250)
    atitude_decubito = StringField(default='', max_lenght=250)
    iteracoes_exp_facial = StringField(default='', max_lenght=250)
    acies = StringField(default='', max_lenght=250)
    iteracoes_fala_linguagem = StringField(default='', max_lenght=250)
    biotipo = StringField(default='', max_lenght=250)
    estado_geral = StringField(default='', max_lenght=250)
    mov_involuntarios_descricao = StringField(default='', max_lenght=250)
    mov_involuntarios = StringField(default='', max_lenght=250)
    nivel_consciencia_lucidez = StringField(default='', max_lenght=250)
    nivel_consciencia_orientacao = StringField(default='', max_lenght=250)
    linfonodos_volume = StringField(default='', max_lenght=250)
    linfonodos_alteracoes_pele = StringField(default='', max_lenght=250)
    linfonodos_sensibilidade = StringField(default='', max_lenght=250)
    linfonodos_consistencia = StringField(default='', max_lenght=250)
    linfonodos_mobilidade = StringField(default='', max_lenght=250)
    linfonodos_tamanho = StringField(default='', max_lenght=250)
    linfonodos_localizacao = StringField(default='', max_lenght=250)
    linfonodos_adenomegalia = StringField(default='', max_lenght=250)
    linfonodos_dor = StringField(default='', max_lenght=250)
    linfonodos_descricao_dor = StringField(default='', max_lenght=250)
    linfonodos_quantidade = StringField(default='', max_lenght=250)
    linfonodos_textura = StringField(default='', max_lenght=250)
    tecido_celular_subcutaneo_espessura = StringField(default='', max_lenght=250)
    tecido_celular_subcutaneo_espasticidade = StringField(default='', max_lenght=250)
    tecido_celular_subcutaneo_flacidez = StringField(default='', max_lenght=250)
    mucosas_hidratacao = StringField(default='', max_lenght=250)
    mucosas_coloracao = StringField(default='', max_lenght=250)
    mucosas_lesoes = StringField(default='', max_lenght=250)
    estado_nutricional_estado = StringField(default='', max_lenght=250)
    estado_nutricional_quantidade = StringField(default='', max_lenght=250)
    perfusao_capilar_tipo = StringField(default='', max_lenght=250)
    perfusao_capilar_lentificada_tempo = StringField(default='', max_lenght=250)
    estado_hidratacao_tipo = StringField(default='', max_lenght=250)
    estado_hidratacao_quantificacao = StringField(default='', max_lenght=250)
    edema_detalhes_dor = StringField(default='', max_lenght=250)
    edema_dor = StringField(default='', max_lenght=250)
    edema_descricao_edema = StringField(default='', max_lenght=250)
    edema_detalhes_consistencia = StringField(default='', max_lenght=250)
    edema_intensidade = StringField(default='', max_lenght=250)
    edema_detalhes_intensidade = StringField(default='', max_lenght=250)
    edema_localizacao = StringField(default='', max_lenght=250)
    edema_detalhes_localizacao = StringField(default='', max_lenght=250)
    pele_coloracao = StringField(default='', max_lenght=250)
    pele_continuidade = StringField(default='', max_lenght=250)
    pele_umidade = StringField(default='', max_lenght=250)
    pele_textura = StringField(default='', max_lenght=250)
    pele_espessura = StringField(default='', max_lenght=250)
    pele_temperatura = StringField(default='', max_lenght=250)
    pele_elasticidade = StringField(default='', max_lenght=250)
    pele_mobilidade = StringField(default='', max_lenght=250)
    pele_turgor = StringField(default='', max_lenght=250)
    pele_sensibilidade = StringField(default='', max_lenght=250)
    pele_lesoes_elementares = StringField(default='', max_lenght=250)
    faneros_cabelos_tipos_implatacao = StringField(default='', max_lenght=250)
    faneros_cabelos_distribuicao = StringField(default='', max_lenght=250)
    faneros_cabelos_quantidade = StringField(default='', max_lenght=250)
    faneros_cabelos_coloracao = StringField(default='', max_lenght=250)
    faneros_cabelos_brilho = StringField(default='', max_lenght=250)
    faneros_unhas_formato = StringField(default='', max_lenght=250)
    faneros_unhas_cor = StringField(default='', max_lenght=250)
    faneros_unhas_resistencia = StringField(default='', max_lenght=250)
