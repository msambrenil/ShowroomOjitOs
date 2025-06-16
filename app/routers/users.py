from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.models import User
from app.database import get_session

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
def read_users(session=Depends(get_session)):
    return session.exec(select(User)).all()


@router.post("/", response_model=User)
def create_user(user: User, session=Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.post("/login")
def login(user: User, session=Depends(get_session)):
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Logged in"}
