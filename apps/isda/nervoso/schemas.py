    # -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str
from main.messages import MSG_FIELD_REQUIRED, MSG_ALREADY_EXISTS


class NervosoSchema(Schema):
    grupo = Str()
    disturbios_consciencia = Str()
    cefaleia = Str()
    tontura_vertigem = Str()
    ausencias = Str()
    convusoes = Str()
    automatismos = Str()
    amnesia = Str()
    disturbios_visuais = Str()
    disturbios_auditivos = Str()
    disturbios_mancha = Str()
    disturbios_motricidade = Str()
    disturbios_esfincterianos = Str()
    disturbios_sono = Str()
    disturbios_funcoes = Str()
    outros = Str()
