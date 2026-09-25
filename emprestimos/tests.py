from datetime import date

from django.test import TestCase

from livros.models import Livro
from usuarios.models import Usuario

from .models import Emprestimo


class EmprestimoTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nome='Ana', email='ana@example.com')
        self.livro = Livro.objects.create(titulo='Duna', autor='Frank Herbert', isbn='ABC-123')

    def test_livro_disponivel_sem_emprestimos(self):
        self.assertTrue(self.livro.esta_disponivel)

    def test_livro_emprestado_com_emprestimo_ativo(self):
        Emprestimo.objects.create(usuario=self.usuario, livro=self.livro)
        self.assertFalse(Livro.objects.get(pk=self.livro.pk).esta_disponivel)

    def test_livro_disponivel_apos_devolucao(self):
        emprestimo = Emprestimo.objects.create(usuario=self.usuario, livro=self.livro)
        emprestimo.data_devolucao = date.today()
        emprestimo.ativo = False
        emprestimo.save()
        self.assertTrue(Livro.objects.get(pk=self.livro.pk).esta_disponivel)
