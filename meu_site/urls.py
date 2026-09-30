from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emprestimos.urls')),  # página inicial -> painel da biblioteca
    path('livros/', include('livros.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', index, name='index'),  # página inicial -> index.html
]

