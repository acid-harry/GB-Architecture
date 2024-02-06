import pytest
from fastapi.testclient import TestClient
from main import app


def test_delete_client(test_db):
    """Тест удаления клиента"""
    client_data = {  # Создание клиента для удаления
        "document": "1234 567890",
        "surname": "Иванов",
        "firstname": "Петр",
        "patronymic": "Сергеевич",
        "birthday": "1980-05-15",
        "phone": "1234567890",
        "email": "petr@example.com",
    }
    with TestClient(app) as client:
        response = client.post("/clients/", json=client_data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    with TestClient(app) as client:  # Удаление клиента
        response = client.delete(f"/clients/{client_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Client deleted"}

    with TestClient(app) as client:  # Проверка, что клиента больше нет
        response = client.get(f"/clients/{client_id}")
    assert response.status_code == 404


def test_update_client(test_db):
    """Тест обновления клиента """
    client_data = {  # Создание клиента для обновления
        "document": "5678 901234",
        "surname": "Сидоров",
        "firstname": "Иван",
        "patronymic": "Алексеевич",
        "birthday": "1975-03-20",
        "phone": "9876543210",
        "email": "ivan@example.com",
    }
    with TestClient(app) as client:
        response = client.post("/clients/", json=client_data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    update_client_data = {  # Обновленные данные клиента
        "document": "9876 543210",
        "surname": "Новиков",
        "firstname": "Иван",
        "patronymic": "Александрович",
        "birthday": "1985-08-10",
        "phone": "9876543210",
        "email": "ivan@example.com",
    }
    with TestClient(app) as client:
        response = client.put(f"/clients/{client_id}", json=update_client_data)
    assert response.status_code == 200
    assert response.json() == {**update_client_data, "id": client_id}


if __name__ == '__main__':
    pytest.main(['-v'])