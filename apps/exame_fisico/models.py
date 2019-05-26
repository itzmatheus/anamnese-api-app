#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python
from datetime import datetime


# Third
from mongoengine import (
    DateTimeField,
    EmbeddedDocumentField,
    EmbeddedDocument
)


# Apps
from main.db.db import db
from apps.exame_fisico.respiratorio.models import Respiratorio
from apps.exame_fisico.cardiovascular.models import Cardiovascular

class ExameFisico(EmbeddedDocument):
    '''
    Entidade ExameFisico
    '''
    meta = {'collection': 'Exame Fisico'}

    respiratorio = EmbeddedDocumentField(Respiratorio,
        default=Respiratorio)
    cardiovascular = EmbeddedDocumentField(Cardiovascular,
        default=Cardiovascular)
