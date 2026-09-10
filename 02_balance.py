import json

from rdash import client


def get_balance() -> dict:
    response = client.get("/account/balance")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_balance(), indent=2))
