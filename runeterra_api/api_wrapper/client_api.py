import os
import requests
import logging
from .deck import Deck

logger = logging.getLogger("Runterra")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s::%(levelname)s | %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

api_key = os.getenv("API_KEY", "NO KEY PROVIDED")
port = os.getenv("PORT", 21337)
baseurl = f"http://localhost:{port}"

logger.info(api_key)
logger.info(f"Connecting to Legends of Runterra at {baseurl}")


def get_endpoint(endpoint):
    url = f"{baseurl}/{endpoint}"
    logger.info(f"Getting {endpoint}")
    response = requests.get(url)
    status = f"{response.status_code} - {response.ok}"
    logger.info(f"Endpoint: {endpoint} response {status}")
    return response.json()


def decklist() -> dict:
    r = get_endpoint("static-decklist")
    deck = Deck(**r)
    return deck


def card_positions() -> dict:
    r = get_endpoint("positional-rectangles")
    return r


def game_status() -> dict:
    r = get_endpoint("game-result")
    return r


if __name__ == "__main__":
    # requests.get("http://localhost:21337/static-decklist")
    print(decklist())
    print(card_positions())
    print(game_status())

