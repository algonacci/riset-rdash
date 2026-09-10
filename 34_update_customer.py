import json
import os
import sys

from rdash import client

CUSTOMER_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 692487


def update_customer(customer_id: int) -> dict:
    current = client.get(f"/customers/{customer_id}")
    current.raise_for_status()
    data = current.json()["data"]
    password = os.environ["RDASH_CUSTOMER_PASSWORD"]

    response = client.put(
        f"/customers/{customer_id}",
        data={
            "name": data["name"],
            "email": data["email"],
            "password": password,
            "password_confirmation": password,
            "organization": data["organization"],
            "street_1": data["street_1"],
            "city": data["city"],
            "state": "DKI Jakarta",
            "country_code": data["country_code"],
            "postal_code": data["postal_code"],
            "voice": data["voice"],
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(update_customer(CUSTOMER_ID), indent=2))
