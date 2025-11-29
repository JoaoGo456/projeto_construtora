# app_gestao/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,    # Para listar (Read)
    CreateView,  # Para criar (Create)
    UpdateView,  # Para atualizar (Update)
    DeleteView   # Para excluir (Delete)
)
from django.utils import timezone 

# 🚨 IMPORTAÇÕES CONSOLIDADAS: Todos os modelos de .models
from .models import Colaborador, EPI, Emprestimo 


# ----------------------------------------------------
# VIEWS PARA COLABORADOR
# ----------------------------------------------------

# R - Read: Listar Colaboradores
class ColaboradorListView(ListView):
    """Exibe a lista de todos os colaboradores cadastrados."""
    model = Colaborador
    template_name = 'colaboradores/colaborador_list.html'
    context_object_name = 'colaboradores' 
    
# C - Create: Criar Novo Colaborador
class ColaboradorCreateView(CreateView):
    """Permite o cadastro de um novo colaborador."""
    model = Colaborador
    template_name = 'colaboradores/colaborador_form.html'
    fields = ['nome', 'matricula', 'cargo', 'ativo']
    
# U - Update: Atualizar Colaborador
class ColaboradorUpdateView(UpdateView):
    """Permite a edição dos dados de um colaborador existente."""
    model = Colaborador
    template_name = 'colaboradores/colaborador_form.html'
    fields = ['nome', 'matricula', 'cargo', 'ativo']
    
# D - Delete: Excluir Colaborador
class ColaboradorDeleteView(DeleteView):
    """Exibe um formulário de confirmação de exclusão e remove o colaborador."""
    model = Colaborador
    template_name = 'colaboradores/colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')


# ----------------------------------------------------
# VIEWS PARA EPI
# ----------------------------------------------------

# R - Read: Listar todos os EPIs
class EPIListView(ListView):
    model = EPI
    template_name = 'epis/epi_list.html'
    context_object_name = 'epis' 

# C - Create: Criar um novo EPI
class EPICreateView(CreateView):
    model = EPI
    template_name = 'epis/epi_form.html'
    fields = ['nome', 'ca', 'descricao', 'quantidade_estoque', 'ativo']

# U - Update: Atualizar um EPI existente
class EPIUpdateView(UpdateView):
    model = EPI
    template_name = 'epis/epi_form.html'
    fields = ['nome', 'ca', 'descricao', 'quantidade_estoque', 'ativo']

# D - Delete: Excluir um EPI
class EPIDeleteView(DeleteView):
    model = EPI
    template_name = 'epis/epi_confirm_delete.html'
    success_url = reverse_lazy('epi_list')


# ----------------------------------------------------
# VIEWS PARA EMPRÉSTIMO / DISTRIBUIÇÃO
# ----------------------------------------------------

# R - Read: Listar todos os Empréstimos
class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_list.html'
    context_object_name = 'emprestimos' 

# C - Create: Criar um novo Empréstimo
class EmprestimoCreateView(CreateView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_form.html'
    fields = ['colaborador', 'epi', 'quantidade', 'data_devolucao_prevista']

# U - Update: Atualizar um Empréstimo (Útil para registrar a devolução)
class EmprestimoUpdateView(UpdateView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_form.html'
    fields = [
        'colaborador', 'epi', 'quantidade', 
        'data_devolucao_prevista', 'data_devolucao_real'
    ]

# D - Delete: Excluir um Empréstimo
class EmprestimoDeleteView(DeleteView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_confirm_delete.html'
    success_url = reverse_lazy('emprestimo_list')