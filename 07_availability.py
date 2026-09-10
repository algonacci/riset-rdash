import json
import sys

from rdash import client

DOMAIN = sys.argv[1] if len(sys.argv) > 1 else "orvix.my.id"


def check_availability(domain: str) -> dict:
    response = client.get(
        "/domains/availability",
        params={"domain": domain},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(check_availability(DOMAIN), indent=2))
