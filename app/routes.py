from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import PostModel
from app.schemas import PostCreate, PostUpdate
from app.metrics import (
    posts_criados_total,
    posts_atualizados_total,
    posts_deletados_total,
    posts_ativos,
    business_operations_total,
)

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok", "message": "API funcionando"}


@router.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = PostModel(title=post.title, content=post.content)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    posts_criados_total.inc()
    business_operations_total.labels(operation="create_post").inc()
    posts_ativos.set(db.query(PostModel).count())

    return new_post


@router.put("/posts/{post_id}")
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    existing_post = db.query(PostModel).filter(PostModel.id == post_id).first()

    if not existing_post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    existing_post.title = post.title
    existing_post.content = post.content

    db.commit()
    db.refresh(existing_post)

    posts_atualizados_total.inc()
    business_operations_total.labels(operation="update_post").inc()
    posts_ativos.set(db.query(PostModel).count())

    return existing_post


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    existing_post = db.query(PostModel).filter(PostModel.id == post_id).first()

    if not existing_post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    db.delete(existing_post)
    db.commit()

    posts_deletados_total.inc()
    business_operations_total.labels(operation="delete_post").inc()
    posts_ativos.set(db.query(PostModel).count())

    return {"message": "Post deletado com sucesso"}
