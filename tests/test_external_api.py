import external_api


class DummyResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def test_fetch_product_by_barcode(monkeypatch):
    payload = {
        "status": 1,
        "product": {
            "product_name": "Orange Juice",
            "brands": "Fresh Co",
            "ingredients_text": "orange",
            "code": "123",
        },
    }

    monkeypatch.setattr(external_api.requests, "get", lambda *args, **kwargs: DummyResponse(payload))

    product = external_api.fetch_product_by_barcode("123")
    assert product["name"] == "Orange Juice"
    assert product["barcode"] == "123"


def test_fetch_product_by_name(monkeypatch):
    payload = {
        "products": [
            {
                "product_name": "Chocolate",
                "brands": "Sweet",
                "ingredients_text": "cocoa",
                "code": "999",
            }
        ]
    }

    monkeypatch.setattr(external_api.requests, "get", lambda *args, **kwargs: DummyResponse(payload))

    product = external_api.fetch_product_by_name("chocolate")
    assert product["name"] == "Chocolate"
