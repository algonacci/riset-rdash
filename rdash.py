import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ["RDASH_BASE_URL"]
RESELLER_ID = os.environ["RDASH_RESELLER_ID"]
API_KEY = os.environ["RDASH_API_KEY"]

client = httpx.Client(
    base_url=BASE_URL,
    auth=(RESELLER_ID, API_KEY),
    timeout=30,
)
