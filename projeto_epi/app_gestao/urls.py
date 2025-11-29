# app_gestao/urls.py

from django.urls import path
from .views import (
    ColaboradorListView,
    ColaboradorCreateView,
    ColaboradorUpdateView,
    ColaboradorDeleteView,
    # As importações de views devem ser mantidas juntas
    EPIListView,
    EPICreateView,
    EPIUpdateView,
    EPIDeleteView,
    EmprestimoListView,
    EmprestimoCreateView,
    EmprestimoUpdateView,
    EmprestimoDeleteView
)

urlpatterns = [
    # ------------------
    # URLs para COLABORADORES
    # ------------------
    # URL completa: /colaboradores/
    path('', ColaboradorListView.as_view(), name='colaborador_list'), # <-- Vírgula OK
    
    # URL completa: /colaboradores/novo/
    path('novo/', ColaboradorCreateView.as_view(), name='colaborador_create'), # <-- Vírgula OK
    
    # URL completa: /colaboradores/editar/1/
    path('editar/<int:pk>/', ColaboradorUpdateView.as_view(), name='colaborador_update'), # <-- Vírgula OK
    
    # URL completa: /colaboradores/excluir/1/
    path('excluir/<int:pk>/', ColaboradorDeleteView.as_view(), name='colaborador_delete'), # <-- Vírgula ESSENCIAL
    
    # ------------------
    # URLs para EPIs
    # ------------------
    # URL completa: /colaboradores/epis/
    path('epis/', EPIListView.as_view(), name='epi_list'), # <-- Vírgula ESSENCIAL
    path('epis/novo/', EPICreateView.as_view(), name='epi_create'), # <-- Vírgula OK
    path('epis/editar/<int:pk>/', EPIUpdateView.as_view(), name='epi_update'), # <-- Vírgula OK
    path('epis/excluir/<int:pk>/', EPIDeleteView.as_view(), name='epi_delete'), # <-- Vírgula ESSENCIAL

    # ------------------
    # URLs para EMPRÉSTIMOS
    # ------------------
    # URL completa: /colaboradores/emprestimos/
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimo_list'), # <-- Vírgula ESSENCIAL
    path('emprestimos/novo/', EmprestimoCreateView.as_view(), name='emprestimo_create'), # <-- Vírgula OK
    path('emprestimos/editar/<int:pk>/', EmprestimoUpdateView.as_view(), name='emprestimo_update'), # <-- Vírgula OK
    path('emprestimos/excluir/<int:pk>/', EmprestimoDeleteView.as_view(), name='emprestimo_delete'), # <-- Última linha sem vírgula, pois é o último item.
]