# -*- coding: utf-8

# Third

from mongoengine.errors import (
    FieldDoesNotExist, DoesNotExist, MultipleObjectsReturned)

# Apps
from apps.responses import resp_exception, resp_does_not_exist

# Local
from .models import Aluno


def check_password_in_signup(password: str, confirm_password: str):

    if not password:
        return False

    if not confirm_password:
        return False

    if not password == confirm_password:
        return False

    return True


def get_aluno_by_id(aluno_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return Aluno.objects.get(id=aluno_id)

    except DoesNotExist:
        return resp_does_not_exist('Aluno', 'Usuário')

    except FieldDoesNotExist as e:
        return resp_exception('Aluno', description=e.__str__())

    except Exception as e:
        return resp_exception('Aluno', description=e.__str__())


def exists_email_in_alunos(email: str, instance=None):
    """
    Verifico se existe um usuário com aquele email
    """
    aluno = None

    try:
        aluno = Aluno.objects.get(email=email)

    except DoesNotExist:
        return False

    except MultipleObjectsReturned:
        return True

    # verifico se o id retornado na pesquisa é mesmo da minha instancia
    # informado no parâmetro
    if instance and instance.id == aluno.id:
        return False

    return True


def get_aluno_by_email(email: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return Aluno.objects.get(email=email)

    except DoesNotExist:
        return resp_does_not_exist('Aluno', 'Usuário')

    except FieldDoesNotExist as e:
        return resp_exception('Aluno', description=e.__str__())

    except Exception as e:
        return resp_exception('Aluno', description=e.__str__())
