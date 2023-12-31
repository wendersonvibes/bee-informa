# Generated by Django 4.2.7 on 2023-12-10 00:19

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Divulgacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('conteudo', ckeditor.fields.RichTextField(verbose_name='Conteúdo')),
                ('data_registro', models.DateField(auto_now=True, verbose_name='Data de Registro')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Divulgação',
                'verbose_name_plural': 'Divulgações',
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25, verbose_name='Nome do setor')),
                ('bloco', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1, verbose_name='Bloco do setor')),
                ('numero', models.IntegerField(verbose_name='Número da sala')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='TipoDivulgacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_divulgacao', models.CharField(max_length=50, verbose_name='Tipo de divulgação')),
            ],
            options={
                'verbose_name': 'Tipo de divulgação',
                'verbose_name_plural': 'Tipos de divulgação',
            },
        ),
        migrations.CreateModel(
            name='TipoRefeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_refeicao', models.CharField(max_length=50, verbose_name='Tipo de refeição')),
            ],
            options={
                'verbose_name': 'Tipo de refeição',
                'verbose_name_plural': 'Tipos de refeição',
            },
        ),
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_inicio', models.TimeField(verbose_name='Horário de início')),
                ('horario_fim', models.TimeField(verbose_name='Horário de fim')),
                ('dia_semana', models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira')], max_length=3, verbose_name='Dia da semana')),
                ('descricao', models.TextField(verbose_name='Descrição do cardápio')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('tipo_refeicao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cardapio_da_refeicao', to='servicos.tiporefeicao')),
            ],
            options={
                'verbose_name': 'Refeicao',
                'verbose_name_plural': 'Refeições',
            },
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.FileField(upload_to='imagem', verbose_name='Imagens')),
                ('divulgacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagem_da_divulgacao', to='servicos.divulgacao')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.CreateModel(
            name='HorarioSetor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_inicio', models.TimeField(verbose_name='Horário de início')),
                ('horario_fim', models.TimeField(verbose_name='Horário de fim')),
                ('dia_semana', models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira')], max_length=3, verbose_name='Dia da semana')),
                ('setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horario_do_setor', to='servicos.setor')),
            ],
            options={
                'verbose_name': 'Horário do setor',
                'verbose_name_plural': 'Horários dos setores',
            },
        ),
        migrations.AddField(
            model_name='divulgacao',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='divulgacao_do_tipo', to='servicos.tipodivulgacao'),
        ),
    ]
