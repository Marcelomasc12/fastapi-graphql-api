from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import PostModel
from app.schemas import PostCreate, PostUpdate

router = APIRouter()

#DEfini os endpoints
@router.get("/health")
def health():
    return {
        "status": "ok",
        "message": "API funcionando"
    }


@router.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = PostModel(
        title=post.title,
        content=post.content
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.put("/posts/{post_id}")
def update_post(
    post_id: int,
    post: PostUpdate,
    db: Session = Depends(get_db)
):
    existing_post = db.query(PostModel).filter(PostModel.id == post_id).first()

    if not existing_post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    existing_post.title = post.title
    existing_post.content = post.content

    db.commit()
    db.refresh(existing_post)

    return existing_post


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    existing_post = db.query(PostModel).filter(PostModel.id == post_id).first()

    if not existing_post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    db.delete(existing_post)
    db.commit()

    return {
        "message": "Post deletado com sucesso"
    }