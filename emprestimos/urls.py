from django.urls import path

from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('', views.relatorio_emprestimos, name='relatorio_emprestimos'),
]