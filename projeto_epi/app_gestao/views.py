# app_gestao/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,      # Para listar (Read)
    CreateView,    # Para criar (Create)
    UpdateView,    # Para atualizar (Update)
    DeleteView     # Para excluir (Delete)
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils import timezone 
from django.db.models import Q

from .forms import EmprestimoStatusUpdateForm # Você precisará criar este ModelForm

# 🚨 IMPORTAÇÕES CONSOLIDADAS: Todos os modelos de .models
from .models import Colaborador, EPI, Emprestimo 
# Importação necessária para o form customizado (crie este arquivo!)
# from .forms import EmprestimoCreateForm 

# ----------------------------------------------------
# VIEWS PARA COLABORADOR
# ----------------------------------------------------

# R - Read: Listar Colaboradores
class ColaboradorListView(ListView):
    """Exibe a lista de todos os colaboradores cadastrados."""
    model = Colaborador
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/colaboradores/colaborador_list.html'
    context_object_name = 'colaboradores' 
    
# C - Create: Criar Novo Colaborador
class ColaboradorCreateView(SuccessMessageMixin, CreateView):
    """Permite o cadastro de um novo colaborador, exibe mensagem e permanece na tela."""
    model = Colaborador
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/colaboradores/colaborador_form.html'
    fields = ['nome', 'matricula', 'cargo', 'ativo']
    success_message = "Colaborador **%(nome)s** cadastrado com sucesso!"
    
    # REQUISITO: Permanecer na tela após o sucesso
    def get_success_url(self):
        return reverse_lazy('colaborador_create') # Assumindo que a URL de criação chama 'colaborador_create'
    
# U - Update: Atualizar Colaborador
class ColaboradorUpdateView(SuccessMessageMixin, UpdateView):
    """Permite a edição dos dados de um colaborador existente."""
    model = Colaborador
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/colaboradores/colaborador_form.html'
    fields = ['nome', 'matricula', 'cargo', 'ativo']
    success_message = "Colaborador **%(nome)s** atualizado com sucesso!"
    
    # Após a edição, redireciona para a lista
    def get_success_url(self):
        return reverse_lazy('colaborador_list')
    
# D - Delete: Excluir Colaborador
class ColaboradorDeleteView(DeleteView):
    """Exibe um formulário de confirmação de exclusão e remove o colaborador."""
    model = Colaborador
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/colaboradores/colaborador_confirm_delete.html'
    success_url = reverse_lazy('colaborador_list')

    # Adiciona a mensagem de sucesso após a exclusão
    def form_valid(self, form):
        messages.success(self.request, f"Colaborador **{self.object.nome}** excluído com sucesso!")
        return super().form_valid(form)


# ----------------------------------------------------
# VIEWS PARA EPI
# ----------------------------------------------------

# R - Read: Listar todos os EPIs
class EPIListView(ListView):
    model = EPI
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/epi/epi_list.html' 
    context_object_name = 'epis' 

# C - Create: Criar um novo EPI
class EPICreateView(SuccessMessageMixin, CreateView):
    model = EPI
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/epi/epi_form.html'
    fields = ['nome', 'ca', 'descricao', 'quantidade_estoque', 'ativo']
    success_message = "EPI **%(nome)s** cadastrado com sucesso!"

    # REQUISITO: Permanecer na tela após o sucesso
    def get_success_url(self):
        return reverse_lazy('epi_create') # Assumindo que a URL de criação chama 'epi_create'

# U - Update: Atualizar um EPI existente
class EPIUpdateView(SuccessMessageMixin, UpdateView):
    model = EPI
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/epi/epi_form.html'
    fields = ['nome', 'ca', 'descricao', 'quantidade_estoque', 'ativo']
    success_message = "EPI **%(nome)s** atualizado com sucesso!"

    def get_success_url(self):
        return reverse_lazy('epi_list')

# D - Delete: Excluir um EPI
class EPIDeleteView(DeleteView):
    model = EPI
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/epi/epi_confirm_delete.html'
    success_url = reverse_lazy('epi_list')

    def form_valid(self, form):
        messages.success(self.request, f"EPI **{self.object.nome}** excluído com sucesso!")
        return super().form_valid(form)


# ----------------------------------------------------
# VIEWS PARA EMPRÉSTIMO / DISTRIBUIÇÃO
# ----------------------------------------------------

# R - Read: Listar todos os Empréstimos
class EmprestimoListView(ListView):
    model = Emprestimo
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/emprestimos/emprestimo_list.html' 
    context_object_name = 'emprestimos' 

# C - Create: Criar um novo Empréstimo
class EmprestimoCreateView(SuccessMessageMixin, CreateView):
    model = Emprestimo
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/emprestimos/emprestimo_form.html'
    # Use fields provisoriamente. Idealmente use form_class = EmprestimoCreateForm
    fields = ['colaborador', 'epi', 'quantidade', 'data_devolucao_prevista'] 
    success_message = "Empréstimo registrado com sucesso!"

    def get_success_url(self):
        # Redireciona para a lista após o cadastro de Empréstimo
        return reverse_lazy('emprestimo_list') 

# U - Update: Atualizar um Empréstimo (Útil para registrar a devolução)
class EmprestimoUpdateView(SuccessMessageMixin, UpdateView):
    model = Emprestimo
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/emprestimos/emprestimo_form.html' # Sugestão de template específico para update/devolução
    fields = [
        # Manter estes no 'fields' mas desabilitá-los/ocultá-los no template
        'colaborador', 'epi', 'quantidade', 'data_devolucao_prevista', 
        
        # Campos que o usuário deve poder alterar
        'status', 'data_devolucao_real', 'observacao_devolucao' 
    ]
    success_message = "Status do Empréstimo atualizado!"

    def get_success_url(self):
        return reverse_lazy('emprestimo_list')
    
    # Adicione a lógica de atualização de estoque/data de devolução
    def form_valid(self, form):
        # Implementar lógica de atualização de estoque e data real de devolução aqui
        return super().form_valid(form)


# D - Delete: Excluir um Empréstimo
class EmprestimoDeleteView(DeleteView):
    model = Emprestimo
    # CORRIGIDO o namespace do template
    template_name = 'app_gestao/emprestimos/emprestimo_confirm_delete.html'
    success_url = reverse_lazy('emprestimo_list')

    def form_valid(self, form):
        messages.success(self.request, "Empréstimo excluído com sucesso!")
        return super().form_valid(form)

def relatorio_emprestimos(request):
    """
    Exibe a tela de relatórios e aplica o filtro AND 
    baseado em colaborador, EPI e status.
    """
    
    # 1. Inicia o QuerySet com todos os objetos
    emprestimos = Emprestimo.objects.all()

    # 2. Obtém os parâmetros de filtro da URL (GET)
    colaborador_nome = request.GET.get('colaborador_filtro', '').strip()
    epi_nome = request.GET.get('epi_filtro', '').strip()
    status = request.GET.get('status_filtro', '').strip()

    # 3. Aplica o Filtro AND (Condição: se o parâmetro foi preenchido)
    
    # Filtro pelo nome do Colaborador (pesquisa parcial, case-insensitive)
    if colaborador_nome:
        # Assumindo que o campo 'nome' está no modelo Colaborador (ForeignKey)
        emprestimos = emprestimos.filter(colaborador__nome__icontains=colaborador_nome)

    # Filtro pelo nome do EPI (equipamento) (pesquisa parcial, case-insensitive)
    if epi_nome:
        # Assumindo que o campo 'nome' está no modelo EPI (ForeignKey)
        emprestimos = emprestimos.filter(epi__nome__icontains=epi_nome)

    # Filtro pelo Status (correspondência exata)
    if status:
        emprestimos = emprestimos.filter(status=status)
        
    # 4. Ordena os resultados para melhor visualização (Ex: Data de Empréstimo mais recente)
    emprestimos = emprestimos.order_by('-data_emprestimo')

    return render(request, 'app_gestao/emprestimos/emprestimo_relatorio.html', {
        'emprestimos': emprestimos,
        # Passa os filtros atuais de volta para pré-preencher o formulário
        'colaborador_filtro': colaborador_nome,
        'epi_filtro': epi_nome,
        'status_filtro': status,
    })

def atualizar_status_emprestimo(request, pk):
    """
    Permite atualizar o status do empréstimo (e data de devolução), 
    bloqueando a edição de campos primários.
    """
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    
    # 1. Cria um ModelForm com os dados da instância
    if request.method == 'POST':
        # O formulário customizado só terá os campos: status, data_devolucao_real, observacao_devolucao
        form = EmprestimoStatusUpdateForm(request.POST, instance=emprestimo)
        
        if form.is_valid():
            # A lógica de bloqueio está no ModelForm (Opção 2)
            form.save() 
            messages.success(request, f"Status do Empréstimo #{pk} atualizado com sucesso!")
            return redirect('emprestimo_relatorio') # Redireciona para o relatório
            
    else:
        # GET: Carrega o formulário com a instância
        form = EmprestimoStatusUpdateForm(instance=emprestimo) 

    # Renderiza um template específico para a edição de status
    return render(request, 'app_gestao/emprestimos/emprestimo_status_update.html', {
        'form': form,
        'emprestimo': emprestimo
    })
# --- FIM DAS VIEWS ---