# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str, Int

class CardiovascularSchema(Schema):
    cardiovascular_inspecaoepalpacao_tipo_polpa_digital = Str()
    cardiovascular_inspecaoepalpacao_presenca_de_abaulamento = Str()
    cardiovascular_inspecaoepalpacao_turgencia_jugular = Str()
    cardiovascular_inspecaoepalpacao_lesoes_elementares = Str()
    cardiovascular_inspecaoepalpacao_situacao_do_ciclo = Str()
    cardiovascular_inspecaoepalpacao_intensidade = Str()
    cardiovascular_inspecaoepalpacao_localizacao_fremito = Str()
    cardiovascular_inspecaoepalpacao_polpas_digitais = Str()
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_valor = Str()
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_localizacao = Str()
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_situacao_ciclo_cardiaco = Str()
    cardiovascular_inspecaoepalpacao_fremitocardiovascular_intensidade = Int()
    cardiovascular_auscultacardiaca_ritmo_cardiaco = Str()
    cardiovascular_auscultacardiaca_intensidade_do_som = Str()
    cardiovascular_auscultacardiaca_frequencia_cardiaca = Str()
    cardiovascular_soprocardiaco_foco = Str()
    cardiovascular_soprocardiaco_intensidade = Str()
    cardiovascular_soprocardiaco_relacao_ciclo_cardiaco = Str()
    cardiovascular_auscultacarotidea_presenca_de_sopro = Str()
