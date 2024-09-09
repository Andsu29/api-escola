from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializers, ListaMatriculasCursoSerializers, ListaMatriculasEstudanteSerializers
from rest_framework import viewsets, generics

class EstudanteViewSet(viewsets.ModelViewSet):
  queryset = Estudante.objects.all()
  serializer_class = EstudanteSerializer
  
class CursoViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
   queryset = Matricula.objects.all()
   serializer_class = MatriculaSerializers

class ListaMatriculaEstudante(generics.ListAPIView):
  def get_queryset(self):
    queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasEstudanteSerializers

class ListaMatriculaCurso(generics.ListAPIView):
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasCursoSerializers