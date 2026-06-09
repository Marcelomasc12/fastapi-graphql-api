# FastAPI GraphQL API

Projeto desenvolvido para a disciplina de Teste e Qualidade de Software.

## Descrição

Esta aplicação implementa uma API utilizando FastAPI, PostgreSQL, Docker e GraphQL.

O projeto possui:

* API REST para gerenciamento de posts
* API GraphQL para consultas
* Banco de dados PostgreSQL
* Testes automatizados com Pytest
* Mock de serviço externo
* Pipeline CI com GitHub Actions
* Quality Gate com cobertura mínima de 90% dos resolvers GraphQL

---

# Tecnologias Utilizadas

* Python 3.12
* FastAPI
* Strawberry GraphQL
* SQLAlchemy
* PostgreSQL
* Docker
* Docker Compose
* Pytest
* Pytest-Cov
* GitHub Actions

---

# Estrutura do Projeto

```text
fastapi-graphql-api/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── database.py
│   ├── external_service.py
│   ├── graphql_schema.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── tests/
│   ├── test_external_service.py
│   ├── test_graphql.py
│   └── test_routes.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Como Executar o Projeto

## Construir e iniciar os containers

```bash
docker compose up --build
```

Utilize quando:

* Executar o projeto pela primeira vez
* Alterar o Dockerfile
* Alterar dependências do requirements.txt
* Alterar o docker-compose.yml

---

## Iniciar containers já criados

```bash
docker compose up
```

Utilize quando os containers já existem e nenhuma configuração foi alterada.

---

## Executar em segundo plano

```bash
docker compose up -d
```

Mantém a aplicação rodando sem ocupar o terminal.

---

## Encerrar a aplicação

```bash
docker compose down
```

Este comando:

* Para os containers
* Remove os containers
* Remove a rede criada pelo Docker Compose

Os dados do PostgreSQL permanecem salvos porque estão armazenados no volume:

```text
postgres_data
```

---

## Remover containers e apagar os dados do banco

```bash
docker compose down -v
```

Atenção:

Esse comando remove os volumes e apaga todos os dados armazenados no PostgreSQL.

---

# Endpoints Disponíveis

## Swagger

Interface para testar os endpoints REST.

```text
http://localhost:8000/docs
```

---

## GraphQL Playground

Interface para executar queries GraphQL.

```text
http://localhost:8000/graphql
```

---

# Endpoints REST

## Verificar saúde da API

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

## Criar Post

```http
POST /posts
```

Exemplo:

```json
{
  "title": "Aprendendo FastAPI",
  "content": "Meu primeiro post salvo no PostgreSQL."
}
```

---

## Atualizar Post

```http
PUT /posts/{id}
```

Exemplo:

```json
{
  "title": "Título Atualizado",
  "content": "Conteúdo atualizado"
}
```

---

## Excluir Post

```http
DELETE /posts/{id}
```

---

# Consulta GraphQL

Exemplo:

```graphql
query {
  getPosts {
    id
    title
    content
  }
}
```

---

# Executando os Testes

## Executar todos os testes

```bash
docker compose exec api pytest -v
```

Utilizamos o comando acima porque os testes devem rodar dentro do mesmo ambiente da aplicação (container da API).

---

## Executar cobertura dos resolvers GraphQL

```bash
docker compose exec api pytest --cov=app.graphql_schema --cov-report=term-missing
```

---

# Quality Gate

O projeto possui um Quality Gate configurado para os resolvers GraphQL.

Cobertura mínima exigida:

```text
90%
```

Caso a cobertura fique abaixo de 90%, a execução falha.

---

# Pipeline CI

Arquivo:

```text
.github/workflows/ci.yml
```

A pipeline executa automaticamente:

1. Checkout do código
2. Build dos containers
3. Inicialização da aplicação
4. Execução dos testes
5. Validação da cobertura mínima dos resolvers GraphQL
6. Encerramento dos containers

A pipeline é executada em:

* Push para a branch main
* Pull Request para a branch main

---

# Testes Implementados

## REST

* Health Check
* Criação de post
* Validação de dados inválidos (422)
* Atualização de post inexistente (404)
* Exclusão de post inexistente (404)

## GraphQL

* Consulta de posts através do resolver getPosts

## Serviço Externo

* Mock de API externa utilizando monkeypatch

---

# Autores

Marcelo Negrão Mascarenhas Filho

Luisa Castro Santos

Engenharia de Software

Disciplina: Teste e Qualidade de Software

