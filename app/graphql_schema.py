import strawberry

from app.database import SessionLocal
from app.models import PostModel
from app.metrics import consultas_graphql_total, posts_ativos, business_operations_total


@strawberry.type
class Post:
    id: int
    title: str
    content: str


@strawberry.type
class Query:

    @strawberry.field
    def get_posts(self) -> list[Post]:
        # Métrica específica do GraphQL
        consultas_graphql_total.inc()

        # Métrica de operação de negócio
        business_operations_total.labels(operation="graphql_query").inc()

        db = SessionLocal()

        try:
            posts = db.query(PostModel).all()

            posts_ativos.set(len(posts))

            return [
                Post(id=post.id, title=post.title, content=post.content)
                for post in posts
            ]

        finally:
            db.close()


schema = strawberry.Schema(query=Query)
