from django.shortcuts import render
from servicos.models import Divulgacao
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def setores_view(request):
    return render(request, 'setores.html')

def divulgacoes_view(request):
    return render(request, 'divulgacoes.html')

def tela_admin_view(request):
    divulgacoes = Divulgacao.objects.all().order_by('data_registro')
    paginacao = Paginator(divulgacoes, 5)

    page_number = request.GET.get("page")
    page_obj = paginacao.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'tela_admin.html', context=context)
