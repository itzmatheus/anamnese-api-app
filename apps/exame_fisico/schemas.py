# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Nested, Str

# Apps
from apps.exame_fisico.respiratorio.schemas import RespiratorioSchema
from apps.exame_fisico.cardiovascular.schemas import CardiovascularSchema
from apps.exame_fisico.abdome.schemas import AbdomeSchema

class ExameFisicoSchema(Schema):
    respiratorio = Nested(RespiratorioSchema)
    cardiovascular = Nested(CardiovascularSchema)
    abdome = Nested(AbdomeSchema)
