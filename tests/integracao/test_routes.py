from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_post():
    response = client.post(
        "/posts",
        json={
            "title": "Post Teste",
            "content": "Conteudo do post teste"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Post Teste"


def test_create_post_invalid_data():
    response = client.post(
        "/posts",
        json={
            "title": "ab",
            "content": "123"
        }
    )

    assert response.status_code == 422


def test_update_post_not_found():
    response = client.put(
        "/posts/99999",
        json={
            "title": "Post Atualizado",
            "content": "Conteudo atualizado"
        }
    )

    assert response.status_code == 404


def test_delete_post_not_found():
    response = client.delete("/posts/99999")

    assert response.status_code == 404