import random
#cards 
cards = ['J','9','A','T','K','Q','7','8']
card_weights = [3,2,1,1,0.3,0.2,0.1,0]

# Heart Club Diamond Spade
suit = ['H','C','D','S']
suit_weights = [0,0,0,0]


# {'playerId': 'A2', 
# 'playerIds': ['A1', 'B1', 'A2', 'B2'], 
# 'timeRemaining': 1500, 
# 'teams': [  {'players': ['A1', 'A2'], 'bid': 17, 'won': 0}, 
#             {'players': ['B1', 'B2'], 'bid': 17, 'won': 4} ], 
# 'cards': ['JS', 'TS', 'KH', '9C', 'JD', '7D', '8D'], 
# 'bidHistory': [['A1', 16], ['B1', 17], ['A1', 17], ['B1', 0], ['A2', 0], ['B2', 0]], 
# 'played': ['9S', '1S', '8S'], 
# 'handsHistory': [['A1', ['7H', '1H', '8H', 'JH'], 'B2']], 
# 'trumpSuit': False, 
# 'trumpRevealed': False}

#note that two players cannot have a same bid
def predictBidValue(game):
    bid = 16
    return { "bid" : bid} 

# {'playerId': 'A2',
#  'playerIds': ['A1', 'B1', 'A2', 'B2'],
# 'cards': ['JS', 'TS', 'KH', '9C'], 
# 'timeRemaining': 1000, 
# 'bidHistory': [['A1', 16], ['B1', 0]]}
def predictTrump(game):
    print(game)
    return {"suit": random.choice(suit)}

#{'playerId': 'A2',
# 'playerIds': ['A1', 'B1', 'A2', 'B2'], 
# 'timeRemaining': 1500, 
# 'teams': [{'players': ['A1', 'A2'], 'bid': 17, 'won': 0}, 
#           {'players': ['B1', 'B2'], 'bid': 17, 'won': 4}], 
# 'cards': ['JS', 'TS', 'KH', '9C', 'JD', '7D', '8D'],
# 'bidHistory': [['A1', 16], ['B1', 17], ['A1', 17], ['B1', 0], ['A2', 0], ['B2', 0]], 
# 'played': ['9S', '1S', '8S'], 'handsHistory': [['A1', ['7H', '1H', '8H', 'JH'], 'B2']], '
# trumpSuit': False, 
# 'trumpRevealed': False}
def predictPlay(game):
    print(game)
    return {"card": random.choice(game['cards'])}