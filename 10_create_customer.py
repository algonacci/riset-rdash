import json
import os

from rdash import client

payload = {
    "name": os.environ["RDASH_CUSTOMER_NAME"],
    "email": os.environ["RDASH_CUSTOMER_EMAIL"],
    "password": os.environ["RDASH_CUSTOMER_PASSWORD"],
    "password_confirmation": os.environ["RDASH_CUSTOMER_PASSWORD"],
    "organization": os.environ["RDASH_CUSTOMER_ORGANIZATION"],
    "street_1": os.environ["RDASH_CUSTOMER_STREET"],
    "city": os.environ["RDASH_CUSTOMER_CITY"],
    "state": os.environ["RDASH_CUSTOMER_STATE"],
    "country_code": os.environ.get("RDASH_CUSTOMER_COUNTRY", "ID"),
    "postal_code": os.environ["RDASH_CUSTOMER_POSTAL_CODE"],
    "voice": os.environ["RDASH_CUSTOMER_PHONE"],
}


def create_customer() -> dict:
    response = client.post("/customers", data=payload)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(json.dumps(create_customer(), indent=2))
