from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.routes import router
from app.graphql_schema import schema

from app.database import engine
from app.models import Base

# Cria as tabelas do banco automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI GraphQL API")

# Rotas REST
app.include_router(router)

# Rotas GraphQL
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")