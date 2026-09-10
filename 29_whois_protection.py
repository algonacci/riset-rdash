import json
import sys

from rdash import client

DOMAIN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 555790


def get_whois_protection(domain_id: int) -> dict:
    response = client.get(f"/domains/{domain_id}/whois-protection")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_whois_protection(DOMAIN_ID), indent=2))
