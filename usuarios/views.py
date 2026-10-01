from django.views.generic import ListView

from .models import Usuario


class UsuarioListView(ListView):
    """Mostra todos os usuários cadastrados."""
    model = Usuario
    template_name = 'usuarios/index.html'
    context_object_name = 'usuarios'
