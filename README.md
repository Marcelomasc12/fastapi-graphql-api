# Desenvolvimento de uma API REST e GraphQL com FastAPI

Projeto desenvolvido para a disciplina **Teste e Qualidade de Software**, utilizando FastAPI para construção de uma API REST e GraphQL, PostgreSQL como banco de dados, Docker para conteinerização, Prometheus e Grafana para observabilidade, testes automatizados e pipeline CI/CD com GitHub Actions.

---

## 👨‍💻 Alunos

- Marcelo Negrão Mascarenhas
- Luisa Castro

**Professor:** Neuton Melo

**Disciplina:** Teste e Qualidade de Software

---

# 📚 Tecnologias Utilizadas

- FastAPI
- GraphQL (Strawberry GraphQL)
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Prometheus
- Grafana
- Pytest
- Black
- GitHub Actions

---

# 📂 Estrutura do Projeto

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI/CD
│
├── app/
│   ├── database.py             # Conexão com PostgreSQL
│   ├── external_service.py      # Serviço externo
│   ├── graphql_schema.py        # Schema GraphQL
│   ├── logging_config.py        # Configuração de logs
│   ├── main.py                  # Inicialização da aplicação
│   ├── metrics.py               # Métricas Prometheus
│   ├── models.py                # Modelos SQLAlchemy
│   ├── routes.py                # Endpoints REST
│   └── schemas.py               # Schemas Pydantic
│
├── observability/
│   └── prometheus.yml           # Configuração do Prometheus
│
├── tests/
│   ├── e2e/
│   ├── integracao/
│   ├── mutacao/
│   └── unitarios/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Funcionalidades

## API REST

- GET /health
- POST /posts
- PUT /posts/{id}
- DELETE /posts/{id}

## GraphQL

- Consulta de posts
- Resolvers GraphQL

## Observabilidade

- Endpoint `/metrics`
- Prometheus
- Dashboards Grafana

## Banco de Dados

- PostgreSQL
- SQLAlchemy ORM

## Testes

- Testes Unitários
- Testes de Integração
- Testes End-to-End (E2E)
- Testes de Mutação

## Qualidade

- Black (formatação)
- Cobertura mínima de 90%
- Pipeline CI/CD

---

# 🐳 Executando o Projeto

## Subir os containers

```bash
docker compose up -d --build
```

---

## Parar os containers

```bash
docker compose down
```

---

# 🧪 Executando os Testes

## Testes Unitários

```bash
docker compose exec api python -m pytest tests/unitarios -v
```

## Testes de Integração

```bash
docker compose exec api python -m pytest tests/integracao -v
```

## Testes E2E

```bash
docker compose exec api python -m pytest tests/e2e -v
```

## Testes de Mutação

```bash
docker compose exec api python -m pytest tests/mutacao -v -s
```

## Todos os Testes

```bash
docker compose exec api python -m pytest tests -v
```

---

# 📊 Cobertura de Testes

```bash
docker compose exec api python -m pytest tests --cov=app --cov-report=term-missing --cov-fail-under=90
```

---

# 🎨 Formatação do Código

## Verificar

```bash
docker compose exec api black --check app tests
```

## Formatar

```bash
docker compose exec api black app tests
```

---

# 📈 Observabilidade

Após iniciar o projeto:

Aplicação

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

GraphQL

```
http://localhost:8000/graphql
```

Métricas

```
http://localhost:8000/metrics
```

Prometheus

```
http://localhost:9090
```

Grafana

```
http://localhost:3000
```

---

# 📌 Pipeline CI/CD

A pipeline é executada automaticamente a cada Push e Pull Request para a branch principal.

Ela realiza:

- Checkout do projeto
- Build dos containers Docker
- Verificação da formatação com Black
- Execução dos testes automatizados
- Validação da cobertura mínima de 90%
- Encerramento dos containers

---

# 📊 Observabilidade

A aplicação exporta métricas utilizando o Prometheus Client.

Algumas métricas implementadas:

- Total de requisições
- Posts criados
- Posts atualizados
- Posts removidos
- Consultas GraphQL
- Quantidade de posts cadastrados
- Operações de negócio

Essas métricas são coletadas pelo Prometheus e apresentadas em dashboards no Grafana.

---

# 📝 Logs

A aplicação possui configuração de logging utilizando o módulo `logging` do Python.

Os logs podem ser visualizados com:

```bash
docker compose logs -f api
```

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina **Teste e Qualidade de Software**.