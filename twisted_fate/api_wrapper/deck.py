from pathlib import Path
import os
import json
from .card import Card
from ..deck_coder.deckCoder import DeckCode
from .utils import read_json_file, get_lor_globals

try:
    globals_file = Path("./data/data/globals-en_us.json")
    data_globals = read_json_file(globals_file)
except:
    data_globals = get_lor_globals()


class Deck:
    def __init__(self, **kwargs):
        self._cards = kwargs.get("CardsInDeck", kwargs.get("cards", None))
        self.deck_code = kwargs.get("DeckCode", None)
        self.cards = []

        if self.deck_code:
            self.decode(self.deck_code, instance=self, in_place=True)

        for card, amount in self._cards.items():
            self.cards.append((Card(CardCode=card, count=amount)))

        if not self.cards and self.deck_code:
            pass  # TODO: generate cards list from deck code

    def encode(self):
        if not self.deck_code:
            self.deck_code = DeckCode.encode_deck(self._cards)
        return self

    @classmethod
    def decode(cls, deck_code, instance=None, in_place=False):
        cards = DeckCode.decode_deck(deck_code)
        if in_place:
            instance._cards = cards
            return None
        return cls(CardsInDeck=cards)

    def to_deck_code(self):
        if not self._cards:
            raise ValueError("Deck is empty")
        if not self.deck_code:
            self.encode()
        return self.deck_code

    def serialize(self):
        s = [c.serialize(as_dict=True) for c in self.cards]
        return json.dumps(s)

    def __str__(self):
        response = ["Decklist:", "--------------"]

        for card in self.cards:
            response.append(f"({card.cost}) {card.name} x {card.count}")
        return "\n".join(response)
