# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Nested, Str

# Apps
from apps.isda.coluna_vertebral.schemas import ColunaVertebralSchema
from apps.isda.musculos.schemas import MusculosSchema
from apps.isda.nervoso.schemas import NervosoSchema
from apps.isda.habidos_de_vida.schemas import HabitosDeVidaSchema


class IsdaSchema(Schema):
    coluna_vertebral = Nested(ColunaVertebralSchema)
    musculos = Nested(MusculosSchema)
    nervoso = Nested(NervosoSchema)
    habidos_de_vida = Nested(HabitosDeVidaSchema)
