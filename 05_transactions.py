import json
import sys
from datetime import date

from rdash import client

TODAY = date.today()
DATE_RANGE = sys.argv[1] if len(sys.argv) > 1 else f"{TODAY.replace(month=1, day=1)}_{TODAY}"


def get_transactions(date_range: str) -> dict:
    response = client.get(
        "/account/transactions",
        params={"date_range": date_range},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_transactions(DATE_RANGE), indent=2))
