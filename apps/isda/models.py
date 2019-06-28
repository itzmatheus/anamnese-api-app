#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python
from datetime import datetime


# Third
from mongoengine import (
    DateTimeField,
    EmbeddedDocumentField,
    EmbeddedDocument
)


# Apps
from main.db.db import db
from apps.isda.coluna_vertebral.models import ColunaVertebral
from apps.isda.musculos.models import Musculos
from apps.isda.nervoso.models import Nervoso
from apps.isda.habitos_de_vida.models import HabitosDeVida
from apps.isda.abdome.models import Abdome
from apps.isda.ectoscopia.models import Ectoscopia
from apps.isda.sintomas_gerais.models import SintomasGerais
from apps.isda.antecedentes.models import Antecedentes
from apps.isda.sistema_geniturinario.models import SistemaGeniturinario
from apps.isda.sistema_hemolinfopetico.models import SistemaHemolinfopetico
from apps.isda.torax.models import Torax


class Isda(EmbeddedDocument):
    '''
    Entidade Isda
    '''
    meta = {'collection': 'Isda'}

    coluna_vertebral = EmbeddedDocumentField(ColunaVertebral,
        default=ColunaVertebral)
    musculos = EmbeddedDocumentField(Musculos, default=Musculos)
    nervoso = EmbeddedDocumentField(Nervoso, default=Nervoso)
    habitos_de_vida = EmbeddedDocumentField(HabitosDeVida, default=HabitosDeVida)
    abdome = EmbeddedDocumentField(Abdome, default=Abdome)
    ectoscopia = EmbeddedDocumentField(Ectoscopia, default=Ectoscopia)
    sintomas_gerais = EmbeddedDocumentField(SintomasGerais, default=SintomasGerais)
    antecedentes = EmbeddedDocumentField(Antecedentes, default=Antecedentes)
    sistema_geniturinario = EmbeddedDocumentField(SistemaGeniturinario, default=SistemaGeniturinario)
    sistema_hemolinfopetico = EmbeddedDocumentField(SistemaHemolinfopetico, default=SistemaHemolinfopetico)
    torax = EmbeddedDocumentField(Torax, default=Torax)
