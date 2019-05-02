# -*- coding:utf-8 -*-

# Python

# Flask
from flask import request

# Third
from flask_restful import Resource

from mongoengine.errors import (
    NotUniqueError, ValidationError, FieldDoesNotExist)

# Apps
from apps.responses import (
    resp_already_exists,
    resp_exception,
    resp_data_invalid,
    resp_ok
)
from main.messages import MSG_NO_DATA, MSG_INVALID_DATA
from main.messages import (
    MSG_RESOURCE_CREATED, MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_DELETED)

# Local
from .models import Anamnese
from .schemas import AnamneseSchema
from .utils import get_anamnese_by_id


class addAnamnese(Resource):
    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        schema = AnamneseSchema()

        # Se meus dados postados forem Nulos retorno uma respota inválida
        if req_data is None:
            return resp_data_invalid('Anamnese', [], msg=MSG_NO_DATA)

        data, errors = schema.load(req_data)

        if errors:
            return resp_data_invalid('Anamnese', errors)

        try:
            model = Anamnese(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists('Anamnese', 'anamnese')

        except ValidationError as e:
            return resp_exception(
                'Anamnese', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Anamnese', description=e.__str__())

        schema = AnamneseSchema()
        result = schema.dump(model)

        return resp_ok(
            'Anamnese',
            MSG_RESOURCE_CREATED.format('Anamnese'), data=result.data
        )

    def get(self, page_id=1):
        # inicializa o schema podendo conter varios objetos
        schema = AnamneseSchema(many=True)
        # incializa o page_size sempre com 10
        page_size = 10

        # se enviarmos o page_size como parametro
        if 'page_size' in request.args:
            # verificamos se ele é menor que 1
            if int(request.args.get('page_size')) < 1:
                page_size = 10
            else:
                # fazemos um type cast convertendo para inteiro
                page_size = int(request.args.get('page_size'))

        try:
            # buscamos todos os usuarios da base utilizando o paginate
            anamneses = Anamnese.objects().paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception('Anamnese', description=e.__str__())

        except Exception as e:
            return resp_exception('Anamnese', description=e.__str__())

        # criamos dados extras a serem respondidos
        extra = {
            'page': anamneses.page, 'pages': anamneses.pages,
            'total': anamneses.total, 'params': {'page_size': page_size}
        }

        # fazemos um dump dos objetos pesquisados
        result = schema.dump(anamneses.items)

        return resp_ok(
            'Anamnese', MSG_RESOURCE_FETCHED_PAGINATED.format('anamneses'),
            data=result.data,
            **extra
        )

    def delete(self, anamnese_id):
        # Busco uma anamnese na coleção users pelo seu id
        anamnese = get_anamnese_by_id(anamnese_id)
        # se não for uma instancia do modelo User retorno uma resposta
        # da requisição http do flask
        if not isinstance(anamnese, Anamnese):
            return anamnese

        try:
            anamnese.save()

        except NotUniqueError:
            return resp_already_exists('Anamnese', 'anamnese')

        except ValidationError as e:
            return resp_exception(
                'Anamnese', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Anamnese', description=e.__str__())

        return resp_ok('Anamnese', MSG_RESOURCE_DELETED.format('Anamnese'))
