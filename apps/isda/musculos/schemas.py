# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str
from main.messages import MSG_FIELD_REQUIRED, MSG_ALREADY_EXISTS


class MusculosSchema(Schema):
    atrofia_muscular = Str()
    dificuldade_andar = Str()
    fraqueza_muscular = Str()
    dor = Str()
    caibras = Str()
    espasmos_musculares = Str()
