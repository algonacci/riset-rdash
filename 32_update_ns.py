import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790
NS1 = sys.argv[2] if len(sys.argv) > 2 else "ns1.orvix.id"
NS2 = sys.argv[3] if len(sys.argv) > 3 else "ns2.orvix.id"


def update_ns(domain_id: int, ns1: str, ns2: str) -> dict:
    response = client.put(
        f"/domains/{domain_id}/ns",
        data={
            "nameserver[0]": ns1,
            "nameserver[1]": ns2,
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(update_ns(DOMAIN_ID, NS1, NS2), indent=2))
