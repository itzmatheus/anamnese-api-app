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
from apps.isda.models import Isda
from apps.exame_fisico.models import ExameFisico


class Anamnese(db.Document):
    '''
    Entidade Anamnese
    '''
    meta = {'collection': 'anamnese'}

    aluno = EmbeddedDocumentField(Aluno, default=Aluno)
    paciente = EmbeddedDocumentField(Paciente, default=Paciente)
    isda = EmbeddedDocumentField(Isda, default=Isda)
    exame_fisico = EmbeddedDocumentField(ExameFisico, default=ExameFisico)
    created_at = DateTimeField(default=datetime.now)
