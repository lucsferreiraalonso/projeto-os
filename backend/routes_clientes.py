from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Cliente

router = APIRouter()

@router.post("/clientes/")
def create_cliente(cliente: Cliente, session: Session = Depends(get_session)):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

@router.get("/clientes/")
def read_clientes(session: Session = Depends(get_session)):
    clientes = session.exec(select(Cliente)).all()
    return clientes