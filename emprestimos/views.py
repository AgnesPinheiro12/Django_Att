from django.shortcuts import render

from livros.models import Livro
from usuarios.models import Usuario

from .models import Emprestimo


def relatorio_emprestimos(request):
    """Página principal: livros, usuários e empréstimos da biblioteca."""
    contexto = {
        'livros': Livro.objects.all(),
        'usuarios': Usuario.objects.all(),
        'emprestimos': Emprestimo.objects.all(),
    }
    return render(request, 'emprestimos/relatorio.html', contexto)
