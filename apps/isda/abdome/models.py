
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Third
from mongoengine import (
    StringField,
    EmbeddedDocument
)


class Abdome(EmbeddedDocument):
    '''
    Entidade Abdome
    '''
    meta = {
        'ordering': ['paredeabdominal_dor']
    }
    paredeabdominal_dor = StringField(max_length=250)
    paredeabdominal_alteracao = StringField(max_length=250)
    pancreas_dor = StringField(max_length=250)
    pancreas_diarreia = StringField(max_length=250)
    pancreas_nauseas = StringField(max_length=250)
    figado_dor = StringField(max_length=250)
    figado_ictericia = StringField(max_length=250)
    estomago_dor = StringField(max_length=250)
    estomago_nauseas = StringField(max_length=250)
    estomago_dispepsia = StringField(max_length=250)
    estomago_pirose = StringField(max_length=250)
    intestino_dor = StringField(max_length=250)
    intestino_diarreia = StringField(max_length=250)
    intestino_esteatorreia = StringField(max_length=250)
    intestino_distensao = StringField(max_length=250)
    intestino_hemorragia = StringField(max_length=250)
    colon_dor = StringField(max_length=250)
    colon_diarreia = StringField(max_length=250)
    colon_obstipacao = StringField(max_length=250)
    colon_sangramento = StringField(max_length=250)
    colon_prurido = StringField(max_length=250)
