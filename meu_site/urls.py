from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emprestimos.urls')),  # página inicial -> painel da biblioteca
    path('livros/', include('livros.urls')),
    path('usuarios/', include('usuarios.urls')),
]

