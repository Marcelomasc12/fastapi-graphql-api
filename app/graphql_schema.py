import strawberry

from app.database import SessionLocal
from app.models import PostModel


@strawberry.type
class Post:
    id: int
    title: str
    content: str


@strawberry.type
class Query:

    @strawberry.field
    def get_posts(self) -> list[Post]:
        db = SessionLocal()

        try:
            posts = db.query(PostModel).all()

            return [
                Post(
                    id=post.id,
                    title=post.title,
                    content=post.content
                )
                for post in posts
            ]
        finally:
            db.close()


schema = strawberry.Schema(query=Query)