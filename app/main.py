from typing import List
from fastapi import Depends, status, FastAPI
from sqlalchemy.orm import Session
from . import models
from . import schemas
from fastapi import APIRouter
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get('/getPost', response_model=List[schemas.CreatePost])
def test_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return post


@router.post('/createPost', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost])
def create_posts(post_create: schemas.CreatePost, db: Session = Depends(get_db)):
    new_post = models.Post(**post_create.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]

app.include_router(router)