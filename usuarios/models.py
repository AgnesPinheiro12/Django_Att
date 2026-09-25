from django.db import models


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, default='')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']

    def __str__(self):
        return self.nome
