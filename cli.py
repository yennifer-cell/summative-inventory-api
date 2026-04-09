import os

import requests

BASE_URL = os.getenv("INVENTORY_API_URL", "http://127.0.0.1:5000")


def request_json(method, path, payload=None):
    url = f"{BASE_URL}{path}"
    response = requests.request(method, url, json=payload, timeout=10)

    if response.status_code == 204:
        return response.status_code, None

    try:
        return response.status_code, response.json()
    except ValueError:
        return response.status_code, {"raw": response.text}


def print_menu():
    print("\nInventory CLI")
    print("1. List inventory")
    print("2. View one item")
    print("3. Add item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Find external product by barcode")
    print("7. Add product from barcode")
    print("8. Exit")


def run_cli():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                status, data = request_json("GET", "/inventory")
                print(status, data)

            elif choice == "2":
                item_id = int(input("Item id: ").strip())
                status, data = request_json("GET", f"/inventory/{item_id}")
                print(status, data)

            elif choice == "3":
                name = input("Name: ").strip()
                brand = input("Brand: ").strip()
                quantity = int(input("Quantity: ").strip())
                price = float(input("Price: ").strip())
                barcode = input("Barcode (optional): ").strip()
                payload = {
                    "name": name,
                    "brand": brand,
                    "quantity": quantity,
                    "price": price,
                    "barcode": barcode,
                }
                status, data = request_json("POST", "/inventory", payload)
                print(status, data)

            elif choice == "4":
                item_id = int(input("Item id: ").strip())
                field = input("Field to update (name/brand/quantity/price/barcode): ").strip()
                raw_value = input("New value: ").strip()

                if field == "quantity":
                    value = int(raw_value)
                elif field == "price":
                    value = float(raw_value)
                else:
                    value = raw_value

                status, data = request_json("PATCH", f"/inventory/{item_id}", {field: value})
                print(status, data)

            elif choice == "5":
                item_id = int(input("Item id: ").strip())
                status, _ = request_json("DELETE", f"/inventory/{item_id}")
                print(status)

            elif choice == "6":
                barcode = input("Barcode: ").strip()
                status, data = request_json("GET", f"/external/barcode/{barcode}")
                print(status, data)

            elif choice == "7":
                barcode = input("Barcode: ").strip()
                quantity = int(input("Quantity to add: ").strip())
                status, data = request_json("POST", f"/inventory/from-barcode/{barcode}", {"quantity": quantity})
                print(status, data)

            elif choice == "8":
                print("Goodbye")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input type. Try again.")
        except requests.RequestException:
            print("Request failed. Is the Flask API running?")


if __name__ == "__main__":
    run_cli()
