from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http.response import HttpResponseRedirect

from .forms import DivulgacaoForm
from .models import Divulgacao, Imagem

def divulgacao_list(request):
    divulgacoes = Divulgacao.objects.all()
    context = {'divulgacoes': divulgacoes}
    return render(request, "divulgacoes.html", context)

def divulgacao_create(request):
    if (request.method == "POST"):
        form = DivulgacaoForm(request.POST, request.FILES)
        if form.is_valid():
            divulgacao = form.save() # salva o form
            imagens = request.FILES.getlist("imagem_da_divulgacao") # coloca as imagens numa lista

            if (imagens):
                for img in imagens: # cria os objetos em ImagemDivulgacao
                    Imagem.objects.create(
                        divulgacao=divulgacao, imagem = img # atributos da classe ImagemDivulgacao
                    )
            return HttpResponseRedirect(reverse("divulgacao-list"))
    
    else:
        form = DivulgacaoForm()
    return render(request, "divulgacoes/divulgacao_create.html", {'form': form})

def divulgacao_delete(request, id):
    divulgacao = Divulgacao.objects.get(id=id)
    if (request.method == "POST"):
        divulgacao.delete()
        return HttpResponseRedirect(reverse("inicio"))
    return render(request, "divulgacoes/divulgacao_delete.html", {'divulgacao': divulgacao})

def divulgacao_update(request, id):
    divulgacao = get_object_or_404(Divulgacao, id=id)
    form = DivulgacaoForm(request.POST or None, request.FILES or None, instance=divulgacao)
    if (request.method == "POST"):
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("inicio"))
    return render(request, "divulgacoes/divulgacao_update.html", {'form': form})