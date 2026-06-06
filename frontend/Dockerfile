# Usa uma imagem oficial e super leve do Node.js
FROM node:20-alpine

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência primeiro (otimiza o cache do Docker)
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia o resto do código do frontend
COPY . .

# Expõe a porta que o Vite usa
EXPOSE 5173

# O comando de inicialização já está no docker-compose.yml