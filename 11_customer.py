import json
import sys

from rdash import client

CUSTOMER_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 692487


def get_customer(customer_id: int) -> dict:
    response = client.get(f"/customers/{customer_id}")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_customer(CUSTOMER_ID), indent=2))
