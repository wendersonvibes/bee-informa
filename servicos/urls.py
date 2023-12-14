from django.urls import path
from . import views

urlpatterns = [
    # DIVULGAÇÕES
    path("listar/divulgacoes/admin", views.admin_divulgacao_list, name="admin-divulgacao-list"),
    path('detalhar/divulgacao/<int:id>', views.divulgacao_detail, name="divulgacao-detail"),  
    path("listar/divulgacoes", views.divulgacao_list, name="divulgacao-list"),
    path('criar/divulgacao', views.divulgacao_create, name="divulgacao-create"),
    path('deletar/divulgacao/<int:id>', views.divulgacao_delete, name="divulgacao-delete"),
    path('atualizar/divulgacao/<int:id>', views.divulgacao_update, name="divulgacao-update"),  

    # SETORES
    path("listar/setor/admin", views.admin_setor_list, name="admin-setor-list"),
    path('criar/setor', views.setor_create, name="setor-create"),
    path('deletar/setor/<int:id>', views.setor_delete, name="setor-delete"),
    path('atualizar/setor/<int:id>', views.setor_update, name="setor-update"),

    # HORÁRIOS DOS SETORES
    path('listar/horario/setor/admin', views.admin_horario_setor_list, name="admin-horario-setor-list"),
    path('criar/horario/setor', views.horario_setor_create, name="horario-setor-create"),  
    path('deletar/horario/setor/<int:id>', views.horario_setor_delete, name="horario-setor-delete"),
    path('atualizar/horario/setor/<int:id>', views.horario_setor_update, name="horario-setor-update"),

    # REFEIÇÕES
    path('listar/refeicao/admin', views.admin_refeicao_list, name="admin-refeicao-list"),
    path('criar/refeicao', views.refeicao_create, name="refeicao-create"), 
    path('deletar/refeicao/<int:id>', views.refeicao_delete, name="refeicao-delete"),
    path('atualizar/refeicao/<int:id>', views.refeicao_update, name="refeicao-update"),
]
