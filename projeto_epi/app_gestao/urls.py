# app_gestao/urls.py

from django.urls import path
# 🚨 CORREÇÃO AQUI: Importar o módulo de views inteiro.
from . import views 
# Isso permite acessar todas as funções e classes como views.NomeDaView


urlpatterns = [
    # ------------------
    # URLs para COLABORADORES
    # ------------------
    # Mudança de: ColaboradorListView.as_view() para views.ColaboradorListView.as_view()
    path('', views.ColaboradorListView.as_view(), name='colaborador_list'), 
    path('novo/', views.ColaboradorCreateView.as_view(), name='colaborador_create'), 
    path('editar/<int:pk>/', views.ColaboradorUpdateView.as_view(), name='colaborador_update'), 
    path('excluir/<int:pk>/', views.ColaboradorDeleteView.as_view(), name='colaborador_delete'), 
    
    # ------------------
    # URLs para EPIs
    # ------------------
    path('epis/', views.EPIListView.as_view(), name='epi_list'), 
    path('epis/novo/', views.EPICreateView.as_view(), name='epi_create'), 
    path('epis/editar/<int:pk>/', views.EPIUpdateView.as_view(), name='epi_update'), 
    path('epis/excluir/<int:pk>/', views.EPIDeleteView.as_view(), name='epi_delete'), 
    
    # ------------------
    # URLs de RELATÓRIOS (Novas FBVs)
    # ------------------
    # Acesso direto à função: views.relatorio_emprestimos
    path('emprestimos/relatorio/', views.relatorio_emprestimos, name='emprestimo_relatorio'),
    
    # Acesso direto à função: views.atualizar_status_emprestimo
    path('emprestimos/atualizar_status/<int:pk>/', views.atualizar_status_emprestimo, name='atualizar_status_emprestimo'),
    
    # ------------------
    # URLs para EMPRÉSTIMOS
    # ------------------
    path('emprestimos/', views.EmprestimoListView.as_view(), name='emprestimo_list'), 
    path('emprestimos/novo/', views.EmprestimoCreateView.as_view(), name='emprestimo_create'), 
    path('emprestimos/editar/<int:pk>/', views.EmprestimoUpdateView.as_view(), name='emprestimo_update'), 
    path('emprestimos/excluir/<int:pk>/', views.EmprestimoDeleteView.as_view(), name='emprestimo_delete'),
]