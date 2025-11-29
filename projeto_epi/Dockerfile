# Dockerfile

# 1. IMAGEM BASE: Usa uma imagem oficial do Python 3.11.x (Slim é mais leve)
FROM python:3.11-slim

# 2. VARIÁVEIS DE AMBIENTE: Configura variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. DIRETÓRIO DE TRABALHO: Define o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# 4. DEPENDÊNCIAS DO SISTEMA (OPCIONAL, mas útil para certas bibliotecas)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#    postgresql-client \
#    && rm -rf /var/lib/apt/lists/*

# 5. COPIA ARQUIVOS: Copia o arquivo de requisitos e instala as dependências
# Recomenda-se copiar apenas o requirements.txt primeiro para cache eficiente
COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. COPIA O PROJETO: Copia o restante do código da aplicação
COPY . /usr/src/app/

# 7. EXPOSIÇÃO DA PORTA: A porta que o servidor Django Gunicorn/Runserver irá escutar
EXPOSE 8000

# 8. COMANDO DE INICIALIZAÇÃO: Define o comando para iniciar o servidor Django
# Se você usar o 'runserver' (apenas para dev/teste):
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Se você usar Gunicorn (recomendado para produção):
# CMD ["gunicorn", "projeto_epi.wsgi:application", "--bind", "0.0.0.0:8000"]