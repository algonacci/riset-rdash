import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790
SOURCE = sys.argv[2] if len(sys.argv) > 2 else "@"
TARGET = sys.argv[3] if len(sys.argv) > 3 else "https://orvix.id"


def create_forwarding(domain_id: int, source: str, target: str) -> dict:
    response = client.post(
        f"/domains/{domain_id}/forwarding",
        data={"from": source, "to": target},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(create_forwarding(DOMAIN_ID, SOURCE, TARGET), indent=2))
