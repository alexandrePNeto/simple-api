# Use a imagem Python 3.13 Alpine como base
FROM python:3.13-alpine

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências de sistema necessárias para compilar pacotes Python (opcional, mas recomendado no Alpine)
# Se o seu projeto for simples, pode remover a linha abaixo
RUN apk add --no-cache gcc musl-dev linux-headers

# Cria um usuário não-root para segurança (similar ao usuário 'node' na sua base)
RUN adduser -D simple-api
RUN chown -R simple-api:simple-api /app

# Copie o arquivo de dependências da raiz para o container
# Nota: O contexto do build deve ser a raiz do projeto
COPY --chown=simple-api:simple-api requirements.txt ./

USER simple-api

# Instala as dependências do projeto
RUN pip install --no-cache-dir --user -r requirements.txt

# Copie o resto do código (da pasta /app da sua máquina) para o container
COPY --chown=simple-api:simple-api ./app .

# Exponha a porta que o seu app utiliza (exemplo: 5687
EXPOSE 5687

# Comando para iniciar a aplicação
# Substitua 'main:app' pelo seu arquivo de entrada
CMD ["python", "main.py"]