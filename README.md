# FastAPI + GraphQL API

Projeto desenvolvido para a disciplina de Testes de Software, utilizando FastAPI, GraphQL, PostgreSQL, Docker e Pytest.

---

# Objetivo
# Aula 03
Validar o funcionamento da aplicação através de:

- Testes de Integração
- Teste E2E (End-to-End)
- Teste de Mutação
- Cobertura de testes

---

# Estrutura do Projeto

```
fastapi-graphql-api
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── .vscode
│
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── external_service.py
│   ├── graphql_schema.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── tests
│   │
│   ├── integracao
│   │   ├── __init__.py
│   │   ├── test_external_service.py
│   │   ├── test_graphql.py
│   │   └── test_routes.py
│   │
│   ├── e2e
│   │   ├── __init__.py
│   │   └── test_e2e_graphql.py
│   │
│   └── mutacao
│       ├── __init__.py
│       ├── relatorio_mutacao.md
│       └── test_mutacao_fluxo_completo.py
│
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

# Subir os Containers

```bash
docker compose up -d --build
```

---

# Parar os Containers

```bash
docker compose down
```

---

# Executar todos os testes

```bash
docker compose exec api python -m pytest tests -v
```

---

# Executar apenas os testes de Integração

```bash
docker compose exec api python -m pytest tests/integracao -v
```

---

# Executar apenas o teste E2E

```bash
docker compose exec api python -m pytest tests/e2e/test_e2e_graphql.py -v
```

---

# Executar apenas o teste de Mutação

```bash
docker compose exec api python -m pytest tests/mutacao/test_mutacao_fluxo_completo.py -v -s
```

O parâmetro `-s` permite visualizar o resultado do teste de mutação no terminal.

---

# Executar todos os testes com cobertura

```bash
docker compose exec api python -m pytest tests --cov=app --cov-report=term-missing --cov-fail-under=90 -v
```

Esse comando exibe:

- Quantidade de testes executados;
- Cobertura individual de cada arquivo da aplicação;
- Cobertura total do projeto;
- Falha caso a cobertura seja inferior a 90%.

---

# Atualizar Dependências

Após adicionar uma nova biblioteca ao `requirements.txt`, reconstruir os containers:

```bash
docker compose up -d --build
```

---

# Atualizar a Pipeline

Após concluir as alterações:

```bash
git add .
git commit -m "Aula 3 - Testes E2E e Mutação"
git push origin main
```

A pipeline do GitHub Actions será executada automaticamente.

---

# Testes Implementados

## Testes de Integração

- Rotas REST
- Consultas GraphQL
- Serviço externo (Mock)

---

## Teste E2E

Fluxo completo validado:

```
Criar Post (REST)
        ↓
Salvar no Banco
        ↓
Consultar pelo GraphQL
        ↓
Atualizar Post (REST)
        ↓
Consultar novamente pelo GraphQL
        ↓
Excluir Post (REST)
        ↓
Confirmar remoção pelo GraphQL
```

---

## Teste de Mutação

Foi inserido propositalmente o seguinte bug:

```python
posts = db.query(PostModel).all()
```

foi alterado para

```python
posts = []
```

Após inserir a mutação, o teste E2E é executado automaticamente.

Resultado esperado:

```
========== TESTE DE MUTAÇÃO ==========
Mutação aplicada: GraphQL retorna lista vazia.
Resultado do E2E: FAILED (esperado)
Conclusão: O E2E detectou o bug.
```

Isso demonstra que o teste E2E consegue identificar alterações que quebram o comportamento esperado da aplicação.

---

# Tecnologias Utilizadas

- Python 3.12
- FastAPI
- GraphQL (Strawberry)
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Pytest
- Pytest-Cov

---

# Autores

- Marcelo Negrão Mascarenhas
- Luisa Castro
