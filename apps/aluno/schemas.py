# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Email, Str, Int
from main.messages import MSG_FIELD_REQUIRED, MSG_ALREADY_EXISTS


class AlunoRegistrationSchema(Schema):
    nome = Str(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})
    matricula = Int(required=True, unique=True, error_messages={
        'required': MSG_FIELD_REQUIRED, 'unique': MSG_ALREADY_EXISTS})
    email = Email()
    grupo = Str()
