from sqlmodel import SQLModel, create_engine, Session

# O arquivo do banco ficará na pasta 'data' que mapeamos no Docker
sqlite_file_name = "/app/data/banco_os.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread=False é necessário para o FastAPI rodar com SQLite
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    # Cria o arquivo do banco e as tabelas se não existirem
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session