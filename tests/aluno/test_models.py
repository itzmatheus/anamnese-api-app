# Third

from mongoengine import (
    IntField,
    StringField
)

# Apps
from apps.aluno.models import Aluno


class TestAluno:

    def setup_method(self):
        self.data = {
            'nome': 'Matheus José', 'email': 'matheusjoselfm@gmail.com',
            'matricula': 1720020805, 'grupo': 'grupo 01'
        }

        # Crio uma instancia do modelo Aluno
        self.model = Aluno(**self.data)

    def test_matricula_field_exists(self):
        """
        Verifico se o campo matricula existe
        """
        assert 'matricula' in self.model._fields

    def test_matricula_field_is_required(self):
        """
        Verifico se o campo matricula é requirido
        """
        assert self.model._fields['matricula'].required is True

    def test_matricula_field_is_unique(self):
        """
        Verifico se o campo matricula é unico
        """
        assert self.model._fields['matricula'].unique is True

    def test_matricula_field_is_str(self):
        """
        Verifico se o campo matricula é do tipo string
        """
        assert isinstance(self.model._fields['matricula'], IntField)

    def test_nome_field_exists(self):
        """
        Verifico se o campo nome existe
        """
        assert 'nome' in self.model._fields

    def test_nome_field_is_str(self):
        assert isinstance(self.model._fields['nome'], StringField)

    def test_all_fields_in_model(self):
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'nome', 'email', 'matricula', 'grupo'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys
