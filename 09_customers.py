import json

from rdash import client


def get_customers() -> dict:
    response = client.get("/customers")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_customers(), indent=2))
