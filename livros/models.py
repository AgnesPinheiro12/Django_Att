from django.db import models


class Livro(models.Model):
    titulo = models.CharField('Título', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.CharField('ISBN', max_length=20, blank=True, default='')
    editora = models.CharField(max_length=100, blank=True, default='')
    ano_publicacao = models.PositiveIntegerField('Ano de publicação', null=True, blank=True)
    exemplares = models.PositiveIntegerField('Exemplares', default=1)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    @property
    def esta_disponivel(self):
        """Um livro está disponível enquanto houver menos empréstimos ativos do que exemplares."""
        ativos = self.emprestimos.filter(ativo=True).count()
        return ativos < self.exemplares
