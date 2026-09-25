from django.db import models

from livros.models import Livro
from usuarios.models import Usuario


class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos', verbose_name='Usuário')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos', verbose_name='Livro')
    data_emprestimo = models.DateField('Data do empréstimo', auto_now_add=True)
    data_devolucao = models.DateField('Data de devolução', null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f'{self.usuario.nome} - {self.livro.titulo}'
