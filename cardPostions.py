from pathlib import Path
import os
import json

globals_file = Path("./static/data/globals-en_us.json")
cards_file = Path("./static/data/set1-en_us.json")

def read_json_file(json_file):
    with open(json_file,encoding='utf8') as f:
        return json.load(f)
#os.startfile(globfile)
data_globals = read_json_file(globals_file)
cards = read_json_file(cards_file)

{
    'PlayerName': 'Snowcola', 
    'OpponentName': 'decks_easythresh_name', 
    'GameState': 'InProgress', 
    'Screen': {'ScreenWidth': 3440, 'ScreenHeight': 1440}, 
    'Rectangles': [
                    {
                        'CardID': 138431400, 
                        'CardCode': 'face', 
                        'TopLeftX': 679, 
                        'TopLeftY': 641, 
                        'Width': 156, 
                        'Height': 156, 
                        'LocalPlayer': True
                    }, 
                    {
                        'CardID': 603424583, 
                        'CardCode': 'face', 
                        'TopLeftX': 679, 
                        'TopLeftY': 954, 'Width': 156, 'Height': 156, 'LocalPlayer': False}, 
                    {'CardID': 2140338133, 'CardCode': '01PZ028', 'TopLeftX': 1131, 'TopLeftY': 92, 'Width': 259, 'Height': 408, 'LocalPlayer': True}, 
                    {'CardID': 71529299, 'CardCode': '01PZ018', 'TopLeftX': 1358, 'TopLeftY': 101, 'Width': 260, 'Height': 410, 'LocalPlayer': True}, 
                    {'CardID': 1625404956, 'CardCode': '01PZ038', 'TopLeftX': 1588, 'TopLeftY': 101, 'Width': 262, 'Height': 412, 'LocalPlayer': True}, 
                    {'CardID': 1325864964, 'CardCode': '01NX020', 'TopLeftX': 1821, 'TopLeftY': 95, 'Width': 263, 'Height': 414, 'LocalPlayer': True}, 
                    {'CardID': 1880618219, 'CardCode': '01PZ040', 'TopLeftX': 2055, 'TopLeftY': 79, 'Width': 264, 'Height': 416, 'LocalPlayer': True}
                    ]
}

class Card:
    def __init__(self, **kwargs):
        self.id = kwargs.get('CardID', None)
        self.card_code = kwargs.get('CardCode', None)
        try:
            self.image_path = Path(f"./static/img/cards/{self.card_code}.png")
            self.image_path_full = Path(f"./static/img/cards/{self.card_code}-full.png")
            self._card_data = self.card_info()
        except Exception:
            pass
        
    def card_info(self):
        for item in cards:
            if item["cardCode"] == self.card_code:
                return item
    
    @property
    def name(self):
        return self._card_data['name']

    @property
    def description(self):
        return self._card_data['descriptionRaw']

    @property
    def cost(self):
        return self._card_data['cost']

    def __str__(self):
        return f"({self.cost}) {self.name}: {self.description}"

    def __hash__(self):
        return hash(self.card_code)


deck = {'DeckCode': 'CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ', 'CardsInDeck': {'01NX020': 3, '01NX035': 3, 
'01NX039': 3, '01PZ001': 3, '01PZ012': 3, '01PZ013': 3, '01PZ018': 3, '01PZ028': 3, '01PZ038': 3, '01PZ039': 3, '01PZ040': 3, '01PZ045': 3, '01PZ052': 3, '01NX011': 1}}

class Deck:
    def __init__(self, **kwargs):
        self._cards = kwargs.get("CardsInDeck", None)
        self.cards = []
        for card, amount in self._cards.items():
            self.cards.append((Card(CardCode=card), amount))

    def __str__(self):
        response = ["Decklist:", "--------------"]
        
        for card, num in self.cards:
            response.append(f"({card.cost}) {card.name} x {num}")
        return "\n".join(response)
