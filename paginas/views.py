from django.shortcuts import render
from servicos.models import Divulgacao, HorarioSetor, Setor, Refeicao
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    setores = Setor.objects.all()
    refeicoes = Refeicao.objects.all()
    context = {
        'setores': setores, 
        'refeicoes': refeicoes
    }
    return render(request, 'home.html', context)

def setores_view(request):
    if 'q' in request.GET:
        procura = request.GET['q']
        setores = Setor.objects.filter(nome__icontains=procura)
        setores_info = {}
    else: 
        setores = Setor.objects.all()
        setores_info = {}

    for setor in setores:
        setor_info = {'nome': setor.nome, 'horarios': []}

        for horario in setor.horario_do_setor.all():
            info_horario = {
                'dia_semana': horario.dia_semana,
                'horario_inicio': horario.horario_inicio,
                'horario_fim': horario.horario_fim
            }
            setor_info['horarios'].append(info_horario)
        setores_info[setor.nome] = setor_info

    context = {'setores_info': setores_info}
    return render(request, 'setores.html', context)

def divulgacoes_view(request):
    return render(request, 'divulgacoes.html')

def tela_admin_view(request):
    divulgacoes = Divulgacao.objects.all().order_by('data_registro')
    paginacao = Paginator(divulgacoes, 5)

    page_number = request.GET.get("page")
    page_obj = paginacao.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'tela_admin.html', context=context)
