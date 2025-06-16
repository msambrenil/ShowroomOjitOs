from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.models import Client
from app.database import get_session

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/", response_model=list[Client])
def read_clients(session=Depends(get_session)):
    return session.exec(select(Client)).all()


@router.post("/", response_model=Client)
def create_client(client: Client, session=Depends(get_session)):
    session.add(client)
    session.commit()
    session.refresh(client)
    return client


@router.get("/{client_id}", response_model=Client)
def get_client(client_id: int, session=Depends(get_session)):
    client = session.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
