import random
from functools import reduce
from .utils import *
# cards
cards = ['J', '9', 'A', 'T', 'K', 'Q', '8', '7']
card_weights = [3, 2, 1.5, 1, 0.3, 0.2, 0.1, 0]
enumWeights = dict(zip(cards, card_weights))

# Heart Club Diamond Spade
suit = ['H', 'C', 'D', 'S']


# note that two players cannot have a same bid
'''

{'playerId': 'A2',
'playerIds': ['A1', 'B1', 'A2', 'B2'],
'cards': ['JS', 'TS', 'KH', '9C'],
'timeRemaining': 1000,
'bidHistory': [['A1', 16], ['B1', 0]],
'bidState': { 'defenderId': 'A1',  # current defender
              'challengerId': 'B1',  #current challenger
              'defenderBid': 16,
              'challengerBid': 17}}
'''

def predictBidValue(game):
    bid = 0
    myHandValue = round(scoreInHandCards(game['cards']))
    myTag = game['playerId'][1] # A B

    myTurn = len(game['bidHistory'])
    # yedi surumaii mero bid xa vane mero cards herera maile bid hanna paryo
    if (myTurn == 0):
        if(myHandValue >= 16): bid = myHandValue
    # yedi second ma mero turn xa vane defender(i.e first ma bid garne opponent hunxa) ko bid herera mero dherai xa vane hanna paryo
    elif (myTurn == 1):
        if(game.bidState['defenderBid'] < myHandValue):
            if(myHandValue > 16): bid = myHandValue
    else:
        # sathi gunda sathi tero
        # Note : challenge garne manxe ko bid defend garne ko vanda thulo hunxa (Hola XD)
        # sathi le challenge hanirathyo vane
        if(game['bidState']['challengerId'][0] == myTag ):
            friendsBid = game['bidState']['challengerBid']
            opponentBid = game['bidState']['DefenderBid']
            # sabb le pass pass gardai gardai hamro palo aayo vane 
            if(friendsBid == 0 and  opponentBid == 0):
                if(myHandValue > 16): bid = myHandValue  
            #sathi le jitiraxa vane
            else:
                # aafno haat ko value add garera raise garne bid (milxa vane)
                bid = game['bidState']['challengerBid'] + (myHandValue - 10)//2
            
        # sathi le defend gariraxa opponent ko higher score bata
        else:
            friendsBid = game['bidState']['defenderBid']
            avgScore = (friendsBid + myHandValue)//2
            if(avgScore > game['bidState']['challengerBid']):
                bid = avgScore

    return {"bid": bid}

# {'playerId': 'A2',
#  'playerIds': ['A1', 'B1', 'A2', 'B2'],
# 'cards': ['JS', 'TS', 'KH', '9C'],
# 'timeRemaining': 1000,
# 'bidHistory': [['A1', 16], ['B1', 0]]}

def predictTrump(game):
    # tara bid history bata keii keii infer garna sakinxa
    # aahile lai aafu sanga jun dherai xa tyo rakhne tw hola ni
        # Kunai suit ko jack pareko xa vane tyeslai naganne .. tyesko weight chhai 0 rakhne .. vannale hataidiye pani vayo
        # kunai suit ma 9 A 10 pareko xa vane tyelle jitne parama weights le multiply garne ani tyelai prefer garne

    # jack ko cards lai hataune    
    cards_JacksRemoved = list(filter(lambda x : x[0] != 'J',game['cards']))

    suitsInHand = [x[1] for x in cards_JacksRemoved]
    suitCount = [suitsInHand.count(x) for x in suit]

    # hareko suit ko card ko weighted sum nikalne
    suitWeights = [0,0,0,0]
    index = 0
    for x in suit:
        cards = [enumWeights[j[0]] for j in cards_JacksRemoved if j[1]==x]
        if(len(cards)):
            # no. of cards of a suit * (sum of weights of a suit)
            suitWeights[index] = suitCount[index] * reduce(lambda a,b : a+b ,cards)
        index += 1

    return {"suit": suit[suitWeights.index(max(suitWeights))]}

# {'playerId': 'A2',
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


if __name__ == '__main__':
    print(
    predictTrump({'playerId': 'A2',
    'playerIds': ['A1', 'B1', 'A2', 'B2'],
    'cards': ['JS', 'TS', '9S', '9C'],
    'timeRemaining': 1000,
    'bidHistory': [['A1', 16], ['B1', 0]],
    'bidState': { 'defenderId': 'A1',
                  'challengerId': 'B1',
                  'defenderBid': 16,
                  'challengerBid': 17}})
    )
    #HCDS

