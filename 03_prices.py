import json

from rdash import client


def get_prices() -> dict:
    response = client.get("/account/prices")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_prices(), indent=2))
