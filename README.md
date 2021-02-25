# twisted_fate


A python api wrapper to for riot's Legends of Runterra client-api including a port of [Riot Games C# implementation of the deck encoder/decoder](https://github.com/RiotGames/LoRDeckCodes)

# Install


```
pip install twisted_fate
```

## Usage

### Create Deck from deck code
```python
from twisted_fate import Deck

draven_deck = Deck.decode("CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ")

# results
print(deck.cards)
#[
#    Card(01NX020, Name: Draven, Cost: 3), 
#    Card(01NX035, Name: Draven's Biggest Fan, Cost: 1), 
#    Card(01NX039, Name: Vision, Cost: 3), 
#    Card(01PZ001, Name: Rummage, Cost: 1), 
#    Card(01PZ012, Name: Flame Chompers!, Cost: 2), 
#    Card(01PZ013, Name: Augmented Experimenter, Cost: 6), #    Card(01PZ018, Name: Academy Prodigy, Cost: 2), 
#    Card(01PZ028, Name: Jury-Rig, Cost: 1), 
#    Card(01PZ038, Name: Sump Dredger, Cost: 2), 
#    Card(01PZ039, Name: Get Excited!, Cost: 3), 
#    Card(01PZ040, Name: Jinx, Cost: 4), 
#    Card(01PZ045, Name: Zaunite Urchin, Cost: 1), 
#    Card(01PZ052, Name: Mystic Shot, Cost: 2), 
#    Card(01NX011, Name: Whirling Death, Cost: 3)
# ]
```
### Create Deck from cards list, (in the format of a response from the client api)
```python
from twisted_fate import Deck
# client api response
deck = {
    "DeckCode":"CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ",
    "CardsInDeck": {
        "01NX020": 3,
        "01NX035": 3,
        "01NX039": 3,
        "01PZ001": 3,
        "01PZ012": 3,
        "01PZ013": 3,
        "01PZ018": 3,
        "01PZ028": 3,
        "01PZ038": 3,
        "01PZ039": 3,
        "01PZ040": 3,
        "01PZ045": 3,
        "01PZ052": 3,
        "01NX011": 1,
    },
}


draven_deck = Deck(cards=deck["CardsInDeck"])
print(draven_deck.encode().deck_code)
# result: CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ

# or

print(draven_deck.to_deck_code())
# result: CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ
```
