from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def setores_view(request):
    return render(request, 'setores.html')

<<<<<<< Updated upstream
# def divulgacoes_view(request):
#     return render(request, 'divulgacoes.html')
=======
def divulgacoes_view(request):
    return render(request, 'divulgacoes.html')

def tela_admin_view(request):
    return render(request, 'tela-admin.html')
>>>>>>> Stashed changes
