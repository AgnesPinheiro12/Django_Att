from django.views.generic import ListView

from .models import Livro


class LivroListView(ListView):
    """Mostra todos os livros cadastrados."""
    model = Livro
    template_name = 'livros/lista_livros.html'
    context_object_name = 'livros'
