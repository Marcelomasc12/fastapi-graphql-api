import strawberry

posts = []

@strawberry.type
class Post:
    title: str
    content: str


@strawberry.type
class Query:

    @strawberry.field
    def get_posts(self) -> list[Post]:
        return [Post(**post) for post in posts]


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_post(self, title: str, content: str) -> Post:

        post = {
            "title": title,
            "content": content
        }

        posts.append(post)

        return Post(**post)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)