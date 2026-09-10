import json
import sys

from rdash import client

DOMAIN = sys.argv[1] if len(sys.argv) > 1 else "sitasiin.my.id"
PERIOD = int(sys.argv[2]) if len(sys.argv) > 2 else 1
CUSTOMER_ID = int(sys.argv[3]) if len(sys.argv) > 3 else 692487


def register_domain(name: str, period: int, customer_id: int) -> dict:
    response = client.post(
        "/domains",
        data={
            "name": name,
            "period": period,
            "customer_id": customer_id,
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(register_domain(DOMAIN, PERIOD, CUSTOMER_ID), indent=2))
