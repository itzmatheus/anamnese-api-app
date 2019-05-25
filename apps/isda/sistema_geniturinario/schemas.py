# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str


class SistemaGeniturinarioSchema(Schema):
    rins_dor = Str()
    rins_alt_miccionais = Str()
    rins_alt_cor_urina = Str()
    rins_alt_cheiro_urina = Str()
    rins_alt_volume_urinario = Str()
    rins_edema = Str()
    rins_febre = Str()
    orgaosgenitais_dor = Str()
    orgaosgenitais_masculino_corrimento = Str()
    orgaosgenitais_masculino_lesoes = Str()
    orgaosgenitais_masculino_nodulos = Str()
    orgaosgenitais_masculino_priapismo = Str()
    orgaosgenitais_masculino_hemospernia = Str()
    orgaosgenitais_masculino_disfuncoes = Str()
    orgaosgenitais_feminino_corrimento = Str()
    orgaosgenitais_feminino_hemorragia = Str()
    orgaosgenitais_feminino_prurido = Str()
