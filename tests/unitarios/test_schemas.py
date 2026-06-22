import pytest
from pydantic import ValidationError

from app.schemas import PostCreate, PostUpdate


def test_post_create_valido():
    post = PostCreate(
        title="Meu post",
        content="Conteúdo válido do post",
    )

    assert post.title == "Meu post"
    assert post.content == "Conteúdo válido do post"


def test_post_create_titulo_muito_curto():
    with pytest.raises(ValidationError):
        PostCreate(
            title="Oi",
            content="Conteúdo válido do post",
        )


def test_post_create_conteudo_muito_curto():
    with pytest.raises(ValidationError):
        PostCreate(
            title="Meu post",
            content="abc",
        )


def test_post_update_valido():
    post = PostUpdate(
        title="Post atualizado",
        content="Conteúdo atualizado",
    )

    assert post.title == "Post atualizado"
    assert post.content == "Conteúdo atualizado"


def test_post_update_titulo_muito_curto():
    with pytest.raises(ValidationError):
        PostUpdate(
            title="Oi",
            content="Conteúdo atualizado",
        )


def test_post_update_conteudo_muito_curto():
    with pytest.raises(ValidationError):
        PostUpdate(
            title="Post atualizado",
            content="abc",
        )
