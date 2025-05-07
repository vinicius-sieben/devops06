# Usar a imagem base python 3.8 slim
FROM python:3.8-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do diretório atual (.) para o diretório de trabalho dentro do container (/app)
COPY . /app

# Instalar as dependências do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Comando para rodar o seu app (ajuste conforme necessário)
CMD ["python", "app.py"]
