from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import ListaMatriculasAlunoSerializer, AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """
    Retorna as matrículas de um aluno ou uma lista vazia caso o aluno não exista
    """
    def get_queryset(self):
       queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
       return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """
    Retorna uma lista de alunos matriculados em um curso ou uma lista vazia caso o curso não exista
    """
    def get_queryset(self):
       queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
       return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]