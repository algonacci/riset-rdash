import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790
NAME = sys.argv[2] if len(sys.argv) > 2 else "www"
RECORD_TYPE = sys.argv[3] if len(sys.argv) > 3 else "A"
CONTENT = sys.argv[4] if len(sys.argv) > 4 else "1.1.1.1"


def delete_dns(domain_id: int, name: str, record_type: str, content: str) -> dict:
    response = client.request(
        "DELETE",
        f"/domains/{domain_id}/dns/record",
        data={
            "name": name,
            "type": record_type,
            "content": content,
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(delete_dns(DOMAIN_ID, NAME, RECORD_TYPE, CONTENT), indent=2))
