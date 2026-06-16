from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_e2e_create_post_rest_and_get_graphql():
    # 1. Cria um post pela API REST
    create_response = client.post(
        "/posts",
        json={
            "title": "Post E2E",
            "content": "Teste de fluxo completo usando REST, banco e GraphQL"
        }
    )

    assert create_response.status_code == 200

    created_post = create_response.json()

    assert created_post["title"] == "Post E2E"
    assert created_post["content"] == "Teste de fluxo completo usando REST, banco e GraphQL"
    assert "id" in created_post

    # 2. Consulta os posts pelo GraphQL
    query = """
    query {
      getPosts {
        id
        title
        content
      }
    }
    """

    graphql_response = client.post(
        "/graphql",
        json={"query": query}
    )

    assert graphql_response.status_code == 200

    posts = graphql_response.json()["data"]["getPosts"]

    # 3. Verifica se o post criado aparece na resposta do GraphQL
    assert any(
        post["id"] == created_post["id"]
        and post["title"] == "Post E2E"
        and post["content"] == "Teste de fluxo completo usando REST, banco e GraphQL"
        for post in posts
    )