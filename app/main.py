from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.database import Base, engine
from app.graphql_schema import schema
from app.models import PostModel
from app.routes import router
from app.logging_config import configure_logging
from app.metrics import setup_metrics

configure_logging()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI GraphQL API")

setup_metrics(app)

app.include_router(router)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
