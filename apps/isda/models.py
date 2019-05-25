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
from apps.isda.coluna_vertebral.models import ColunaVertebral


class Isda(EmbeddedDocument):
    '''
    Entidade Isda
    '''
    meta = {'collection': 'Isda'}

    coluna_vertebral = EmbeddedDocumentField(ColunaVertebral,
        default=ColunaVertebral)
