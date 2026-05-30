from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_post():

    query = """
    mutation {
      createPost(
        title: "Primeiro Post",
        content: "Conteudo Teste"
      ) {
        title
        content
      }
    }
    """

    response = client.post(
        "/graphql",
        json={"query": query}
    )

    assert response.status_code == 200


def test_get_posts():

    query = """
    query {
      getPosts {
        title
        content
      }
    }
    """

    response = client.post(
        "/graphql",
        json={"query": query}
    )

    assert response.status_code == 200