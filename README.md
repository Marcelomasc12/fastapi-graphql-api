# FastAPI GraphQL API

Projeto desenvolvido para a disciplina de Teste e Qualidade de Software.

## Objetivo

Criar uma API utilizando FastAPI e GraphQL contendo:

- Endpoint de Health Check
- Queries GraphQL
- Mutations GraphQL
- Testes unitários com Pytest
- Pipeline CI com GitHub Actions

---

## Tecnologias

- Python 3.12
- FastAPI
- Strawberry GraphQL
- Pydantic
- Pytest
- Docker
- GitHub Actions

---

## Estrutura do Projeto

```text
fastapi-graphql-api/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   └── graphql_schema.py
│
├── tests/
│   ├── test_routes.py
│   └── test_graphql.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Endpoints

### Health Check

```http
GET /health
```

Resposta:

```json
{
  "status": "ok",
  "message": "API funcionando"
}
```

---

### GraphQL

```http
POST /graphql
```

Interface gráfica:

```text
http://127.0.0.1:8000/graphql
```

---

## Executando Localmente

### Criar ambiente virtual

```bash
python3 -m venv venv
```

### Ativar ambiente virtual

```bash
source venv/bin/activate
```

### Instalar dependências

```bash
python3 -m pip install -r requirements.txt
```

### Executar aplicação

```bash
uvicorn app.main:app --reload
```

---

## Executar Testes

```bash
pytest
```

Resultado esperado:

```text
3 passed
```

---

## Exemplo GraphQL

### Criar Post

```graphql
mutation {
  createPost(
    title: "Primeiro Post",
    content: "Conteudo Teste"
  ) {
    title
    content
  }
}
```

### Buscar Posts

```graphql
query {
  getPosts {
    title
    content
  }
}
```

---

## Pipeline CI

O projeto possui integração com GitHub Actions.

A cada push para a branch main:

- Instala dependências
- Executa testes unitários
- Valida o projeto automaticamente

---

## Autor

Marcelo Negrão Mascarenhas Filho e Luisa Castro

Engenharia de Software
