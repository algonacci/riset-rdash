import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790


def create_dns(domain_id: int) -> dict:
    response = client.post(
        f"/domains/{domain_id}/dns",
        data={
            "records[0][name]": "www",
            "records[0][type]": "A",
            "records[0][content]": "1.1.1.1",
            "records[0][ttl]": 3600,
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(create_dns(DOMAIN_ID), indent=2))
