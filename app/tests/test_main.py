from fastapi.testclient import TestClient

from .conftest import settings


def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Test App"}
    assert response.json() == {"msg": settings.app_name}
