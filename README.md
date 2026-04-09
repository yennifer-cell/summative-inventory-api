# Inventory Management API (Flask)

This project is a Flask-based inventory management system built for a summative lab.
It includes:

- Full CRUD routes for inventory items
- OpenFoodFacts API integration
- A small CLI client to interact with the API
- Pytest tests for API, external integration, and CLI helpers

## 1. Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run the API

```bash
python app.py
```

The API runs on `http://127.0.0.1:5000` by default.

## 3. Run the CLI

In a new terminal (with the venv active and API running):

```bash
python cli.py
```

## 4. Routes

- `GET /` - health message
- `GET /inventory` - list all items
- `GET /inventory/<id>` - fetch one item
- `POST /inventory` - create item
- `PATCH /inventory/<id>` - update item
- `DELETE /inventory/<id>` - delete item
- `GET /external/barcode/<barcode>` - fetch product from OpenFoodFacts by barcode
- `GET /external/search?name=<name>` - fetch product from OpenFoodFacts by name
- `POST /inventory/from-barcode/<barcode>` - create inventory item from external product data

## 5. Sample Request

`POST /inventory`

```json
{
  "name": "Organic Almond Milk",
  "brand": "Silk",
  "quantity": 12,
  "price": 3.99,
  "barcode": "737628064502"
}
```

## 6. Run Tests

```bash
pytest -q
```

## 7. Submission Note

If your LMS asks for a website URL submission, paste the GitHub repository URL for this project.
