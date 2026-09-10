import json
import sys

from rdash import client

TRANSACTION_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 632159


def get_transaction(transaction_id: int) -> dict:
    response = client.get(f"/account/transactions/{transaction_id}")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_transaction(TRANSACTION_ID), indent=2))
