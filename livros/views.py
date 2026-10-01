from django.views.generic import ListView

from .models import Livro


class LivroListView(ListView):
    """Mostra todos os livros cadastrados."""
    model = Livro
    template_name = 'livros/index.html'
    context_object_name = 'livros'
