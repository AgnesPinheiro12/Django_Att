from django.contrib import admin

from .models import Emprestimo


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'ativo')
    list_filter = ('ativo', 'data_emprestimo')
    search_fields = ('usuario__nome', 'livro__titulo')

    @admin.action(description='Marcar como devolvidos')
    def marcar_como_devolvido(self, request, queryset):
        from django.utils import timezone
        queryset.update(ativo=False, data_devolucao=timezone.localdate())

    actions = ['marcar_como_devolvido']
