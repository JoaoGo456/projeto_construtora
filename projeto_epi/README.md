# 🛡️ Sistema de Gerenciamento de EPIs (projeto_epi)

Este projeto tem como objetivo desenvolver um sistema para controle e gestão de Equipamentos de Proteção Individual (EPIs) em uma construtora, utilizando o framework **Django** em Python.

---

## 🚀 Como Executar o Projeto

Existem duas maneiras principais de executar este projeto: de forma nativa (ambiente virtual) ou utilizando Docker (recomendado para consistência).

### 1. Execução Nativa (Ambiente de Desenvolvimento)

**Pré-requisitos:**
* Python 3.10+
* pip (gerenciador de pacotes Python)

1.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/macOS
    # .venv\Scripts\activate  # No Windows
    ```

2.  **Instale as Dependências:**
    Crie um arquivo `requirements.txt` (se ainda não existir) com todas as suas dependências (Django, etc.) e instale-as:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Realize as Migrações do Banco de Dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Crie um Superusuário (Opcional, para acesso ao Admin):**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Inicie o Servidor:**
    ```bash
    python manage.py runserver
    ```
    O sistema estará disponível em: `http://127.0.0.1:8000/`

---

### 2. Execução via Docker (Ambiente Consistente)

**Pré-requisitos:**
* Docker e Docker Compose instalados.

1.  **Construa a Imagem do Docker:**
    Este comando lê o `Dockerfile` e cria uma imagem Docker local.
    ```bash
    docker build -t projeto-epi:latest .
    ```

2.  **Execute o Container:**
    Este comando inicia um container a partir da imagem, mapeando a porta 8000 do container para a porta 8000 da sua máquina.
    ```bash
    docker run -p 8000:8000 projeto-epi:latest
    ```
    O sistema estará disponível em: `http://localhost:8000/`

---

## 📖 Funcionalidades Implementadas

* **CRUD de Colaboradores:** Completo com Listagem, Criação, Edição e Exclusão.
* **Django Admin:** Interface administrativa configurada para o modelo `Colaborador`.

## ⚙️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Banco de Dados:** SQLite (padrão)
* **Containerização:** Docker

---