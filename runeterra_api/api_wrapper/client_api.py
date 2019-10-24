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


class LoRClient:
    
    baseurl = f"http://localhost:"

    def __init__(self, api_key, port):
        self.api_key = api_key
        self.port = port
        self.baseurl = self.baseurl + port

    def get_endpoint(self, endpoint):
        url = f"{self.baseurl}/{endpoint}"
        logger.info(f"Getting {endpoint}")
        response = requests.get(url)
        status = f"{response.status_code} - {response.ok}"
        logger.info(f"Endpoint: {endpoint} response {status}")
        return response.json()

    def decklist(self) -> dict:
        r = self.get_endpoint("static-decklist")
        deck = Deck(**r)
        return deck

    def card_positions(self) -> dict:
        r = self.get_endpoint("positional-rectangles")
        return r

    def game_status(self) -> dict:
        r = self.get_endpoint("game-result")
        return r
