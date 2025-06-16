from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.models import Product
from app.database import get_session

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[Product])
def read_products(session=Depends(get_session)):
    return session.exec(select(Product)).all()


@router.post("/", response_model=Product)
def create_product(product: Product, session=Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, session=Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
