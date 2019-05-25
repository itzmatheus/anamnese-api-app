# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str


class ColunaVertebralSchema(Schema):
    dor = Str()
    rigidez = Str()
    sinais_inflamatorios = Str()
    crepitacao_articular = Str()
    manifestacao_sistemica = Str()
