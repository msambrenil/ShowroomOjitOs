from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.models import Sale, SaleItem
from app.database import get_session

router = APIRouter(prefix="/sales", tags=["sales"])


@router.get("/", response_model=list[Sale])
def read_sales(session=Depends(get_session)):
    return session.exec(select(Sale)).all()


@router.post("/", response_model=Sale)
def create_sale(sale: Sale, session=Depends(get_session)):
    session.add(sale)
    session.commit()
    session.refresh(sale)
    return sale


@router.get("/{sale_id}", response_model=Sale)
def get_sale(sale_id: int, session=Depends(get_session)):
    sale = session.get(Sale, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale
