# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Nested, Str, DateTime

# Apps
from apps.aluno.schemas import AlunoRegistrationSchema
from apps.paciente.schemas import PacienteRegistrationSchema
from apps.isda.schemas import IsdaSchema
from apps.exame_fisico.schemas import ExameFisicoSchema

class AnamneseSchema(Schema):
    id = Str()
    aluno = Nested(AlunoRegistrationSchema)
    paciente = Nested(PacienteRegistrationSchema)
    isda = Nested(IsdaSchema)
    exame_fisico = Nested(ExameFisicoSchema)
    created_at = DateTime()
    comentarios = Str()
    anotacoes_globais = Str()

