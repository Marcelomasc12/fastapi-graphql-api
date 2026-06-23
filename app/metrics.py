from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

# ==========================
# Métricas de requisições
# ==========================

app_requests_total = Counter(
    "app_requests_total", "Total de requisições da aplicação", ["method", "path"]
)

# ==========================
# Contadores (histórico)
# ==========================

posts_criados_total = Counter("posts_criados_total", "Total de posts criados")

posts_atualizados_total = Counter(
    "posts_atualizados_total", "Total de posts atualizados"
)

posts_deletados_total = Counter("posts_deletados_total", "Total de posts deletados")

consultas_graphql_total = Counter(
    "consultas_graphql_total", "Total de consultas GraphQL"
)

business_operations_total = Counter(
    "business_operations_total",
    "Total de operações de negócio",
    ["operation"],
)

# ==========================
# Gauge (estado atual)
# ==========================

posts_ativos = Gauge("posts_ativos", "Quantidade atual de posts cadastrados")


def setup_metrics(app):
    @app.middleware("http")
    async def count_requests(request, call_next):
        response = await call_next(request)

        app_requests_total.labels(
            method=request.method,
            path=request.url.path,
        ).inc()

        return response

    @app.get("/metrics")
    def metrics():
        return Response(
            generate_latest(),
            media_type=CONTENT_TYPE_LATEST,
        )
