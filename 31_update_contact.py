import json
import sys

from rdash import client

CUSTOMER_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 692487
CONTACT_ID = int(sys.argv[2]) if len(sys.argv) > 2 else 609309


def update_contact(customer_id: int, contact_id: int) -> dict:
    current = client.get(f"/customers/{customer_id}/contacts/{contact_id}")
    current.raise_for_status()
    data = current.json()["data"]
    data["state"] = "DKI Jakarta"

    response = client.put(
        f"/customers/{customer_id}/contacts/{contact_id}",
        data={
            "label": data["label"],
            "name": data["name"],
            "email": data["email"],
            "organization": data["organization"],
            "street_1": data["street_1"],
            "city": data["city"],
            "state": data["state"],
            "country_code": data["country_code"],
            "postal_code": data["postal_code"],
            "voice": data["voice"],
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(update_contact(CUSTOMER_ID, CONTACT_ID), indent=2))
