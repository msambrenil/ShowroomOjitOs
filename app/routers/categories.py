from fastapi import APIRouter, Depends
from sqlmodel import select
from app.models import Category
from app.database import get_session

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=list[Category])
def read_categories(session=Depends(get_session)):
    return session.exec(select(Category)).all()


@router.post("/", response_model=Category)
def create_category(category: Category, session=Depends(get_session)):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category
