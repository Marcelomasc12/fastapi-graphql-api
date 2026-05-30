# FastAPI GraphQL API

Projeto da disciplina de Teste e Qualidade de Software.

## Tecnologias

- FastAPI
- GraphQL (Strawberry)
- Pydantic
- Pytest
- Docker

## Endpoints

### Health Check

GET /health

### GraphQL

POST /graphql

## Executar

pip install -r requirements.txt

uvicorn app.main:app --reload