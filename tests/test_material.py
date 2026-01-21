from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_material(client):
    payload = {
        "nome": "Cimento",
        "quantidade": 10,
        "precoUnitario": 50.0
    }
    response = client.post("/material/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["nome"] == "Cimento"
    assert data["quantidade"] == 10
    assert data["precoUnitario"] == 50.0

def test_get_all_material(client):
    response = client.get("/material/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_material_by_id(client):
    payload = {
        "nome": "Areia",
        "quantidade": 5,
        "precoUnitario": 30.0
    }
    create_response = client.post("/material/", json=payload)
    material_id = create_response.json()["id"]
    response = client.get(f"/material/{material_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == material_id
    assert data["nome"] == "Areia"
