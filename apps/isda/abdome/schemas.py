    # -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str

class AbdomeSchema(Schema):

    paredeabdominal_dor = Str()
    paredeabdominal_alteracao = Str()
    pancreas_dor = Str()
    pancreas_diarreia = Str()
    pancreas_nauseas = Str()
    figado_dor = Str()
    figado_ictericia = Str()
    estomago_dor = Str()
    estomago_nauseas = Str()
    estomago_dispepsia = Str()
    estomago_pirose = Str()
    intestino_dor = Str()
    intestino_diarreia = Str()
    intestino_esteatorreia = Str()
    intestino_distensao = Str()
    intestino_hemorragia = Str()
    colon_dor = Str()
    colon_diarreia = Str()
    colon_obstipacao = Str()
    colon_sangramento = Str()
    colon_prurido = Str()
