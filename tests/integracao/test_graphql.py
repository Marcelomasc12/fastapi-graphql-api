from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_posts_graphql():
    query = """
    query {
      getPosts {
        id
        title
        content
      }
    }
    """

    response = client.post("/graphql", json={"query": query})

    assert response.status_code == 200
    assert "data" in response.json()
    assert "getPosts" in response.json()["data"]
