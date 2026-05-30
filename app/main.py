from fastapi import FastAPI
from app.routes import router
from strawberry.fastapi import GraphQLRouter
from app.graphql_schema import schema

app = FastAPI(title="FastAPI GraphQL API")

app.include_router(router)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")