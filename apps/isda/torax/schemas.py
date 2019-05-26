# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str
from main.messages import MSG_FIELD_REQUIRED, MSG_ALREADY_EXISTS


class ToraxSchema(Schema):

    traqueia_dor = Str()
    traqueia_tosse = Str()
    traqueia_expectoracao = Str()
    traqueia_hemoptise = Str()
    traqueia_vomica = Str()
    traqueia_chieira = Str()
    traqueia_estridor = Str()
    traqueia_triagem = Str()
    parede_toraxica_dor = Str()
    parede_toraxica_dispineia = Str()
    mamas_dor = Str()
    mamas_nodulo = Str()
    mamas_secrecao = Str()
    diafragma_dor = Str()
    diafragma_soluco = Str()
    diafragma_sintomas_compressao = Str()
    coracao_dor = Str()
    coracao_palpitacoes = Str()
    coracao_intolerancia_esforcos = Str()
    coracao_desmaio_esforco = Str()
    coracao_cianose = Str()
    coracao_edema = Str()
    coracao_astenia = Str()
    coracao_alteracoes_sono = Str()
    esofago_dor = Str()
    esofago_disfagia = Str()
    esofago_odinofagia = Str()
    esofago_pirose = Str()
    esofago_regurgitacao = Str()
    esofago_hematemese = Str()
