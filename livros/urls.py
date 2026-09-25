from django.urls import path

from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.LivroListView.as_view(), name='lista_livros'),
]