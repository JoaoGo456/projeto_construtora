import pytest # 1. Importe o pytest
from django.test import Client
from django.urls import reverse

def test_home_url():
    assert reverse('colaborador_list') == '/colaboradores/'

@pytest.mark.django_db # 2. Autorize o acesso ao banco de dados
def test_home_ok():
    client = Client()
    response = client.get(reverse('colaborador_list'))
    assert response.status_code == 200