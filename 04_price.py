import json
import sys

from rdash import client

PRICE_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 84959


def get_price(price_id: int) -> dict:
    response = client.get(f"/account/prices/{price_id}")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_price(PRICE_ID), indent=2))
