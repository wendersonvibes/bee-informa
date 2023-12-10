from django.contrib import admin
from .models import Divulgacao, Imagem, TipoDivulgacao, Setor, HorarioSetor, TipoRefeicao, Refeicao

admin.site.register(TipoDivulgacao)

@admin.register(Divulgacao)
class DivulgacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']

@admin.register(Imagem)
class ImagemDivulgacaoAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

admin.site.register(HorarioSetor)
admin.site.register(TipoRefeicao)
admin.site.register(Refeicao)