# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Nested, Str

# Apps
from apps.isda.coluna_vertebral.schemas import ColunaVertebralSchema
from apps.isda.musculos.schemas import MusculosSchema


class IsdaSchema(Schema):
    coluna_vertebral = Nested(ColunaVertebralSchema)
    musculos = Nested(MusculosSchema)
