from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Estudante
    fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = ['id', 'codigo', 'descricao', 'nivel']

class MatriculaSerializers(serializers.ModelSerializer):
  class Meta:
    model = Matricula
    exclude = []

class ListaMatriculasEstudanteSerializers(serializers.ModelSerializer):
  curso = serializers.ReadOnlyField(source='curso.descricao')
  periodo = serializers.SerializerMethodField()
  class Meta:
    model = Matricula
    fields = ['curso', 'periodo']

  def get_periodo(self, obj):
    return obj.get_periodo_display()
  
class ListaMatriculasCursoSerializers(serializers.ModelSerializer):
  estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
  class Meta:
    model = Matricula
    fields = ['estudante_nome']