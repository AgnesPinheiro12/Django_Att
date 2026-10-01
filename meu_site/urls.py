from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 📌 Rotas dos seus Apps (Organizadas por caminho único)
    path('emprestimos/', include('emprestimos.urls')),  # Mudado de '' para 'emprestimos/' para liberar a home
    path('livros/', include('livros.urls')),
    path('usuarios/', include('usuarios.urls')),
    
    # 🏠 Página Inicial Única do Site todo (Cai no seu index.html geral)
    path('', index, name='index'),  
]
