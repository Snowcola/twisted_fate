from runeterra_api import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_deck():
    import runeterra_api as api

    deck = {
        "DeckCode": "CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ",
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
    z = api.Deck(**deck)
    assert z.cards[0].cardCode in deck["CardsInDeck"]