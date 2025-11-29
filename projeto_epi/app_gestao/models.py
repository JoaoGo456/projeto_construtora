# app_gestao/models.py (ou o nome da sua app)

from django.db import models
from django.urls import reverse # 👈 Importação necessária
from django.utils import timezone # Para usar a data/hora atual

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    cargo = models.CharField(max_length=100)
    # Adicionamos um campo 'ativo' que é uma boa prática
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

    # 👈 Método adicionado para o funcionamento correto das CBVs de criação/edição
    def get_absolute_url(self):
        # O nome 'colaborador_list' deve ser o nome (name) da URL da lista de colaboradores
        return reverse('colaborador_list') 

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

        # app_gestao/models.py (Adicionar abaixo da classe Colaborador)


class EPI(models.Model):
    # Campos básicos do EPI
    nome = models.CharField(max_length=150, verbose_name="Nome do EPI")
    ca = models.CharField(max_length=20, unique=True, verbose_name="Certificado de Aprovação (CA)")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição Detalhada")
    quantidade_estoque = models.IntegerField(default=0, verbose_name="Qtd. em Estoque")
    
    # Campo para indicar se o EPI está ativo (em uso pela empresa)
    ativo = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.nome} (CA: {self.ca})"

    def get_absolute_url(self):
        # Redireciona para a lista de EPIs após sucesso
        return reverse('epi_list')

    class Meta:
        verbose_name = "EPI"
        verbose_name_plural = "EPIs"

        # app_gestao/models.py (Adicionar abaixo da classe EPI)

# ... (Definições das classes Colaborador e EPI) ...

class Emprestimo(models.Model):
    colaborador = models.ForeignKey(
        Colaborador, 
        on_delete=models.PROTECT, # Protege o colaborador de ser deletado se tiver empréstimos
        verbose_name="Colaborador"
    )
    epi = models.ForeignKey(
        EPI, 
        on_delete=models.PROTECT, 
        verbose_name="EPI"
    )
    quantidade = models.IntegerField(verbose_name="Quantidade Emprestada")
    
    # Rastreamento de datas
    data_emprestimo = models.DateTimeField(default=timezone.now, verbose_name="Data do Empréstimo")
    data_devolucao_prevista = models.DateField(
        null=True, blank=True, 
        verbose_name="Devolução Prevista"
    )
    data_devolucao_real = models.DateTimeField(
        null=True, blank=True, 
        verbose_name="Data de Devolução Real"
    )

    @property
    def devolvido(self):
        """Propriedade para verificar se o EPI foi devolvido."""
        return self.data_devolucao_real is not None

    def __str__(self):
        return f"{self.epi.nome} para {self.colaborador.nome} em {self.data_emprestimo.strftime('%d/%m/%Y')}"

    def get_absolute_url(self):
        return reverse('emprestimo_list')

    class Meta:
        verbose_name = "Empréstimo de EPI"
        verbose_name_plural = "Empréstimos de EPIs"
        # Garante que os empréstimos mais recentes apareçam primeiro
        ordering = ['-data_emprestimo']