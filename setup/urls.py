from django.contrib import admin
from django.urls import path, include
from escola.views import ListaMatriculasAluno, AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'cursos', CursosViewSet, basename='Cursos')
router.register(r'matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view(), name='matriculas_aluno'),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view(), name='alunos_matriculados'),
]
