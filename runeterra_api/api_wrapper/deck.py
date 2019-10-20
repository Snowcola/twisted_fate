from pathlib import Path
import os
import json
from .card import Card
from .utils import read_json_file, get_lor_globals

try:
    globals_file = Path("./data/data/globals-en_us.json")
    data_globals = read_json_file(globals_file)
except:
    data_globals = get_lor_globals()


class Deck:
    def __init__(self, **kwargs):
        self._cards = kwargs.get("CardsInDeck", None)
        self.cards = []
        for card, amount in self._cards.items():
            self.cards.append((Card(CardCode=card, count=amount)))

    def __str__(self):
        response = ["Decklist:", "--------------"]

        for card in self.cards:
            response.append(f"({card.cost}) {card.name} x {card.count}")
        return "\n".join(response)
