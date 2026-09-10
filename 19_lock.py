import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790
REASON = sys.argv[2] if len(sys.argv) > 2 else "theft protection"


def lock_domain(domain_id: int, reason: str) -> dict:
    response = client.put(
        f"/domains/{domain_id}/locked",
        data={"reason": reason},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(lock_domain(DOMAIN_ID, REASON), indent=2))
