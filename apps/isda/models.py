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
from apps.isda.habidos_de_vida.models import HabitosDeVida
from apps.isda.abdome.models import Abdome
from apps.isda.ecstocopia.models import Ecstocopia


class Isda(EmbeddedDocument):
    '''
    Entidade Isda
    '''
    meta = {'collection': 'Isda'}

    coluna_vertebral = EmbeddedDocumentField(ColunaVertebral,
        default=ColunaVertebral)
    musculos = EmbeddedDocumentField(Musculos, default=Musculos)
    nervoso = EmbeddedDocumentField(Nervoso, default=Nervoso)
    habidos_de_vida = EmbeddedDocumentField(HabitosDeVida, default=HabitosDeVida)
    abdome = EmbeddedDocumentField(Abdome, default=Abdome)
    ecstocopia = EmbeddedDocumentField(Ecstocopia, default=Ecstocopia)
