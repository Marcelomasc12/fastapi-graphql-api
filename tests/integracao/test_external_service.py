from unittest.mock import patch

from app.external_service import buscar_autor_externo


@patch("app.external_service.requests.get")
def test_buscar_autor_externo_com_mock(mock_get):
    mock_get.return_value.json.return_value = {"id": 1, "name": "Autor Teste"}

    mock_get.return_value.raise_for_status.return_value = None

    resultado = buscar_autor_externo()

    assert resultado["id"] == 1
    assert resultado["name"] == "Autor Teste"
