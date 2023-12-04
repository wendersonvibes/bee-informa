from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings

class TipoDivulgacao(models.Model):
    tipo_divulgacao = models.CharField(verbose_name="Tipo de divulgação", max_length=50)

    def __str__(self):
        return self.tipo_divulgacao
    
class Divulgacao(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=50)
    conteudo = RichTextField(verbose_name="Conteúdo", config_name='awesome_ckeditor')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuário", on_delete=models.CASCADE)
    data_registro = models.DateField(verbose_name='Data de Registro', auto_now=True)
    tipo = models.ForeignKey(TipoDivulgacao, related_name="divulgacao_do_tipo", on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

class Imagem(models.Model):
    imagem = models.FileField("Imagens", upload_to="imagem")
    divulgacao = models.ForeignKey(Divulgacao, related_name="imagem_da_divulgacao", on_delete=models.CASCADE)

    def __str__(self):
        return self.divulgacao.titulo