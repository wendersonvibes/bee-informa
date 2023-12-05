from django.urls import path
from . import views

urlpatterns = [
    path("listar/divulgacoes", views.divulgacao_list, name="divulgacao-list"),
    path('criar/divulgacao', views.divulgacao_create, name="divulgacao-create"),
    path('deletar/divulgacao/<int:id>', views.divulgacao_delete, name="divulgacao-delete"),
    path('atualizar/divulgacao/<int:id>', views.divulgacao_update, name="divulgacao-update"),  
]
