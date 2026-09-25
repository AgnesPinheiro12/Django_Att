from django.shortcuts import render
from .models import Matricula
from alunos.models import Aluno
from cursos.models import Curso

def relatorio_geral(request):
    """Página principal: alumnos, cursos e matrículas com seu status."""
    contexto = {
        'alumnos': Aluno.objects.all(),
        'cursos': Curso.objects.all(),
        'matriculas': Matricula.objects.all(),
    }
    return render(request, 'matriculas/relatorio.html', contexto)


# Create your views here.
