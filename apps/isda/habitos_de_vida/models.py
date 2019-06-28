#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class HabitosDeVida(EmbeddedDocument):
    '''
    Entidade Hábitos de vida
    '''
    meta = {
        'ordering': ['atividades_fisicas']
    }
    atividades_fisicas = StringField(max_length=250, default='')
    contato_triatomineo = StringField(max_length=250, default='')
    habitacao = StringField(max_length=250, default='')
    contato_animais = StringField(max_length=250, default='')
    alimentacao = StringField(max_length=250, default='')
    consumo_alcool = StringField(max_length=250, default='')
    ajustamento_familiar = StringField(max_length=250, default='')
    lazer = StringField(max_length=250, default='')
    vida_conjugal = StringField(max_length=250, default='')
    condicoes_sociais = StringField(max_length=250, default='')
    padraosono_valor = StringField(max_length=250, default='')
    padraosono_acorda_antes = StringField(max_length=250, default='')
    padraosono_acorda_durante = StringField(max_length=250, default='')
    padraosono_demora_iniciar = StringField(max_length=250, default='')
    tabagismo_anos_maco = StringField(max_length=250, default='')
    tabagismo_valor = StringField(max_length=250, default='')
    drogas_valor = StringField(max_length=250, default='')
    drogas_outros = StringField(max_length=250, default='')
    banho_frequencia = StringField(max_length=250, default='')
    banho_valor = StringField(max_length=250, default='')
    banho_ultimo_banho = StringField(max_length=250, default='')
