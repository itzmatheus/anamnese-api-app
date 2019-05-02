# -*- coding: utf-8 -*-

# Python
import json

# Third
# Importando client
from tests.test_conf import client


# Criando funcao test_index_response como parametro o cliente criado no arquivo
def test_index_response_200(client):
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/')

    # Verificamos a assertividade do código de resposta da requisição
    # http. Ela deve ser exatamente igual 200 retornando um True para
    # o teste
    assert response.status_code == 200


def test_home_response_hello(client):
    """
    **Given** Luiza está acessando a API,
    **When** ela informa a rota/endpoint `/`,
    **Then** a api deve responder um objeto com a chave `['status']`,
    **And** seu conteúdo deve ser `OK`
    """
    # Realiza uma requisição HTTP do tipo get para o endpoint /
    response = client.get('/')

    # Utilizamos a função loads do modulo json para retornar um dict
    # para a váriavel data.
    # Precisamos passar por parâmetro para essa função a resposta
    # retornada pelo servidor, através da váriavel response.data
    # e decodificar para utf-8
    data = json.loads(response.data.decode('utf-8'))
    # Fazemos o teste de asserção pela chave 'status'
    assert data['status'] == 'OK'
