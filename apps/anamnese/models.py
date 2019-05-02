#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python
from datetime import datetime


# Third
from mongoengine import (
    DateTimeField,
    EmbeddedDocumentField
)


# Apps
from main.db.db import db
from apps.aluno.models import Aluno
from apps.paciente.models import Paciente


class Anamnese(db.Document):
    '''
    Entidade Anamnese
    '''
    meta = {'collection': 'anamnese'}

    aluno = EmbeddedDocumentField(Aluno, default=Aluno)
    paciente = EmbeddedDocumentField(Paciente, default=Paciente)
    created_at = DateTimeField(default=datetime.now)
