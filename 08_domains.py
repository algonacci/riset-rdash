import json

from rdash import client


def get_domains() -> dict:
    response = client.get("/domains")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_domains(), indent=2))
