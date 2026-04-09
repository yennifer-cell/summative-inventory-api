import pytest

import app as app_module


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    app_module.inventory[:] = [
        {
            "id": 1,
            "name": "Milk",
            "brand": "Brand A",
            "quantity": 4,
            "price": 2.5,
            "barcode": "111",
        },
        {
            "id": 2,
            "name": "Bread",
            "brand": "Brand B",
            "quantity": 7,
            "price": 1.8,
            "barcode": "222",
        },
    ]
    return app_module.app.test_client()


def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_create_inventory_item(client):
    payload = {"name": "Eggs", "brand": "Farm", "quantity": 12, "price": 4.2}
    response = client.post("/inventory", json=payload)
    assert response.status_code == 201
    assert response.get_json()["name"] == "Eggs"


def test_patch_inventory_item(client):
    response = client.patch("/inventory/1", json={"quantity": 10})
    assert response.status_code == 200
    assert response.get_json()["quantity"] == 10


def test_delete_inventory_item(client):
    response = client.delete("/inventory/2")
    assert response.status_code == 204


def test_barcode_lookup_route(client, monkeypatch):
    monkeypatch.setattr(
        app_module,
        "fetch_product_by_barcode",
        lambda barcode: {"name": "Mock Product", "barcode": barcode},
    )

    response = client.get("/external/barcode/12345")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Mock Product"
