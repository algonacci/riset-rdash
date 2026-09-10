import json
import sys

from rdash import client

DOMAIN = sys.argv[1] if len(sys.argv) > 1 else "sitasiin.my.id"


def get_whois(domain: str) -> dict:
    response = client.get("/domains/whois", params={"domain": domain})
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_whois(DOMAIN), indent=2))
