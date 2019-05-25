# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Nested, Str

# Apps
from apps.isda.coluna_vertebral.schemas import ColunaVertebralSchema


class IsdaSchema(Schema):
    coluna_vertebral = Nested(ColunaVertebralSchema)
