#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class SistemaGeniturinario(EmbeddedDocument):
    '''
    Entidade Sistema Geniturinario
    '''
    meta = {
        'ordering': ['rins_dor']
    }
    rins_dor = StringField(max_length=250, default='')
    rins_alt_miccionais = StringField(max_length=250, default='')
    rins_alt_cor_urina = StringField(max_length=250, default='')
    rins_alt_cheiro_urina = StringField(max_length=250, default='')
    rins_alt_volume_urinario = StringField(max_length=250, default='')
    rins_edema = StringField(max_length=250, default='')
    rins_febre = StringField(max_length=250, default='')
    orgaosgenitais_dor = StringField(max_length=250, default='')
    orgaosgenitais_masculino_corrimento = StringField(max_length=250, default='')
    orgaosgenitais_masculino_lesoes = StringField(max_length=250, default='')
    orgaosgenitais_masculino_nodulos = StringField(max_length=250, default='')
    orgaosgenitais_masculino_priapismo = StringField(max_length=250, default='')
    orgaosgenitais_masculino_hemospernia = StringField(max_length=250, default='')
    orgaosgenitais_masculino_disfuncoes = StringField(max_length=250, default='')
    orgaosgenitais_feminino_corrimento = StringField(max_length=250, default='')
    orgaosgenitais_feminino_hemorragia = StringField(max_length=250, default='')
    orgaosgenitais_feminino_prurido = StringField(max_length=250, default='')
