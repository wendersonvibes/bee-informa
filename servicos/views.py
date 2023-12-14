from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator

from .forms import DivulgacaoForm, SetorForm, HorarioSetorForm, RefeicaoForm
from .models import Divulgacao, Imagem, Setor, HorarioSetor, Refeicao

########################## DIVULGAÇÕES ##########################

def admin_divulgacao_list(request):
    divulgacoes = Divulgacao.objects.all().order_by('data_registro')
    paginacao = Paginator(divulgacoes, 5)

    page_number = request.GET.get("page")
    page_obj = paginacao.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, "divulgacoes/divulgacao_list.html", context)

def divulgacao_list(request):
    divulgacoes = Divulgacao.objects.all()
    context = {'divulgacoes': divulgacoes}
    return render(request, "divulgacoes.html", context)

def divulgacao_detail(request, id):
    divulgacao = get_object_or_404(Divulgacao, id=id)
    return render(request, "divulgacoes/divulgacao_detail.html", {'divulgacao': divulgacao})

def divulgacao_create(request):
    if (request.method == "POST"):
        form = DivulgacaoForm(request.POST, request.FILES)
        autor = request.user
        if form.is_valid():
            divulgacao = form.save(commit=False)
            divulgacao.autor = autor
            divulgacao.save()
            # salva o form
            imagens = request.FILES.getlist("imagem_da_divulgacao") # coloca as imagens numa lista

            if (imagens):
                for img in imagens: # cria os objetos em ImagemDivulgacao
                    Imagem.objects.create(
                        divulgacao=divulgacao, imagem = img # atributos da classe ImagemDivulgacao
                    )
            return HttpResponseRedirect(reverse("admin-divulgacao-list"))
    
    else:
        form = DivulgacaoForm()
    return render(request, "divulgacoes/divulgacao_create.html", {'form': form})

def divulgacao_delete(request, id):
    divulgacao = Divulgacao.objects.get(id=id)
    if (request.method == "POST"):
        divulgacao.delete()
        return HttpResponseRedirect(reverse("admin-divulgacao-list"))
    return render(request, "divulgacoes/divulgacao_delete.html", {'divulgacao': divulgacao})

def divulgacao_update(request, id):
    divulgacao = get_object_or_404(Divulgacao, id=id)
    form = DivulgacaoForm(request.POST or None, request.FILES or None, instance=divulgacao)
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin-divulgacao-list"))
    return render(request, "divulgacoes/divulgacao_update.html", {'form': form})

########################## SETOR ##########################
def admin_setor_list(request):
    setores = Setor.objects.all().order_by("nome")
    paginacao = Paginator(setores, 5)

    page_number = request.GET.get("page")
    page_obj = paginacao.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, "setores/setor_list.html", context)

def setor_create(request):
    if (request.method == "POST"):
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save() # salva o form
            return HttpResponseRedirect(reverse("admin-setor-list"))
    else:
        form = SetorForm()
    return render(request, "setores/setor_create.html", {'form': form})

def setor_delete(request, id):
    setor = Setor.objects.get(id=id)
    if (request.method == "POST"):
        setor.delete()
        return HttpResponseRedirect(reverse("setor-list"))
    return render(request, "setores/setor_delete.html", {'setor': setor})

def setor_update(request, id):
    setor = get_object_or_404(Setor, id=id)
    form = SetorForm(request.POST or None, instance=setor)
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("setor-list"))
    return render(request, "setores/setor_update.html", {'form': form})

########################## HORÁRIO DO SETOR ##########################
def admin_horario_setor_list(request):
    horarios = HorarioSetor.objects.all().order_by("setor")
    paginacao = Paginator(horarios, 5)

    page_number = request.GET.get("page")
    page_obj = paginacao.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, "setores/horarios/horario_setor_list.html", context)

def horario_setor_create(request):
    if (request.method == "POST"):
        form = HorarioSetorForm(request.POST)
        if form.is_valid():
            form.save() # salva o form
            return HttpResponseRedirect(reverse("admin-horario-setor-list"))
    form = HorarioSetorForm()
    return render(request, "setores/horarios/horario_setor_create.html", {'form': form})

def horario_setor_delete(request, id):
    horario_setor = HorarioSetor.objects.get(id=id)
    if (request.method == "POST"):
        horario_setor.delete()
        return HttpResponseRedirect(reverse("admin-horario-setor-list"))
    return render(request, "setores/horarios/horario_setor_delete.html", {'horario': horario_setor})

def horario_setor_update(request, id):
    horario_setor = get_object_or_404(HorarioSetor, id=id)
    form = HorarioSetorForm(request.POST or None, instance=horario_setor)
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin-horario-setor-list"))
    return render(request, "setores/horarios/horario_setor_update.html", {'form': form})

########################## REFEIÇÃO ##########################
def admin_refeicao_list(request):
    refeicoes = Refeicao.objects.all()
    paginacao = Paginator(refeicoes, 5)

    page_number = request.GET.get("page")
    page_obj = paginacao.get_page(page_number)
    context = {'page_obj': page_obj}
    
    return render(request, "refeicoes/refeicao_list.html", context)

def refeicao_create(request):
    if (request.method == "POST"):
        form = RefeicaoForm(request.POST)
        if form.is_valid():
            form.save() # salva o form
            return HttpResponseRedirect(reverse("admin-refeicao-list"))
    form = RefeicaoForm()
    return render(request, "refeicoes/refeicao_create.html", {'form': form})

def refeicao_delete(request, id):
    refeicao = Refeicao.objects.get(id=id)
    if (request.method == "POST"):
        refeicao.delete()
        return HttpResponseRedirect(reverse("admin-refeicao-list"))
    return render(request, "refeicoes/refeicao_delete.html", {'refeicao': refeicao})

def refeicao_update(request, id):
    refeicao = get_object_or_404(Refeicao, id=id)
    form = RefeicaoForm(request.POST or None, instance=refeicao)
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin-refeicao-list"))
    return render(request, "refeicoes/refeicao_update.html", {'form': form})
