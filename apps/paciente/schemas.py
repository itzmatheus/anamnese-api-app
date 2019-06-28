# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str, Int, DateTime
from main.messages import MSG_FIELD_REQUIRED


class PacienteRegistrationSchema(Schema):
    nome = Str(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})
    sexo = Str()
    leito = Str()
    queixa_principal = Str()
    profissao = Str()
    cor = Str()
    estado_civil = Str()
    religiao = Str()
    posicionamento_sexual = Str()
    nacionalidade = Str()
    hora_inicio = DateTime()
    idade = Int()
    enfermaria = Str()
