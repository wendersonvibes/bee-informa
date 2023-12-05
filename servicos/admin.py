from django.contrib import admin
from .models import Divulgacao, Imagem, TipoDivulgacao

admin.site.register(TipoDivulgacao)

@admin.register(Divulgacao)
class DivulgacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']

@admin.register(Imagem)
class ImagemDivulgacaoAdmin(admin.ModelAdmin):
    list_display = ['id']