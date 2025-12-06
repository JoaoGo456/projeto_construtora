from django import forms
from .models import Emprestimo

class EmprestimoStatusUpdateForm(forms.ModelForm):
    """
    Formulário customizado para atualizar o status do empréstimo.
    Bloqueia a edição de campos-chave.
    """
    class Meta:
        model = Emprestimo
        # Inclua APENAS os campos que o usuário PODE alterar para esta ação
        fields = ['status', 'data_devolucao_real', 'observacao_devolucao']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 1. Adiciona os campos de leitura (bloqueados)
        # O self.instance contém o objeto Emprestimo sendo editado
        
        # Colaborador (Exibição apenas)
        self.fields['colaborador_nome'] = forms.CharField(
            label='Colaborador', 
            initial=self.instance.colaborador.nome, 
            required=False, 
            widget=forms.TextInput(attrs={'disabled': 'disabled'}) # ATRIBUTO DISABLED!
        )
        
        # EPI (Equipamento) (Exibição apenas)
        self.fields['epi_nome'] = forms.CharField(
            label='Equipamento', 
            initial=self.instance.epi.nome, 
            required=False, 
            widget=forms.TextInput(attrs={'disabled': 'disabled'}) # ATRIBUTO DISABLED!
        )
        
        # Data do Empréstimo (Exibição apenas)
        self.fields['data_emprestimo_display'] = forms.DateField(
            label='Data do Empréstimo', 
            initial=self.instance.data_emprestimo, 
            required=False, 
            widget=forms.DateInput(attrs={'disabled': 'disabled'}) # ATRIBUTO DISABLED!
        )

        # Data Prevista da Devolução (Exibição apenas)
        self.fields['data_devolucao_prevista_display'] = forms.DateField(
            label='Data Prevista', 
            initial=self.instance.data_devolucao_prevista, 
            required=False, 
            widget=forms.DateInput(attrs={'disabled': 'disabled'}) # ATRIBUTO DISABLED!
        )
        
        # Reposiciona e ordena os campos no formulário (opcional, mas recomendado)
        # Este é apenas um exemplo simplificado, você precisará adaptá-lo ao seu template
        field_order = [
            'colaborador_nome', 'epi_nome', 
            'data_emprestimo_display', 'data_devolucao_prevista_display',
            'status', 'data_devolucao_real', 'observacao_devolucao'
        ]
        self.order_fields(field_order)