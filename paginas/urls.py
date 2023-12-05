from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="inicio"),
    path('setores/',views.setores_view, name='setores'),
    path('divulgacoes/',views.divulgacoes_view, name='divulgacoes'),
    path('tela-admin/',views.tela_admin_view, name='tela-admin'),
]
