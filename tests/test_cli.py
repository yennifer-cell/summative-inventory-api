import cli


class DummyResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload
        self.text = str(payload)

    def json(self):
        return self._payload


def test_request_json_get(monkeypatch):
    monkeypatch.setattr(
        cli.requests,
        "request",
        lambda *args, **kwargs: DummyResponse(200, [{"id": 1, "name": "Milk"}]),
    )

    status, data = cli.request_json("GET", "/inventory")
    assert status == 200
    assert data[0]["name"] == "Milk"


def test_request_json_delete(monkeypatch):
    monkeypatch.setattr(
        cli.requests,
        "request",
        lambda *args, **kwargs: DummyResponse(204, None),
    )

    status, data = cli.request_json("DELETE", "/inventory/1")
    assert status == 204
    assert data is None
