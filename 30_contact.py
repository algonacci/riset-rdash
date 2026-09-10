import json
import sys

from rdash import client

CUSTOMER_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 692487
CONTACT_ID = int(sys.argv[2]) if len(sys.argv) > 2 else 609309


def get_contact(customer_id: int, contact_id: int) -> dict:
    response = client.get(f"/customers/{customer_id}/contacts/{contact_id}")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_contact(CUSTOMER_ID, CONTACT_ID), indent=2))
