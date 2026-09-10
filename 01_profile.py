import json

from rdash import client


def get_profile() -> dict:
    response = client.get("/account/profile")
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(get_profile(), indent=2))
