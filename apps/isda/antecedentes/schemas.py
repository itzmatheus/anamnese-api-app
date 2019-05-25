# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str

class AntecedentesSchema(Schema):
    familia_enxaqueca = Str()
    familia_diabetes = Str()
    familia_has = Str()
    familia_alzheimer = Str()
    familia_outros = Str()
    familia_cancer_valor = Str()
    familia_cancer_especifique = Str()
    familia_cancer_outros = Str()
    pessoais_patologico_doencas_atuais = Str()
    pessoais_patologico_alergias = Str()
    pessoais_patologico_cirurgias = Str()
    pessoais_patologico_transfusoes = Str()
    pessoais_patologico_doencas_sofridas = Str()
    pessoais_patologico_historia = Str()
    pessoais_patologico_medicamentos_em_uso = Str()
    pessoais_fisiologicos_gestacao_nascimento = Str()
    pessoais_fisiologicos_desenvolvimento_psicomotor = Str()
    pessoais_fisiologicos_desenvolvimento_sexual = Str()
