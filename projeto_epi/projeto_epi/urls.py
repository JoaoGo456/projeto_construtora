# projeto_epi/urls.py (Principal do projeto)

from django.contrib import admin
from django.urls import path, include
# 💡 Importação necessária para fazer o redirecionamento
from django.views.generic.base import RedirectView 

urlpatterns = [
    # 1. Rota Raiz (Redirecionamento): Redireciona a página inicial ('') para '/colaboradores/'
    path('', RedirectView.as_view(url='colaboradores/', permanent=True), name='index'), # 🚨 CORRIGIDO E ADICIONADA VÍRGULA
    
    path('colaboradores/', include('app_gestao.urls')),
    
    # 2. Rota Admin
    path('admin/', admin.site.urls),
    
    # 3. Inclusão das URLs da Aplicação
   
]