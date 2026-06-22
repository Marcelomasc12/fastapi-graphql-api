from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_e2e_crud_post_rest_graphql():

    # 1. Criar post (REST)
    # ============================
    create_response = client.post(
        "/posts",
        json={
            "title": "Post E2E",
            "content": "Teste de fluxo completo usando REST, banco e GraphQL",
        },
    )

    assert create_response.status_code == 200

    created_post = create_response.json()
    post_id = created_post["id"]

    assert created_post["title"] == "Post E2E"
    assert (
        created_post["content"]
        == "Teste de fluxo completo usando REST, banco e GraphQL"
    )

    # 2. Consultar no GraphQL
    # ============================
    query = """
    query {
      getPosts {
        id
        title
        content
      }
    }
    """

    graphql_response = client.post("/graphql", json={"query": query})

    assert graphql_response.status_code == 200

    posts = graphql_response.json()["data"]["getPosts"]

    assert any(
        post["id"] == post_id
        and post["title"] == "Post E2E"
        and post["content"] == "Teste de fluxo completo usando REST, banco e GraphQL"
        for post in posts
    )

    # 3. Atualizar post (REST)
    # ============================
    update_response = client.put(
        f"/posts/{post_id}",
        json={"title": "Post Atualizado", "content": "Conteúdo atualizado"},
    )

    assert update_response.status_code == 200

    # 4. Consultar novamente no GraphQL
    # ============================
    graphql_response = client.post("/graphql", json={"query": query})

    posts = graphql_response.json()["data"]["getPosts"]

    assert any(
        post["id"] == post_id
        and post["title"] == "Post Atualizado"
        and post["content"] == "Conteúdo atualizado"
        for post in posts
    )

    # 5. Deletar post (REST)
    # ============================
    delete_response = client.delete(f"/posts/{post_id}")

    assert delete_response.status_code == 200

    # 6. Confirmar remoção no GraphQL
    # ============================
    graphql_response = client.post("/graphql", json={"query": query})

    posts = graphql_response.json()["data"]["getPosts"]

    assert not any(post["id"] == post_id for post in posts)
