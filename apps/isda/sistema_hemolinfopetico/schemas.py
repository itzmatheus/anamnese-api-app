# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str


class SistemaHemolinfopeticoSchema(Schema):
    astenia = Str()
    adenomegalia = Str()
    hepatomegalia = Str()
    esplenomegalia = Str()
    hemorragia = Str()
