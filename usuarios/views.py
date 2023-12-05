from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('inicio'))
        else:
            return HttpResponse("Algo errado")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('inicio'))

# def dashboard_view(request):
#     if request.user.is_authenticated:
#         return render(request, 'tela-admin.html')