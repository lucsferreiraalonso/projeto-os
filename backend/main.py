from fastapi import FastAPI
from database import create_db_and_tables

# Inicializa o FastAPI
app = FastAPI(
    title="API - Sistema de Ordem de Serviço",
    description="Backend do Sistema para gestão de OS",
    version="1.0.0"
)

# Evento que roda assim que o servidor liga (para criar o banco de dados)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Rota de teste (Hello World)
@app.get("/")
def read_root():
    return {
        "status": "sucesso",
        "mensagem": "API do Sistema de OS rodando perfeitamente dentro do Docker!",
        "banco_de_dados": "SQLite configurado."
    }