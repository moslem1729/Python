from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import oauth2_schema, get_current_user
from db import db_article
from db.database import get_db
from schemas import ArticleDisplay, ArticleBase, UserBase

router = APIRouter(
	prefix='/article',
	tags=['article']
)


# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db),
                   current_user: UserBase = Depends(get_current_user)):
	return db_article.create_article(db, request)


@router.get('/{id}')  # , response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
	return {
		"date": db_article.get_article(db, id),
		"current_user": current_user
	}
