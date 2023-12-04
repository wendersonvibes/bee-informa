from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def setores_view(request):
    return render(request, 'setores.html')

# def divulgacoes_view(request):
#     return render(request, 'divulgacoes.html')
