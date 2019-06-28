# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Nested, Str

# Apps
from apps.isda.coluna_vertebral.schemas import ColunaVertebralSchema
from apps.isda.musculos.schemas import MusculosSchema
from apps.isda.nervoso.schemas import NervosoSchema
from apps.isda.habitos_de_vida.schemas import HabitosDeVidaSchema
from apps.isda.abdome.schemas import AbdomeSchema
from apps.isda.ectoscopia.schemas import EctoscopiaSchema
from apps.isda.sintomas_gerais.schemas import SintomasGeraisSchema
from apps.isda.antecedentes.schemas import AntecedentesSchema
from apps.isda.sistema_geniturinario.schemas import SistemaGeniturinarioSchema
from apps.isda.sistema_hemolinfopetico.schemas import SistemaHemolinfopeticoSchema
from apps.isda.torax.schemas import ToraxSchema


class IsdaSchema(Schema):
    coluna_vertebral = Nested(ColunaVertebralSchema)
    musculos = Nested(MusculosSchema)
    nervoso = Nested(NervosoSchema)
    habitos_de_vida = Nested(HabitosDeVidaSchema)
    abdome = Nested(AbdomeSchema)
    ectoscopia = Nested(EctoscopiaSchema)
    sintomas_gerais = Nested(SintomasGeraisSchema)
    antecedentes = Nested(AntecedentesSchema)
    sistema_geniturinario = Nested(SistemaGeniturinarioSchema)
    sistema_hemolinfopetico = Nested(SistemaHemolinfopeticoSchema)
    torax = Nested(ToraxSchema)
