import pytest
from starlette.testclient import TestClient
from web_app.main import app

@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):
    response = client.get("/health_check/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
