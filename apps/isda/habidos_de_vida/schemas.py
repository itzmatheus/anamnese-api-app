# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str


class HabitosDeVidaSchema(Schema):
    atividades_fisicas = Str()
    contato_triatomineo = Str()
    habitacao = Str()
    contato_animais = Str()
    alimentacao = Str()
    consumo_alcool = Str()
    ajustamento_familiar = Str()
    lazer = Str()
    vida_conjugal = Str()
    condicoes_sociais = Str()
    padraosono_valor = Str()
    padraosono_acorda_antes = Str()
    padraosono_acorda_durante = Str()
    padraosono_demora_iniciar = Str()
    tabagismo_anos_maco = Str()
    tabagismo_valor = Str()
    drogas_valor = Str()
    drogas_outros = Str()
    banho_frequencia = Str()
    banho_valor = Str()
    banho_ultimo_banho = Str()
