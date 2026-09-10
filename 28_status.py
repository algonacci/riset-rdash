import json

from rdash import client


def get_status() -> dict:
    response = client.get("/status")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_status(), indent=2))
