from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings

# TIPOS DE DIVULGAÇÃO
class TipoDivulgacao(models.Model):
    tipo_divulgacao = models.CharField(verbose_name="Tipo de divulgação", max_length=50)

    class Meta:
        verbose_name = "Tipo de divulgação"
        verbose_name_plural = "Tipos de divulgação"

    def __str__(self):
        return self.tipo_divulgacao

# DIVULGAÇÕES   
class Divulgacao(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=50)
    conteudo = RichTextField(verbose_name="Conteúdo", config_name='awesome_ckeditor')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuário", on_delete=models.SET_NULL, null=True)
    data_registro = models.DateField(verbose_name='Data de Registro', auto_now=True)
    tipo = models.ForeignKey(TipoDivulgacao, related_name="divulgacao_do_tipo", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Divulgação"
        verbose_name_plural = "Divulgações"
        
    def __str__(self):
        return self.titulo

# IMAGENS
class Imagem(models.Model):
    imagem = models.FileField("Imagens", upload_to="imagem")
    divulgacao = models.ForeignKey(Divulgacao, related_name="imagem_da_divulgacao", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self):
        return self.divulgacao.titulo
    
# SETORES 
class Setor(models.Model):
    BLOCO_CHOICES = (
        ("A", "A"),
        ("B", "B")
    )

    nome = models.CharField(verbose_name="Nome do setor", max_length=25)
    bloco = models.CharField(verbose_name="Bloco do setor", choices=BLOCO_CHOICES, max_length=1)
    numero = models.IntegerField(verbose_name="Número da sala")
    
    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    def __str__(self):
        return self.nome

# HORÁRIOS DOS SETORES 
class HorarioSetor(models.Model):
    DIAS_SEMANA_CHOICES = (
        ("SEG", "Segunda-feira"),
        ("TER", "Terça-feira"),
        ("QUA", "Quarta-feira"),
        ("QUI", "Quinta-feira"),
        ("SEX", "Sexta-feira")
    )

    horario_inicio = models.TimeField(verbose_name="Horário de início", auto_now_add=False)
    horario_fim = models.TimeField(verbose_name="Horário de fim", auto_now_add=False)
    setor = models.ForeignKey(Setor, related_name="horario_do_setor", on_delete=models.SET_NULL, null=True)
    dia_semana = models.CharField(verbose_name="Dia da semana", choices=DIAS_SEMANA_CHOICES, max_length=3)

    class Meta:
        verbose_name = "Horário do setor"
        verbose_name_plural = "Horários dos setores"

    def __str__(self):
        return (f'{self.setor.nome} ({self.horario_inicio} - {self.horario_fim}) - {self.dia_semana}')
    
class TipoRefeicao(models.Model):
    tipo_refeicao = models.CharField(verbose_name="Tipo de refeição", max_length=50)

    class Meta:
        verbose_name = "Tipo de refeição"
        verbose_name_plural = "Tipos de refeição"

    def __str__(self):
        return self.tipo_refeicao

class Refeicao(models.Model):
    DIAS_SEMANA_CHOICES = (
        ("SEG", "Segunda-feira"),
        ("TER", "Terça-feira"),
        ("QUA", "Quarta-feira"),
        ("QUI", "Quinta-feira"),
        ("SEX", "Sexta-feira")
    )

    horario_inicio = models.TimeField(verbose_name="Horário de início", auto_now_add=False)
    horario_fim = models.TimeField(verbose_name="Horário de fim", auto_now_add=False)
    dia_semana = models.CharField(verbose_name="Dia da semana", choices=DIAS_SEMANA_CHOICES, max_length=3)
    descricao = models.TextField(verbose_name="Descrição do cardápio")
    data = models.DateField(verbose_name="Data", blank=True, null=True)
    tipo_refeicao = models.ForeignKey(TipoRefeicao, related_name="cardapio_da_refeicao", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Refeicao"
        verbose_name_plural = "Refeições"

    def __str__(self):
        return (f"{self.tipo_refeicao.tipo_refeicao} ({self.data} - {self.dia_semana})")
    
