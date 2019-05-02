# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Nested, Str, DateTime

# Apps
from apps.aluno.schemas import AlunoRegistrationSchema
from apps.paciente.schemas import PacienteRegistrationSchema


class AnamneseSchema(Schema):
    aluno = Nested(AlunoRegistrationSchema)
    paciente = Nested(PacienteRegistrationSchema)
    id = Str()
    created_at = DateTime()
