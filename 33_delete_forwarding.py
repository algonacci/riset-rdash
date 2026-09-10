import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790
FORWARDING_ID = int(sys.argv[2]) if len(sys.argv) > 2 else 15735


def delete_forwarding(domain_id: int, forwarding_id: int) -> dict:
    response = client.delete(f"/domains/{domain_id}/forwarding/{forwarding_id}")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(delete_forwarding(DOMAIN_ID, FORWARDING_ID), indent=2))
