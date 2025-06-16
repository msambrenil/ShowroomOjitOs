from fastapi import APIRouter, Depends
from sqlmodel import select
from app.models import Tag
from app.database import get_session

router = APIRouter(prefix="/tags", tags=["tags"])

@router.get("/", response_model=list[Tag])
def read_tags(session=Depends(get_session)):
    return session.exec(select(Tag)).all()

@router.post("/", response_model=Tag)
def create_tag(tag: Tag, session=Depends(get_session)):
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag
