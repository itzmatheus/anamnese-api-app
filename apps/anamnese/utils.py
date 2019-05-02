# -*- coding: utf-8

from mongoengine.errors import FieldDoesNotExist, DoesNotExist
from .models import Anamnese
from apps.responses import resp_exception, resp_does_not_exist


def get_anamnese_by_id(anamnese_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return Anamnese.objects.get(id=anamnese_id)

    except DoesNotExist:
        return resp_does_not_exist('anamneses', 'Anamnese')

    except FieldDoesNotExist as e:
        return resp_exception('anamneses', description=e.__str__())

    except Exception as e:
        return resp_exception('anamneses', description=e.__str__())
