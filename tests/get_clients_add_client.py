import pytest
from fastapi.testclient import TestClient
from main import app


def test_get_clients(test_db):
    """Тест запроса на получение всех клиентов"""
    with TestClient(app) as client:
        response = client.get("/clients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json() == []


def test_add_client(test_db):
    """Тест создания клиента"""
    client_data = {
        "document": "7000 698522",
        "surname": "Сидоров",
        "firstname": "Петр",
        "patronymic": "Сергеевич",
        "birthday": "1980-05-15",
        "phone": "1234567890",
        "email": "petr@example.com",
    }
    with TestClient(app) as client:
        response = client.post("/clients/", json=client_data)
    assert response.status_code == 200
    assert "id" in response.json()

    """Проверка добавленного клиента"""
    with TestClient(app) as client:
        response = client.get(f"/clients/{response.json()['id']}")
    assert response.status_code == 200
    assert response.json() == {**client_data, "id": response.json()["id"]}


if __name__ == '__main__':
    pytest.main(['-v'])