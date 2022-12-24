import random
from functools import reduce
from .utils import *
# cards
cards = ['J', '9', '1', 'T', 'K', 'Q', '8', '7']
card_weights = [3, 2, 1.5, 1, 0.3, 0.2, 0.1, 0]
enumWeights = dict(zip(cards, card_weights))

# Heart Club Diamond Spade
suit = ['H', 'C', 'D', 'S']


# note that two players cannot have a same bid





'''
{'playerId': 'You-1', 
'playerIds': ['You-0', 'Opponent-0', 'You-1', 'Opponent-1'], 
'cards': ['JC', 'TD', '9D', 'KC'],
'timeRemaining': 1500, 
'bidHistory': [['You-0', 0], ['Opponent-0', 16]], 
'bidState': {
    'defenderId': 'Opponent-0', 
    'challengerId': 'You-1',
    'defenderBid': 16, 
    'challengerBid': 0}}
'''

def predictBidValue(game):
    print("Predicting bid for : ")
    print(game)
    optimumBid = optimumBidVal(game['cards'])
    print(f"optimum bid: {optimumBid}")
    # get bid for challenger and defender
    challengerBid=game['bidState']['challengerBid']
    defenderBid=game['bidState']['defenderBid']

    myTurn = len(game['bidHistory'])
    
    # yedi surumaii mero bid xa vane mero cards herera maile bid hanna paryo
    # if my score is more than 6 i'll only bid 16 if my turn is 1st
    if (myTurn == 0):
        if(optimumBid >= 16): return {"bid": 16}
    # yedi second ma mero turn xa vane defender(i.e first ma bid garne opponent hunxa) ko bid herera mero dherai xa vane hanna paryo
    elif (myTurn == 1):
        if(defenderBid==0 and optimumBid>=16):
            return {'bid':16}
        elif(defenderBid < optimumBid):
            return {"bid":defenderBid+1}
        else:
            return {'bid':0}
    else:
        # check if whether i am challenger or defender
        # looking at the payload i found we are either challenger or defender
        if(game['bidState']['challengerId'] == game['playerId'] ):
            if(defenderBid==0 and optimumBid>=16):
                return {'bid':16}

            elif(defenderBid<optimumBid and defenderBid!=0):
                # raise bid 1 more than defender if our optimum bid is more 
                return {'bid':defenderBid+1}
            else:
                return {'bid':0}
        # in case i am defender
        else:
            if(challengerBid==0 and optimumBid>=16):
                return {'bid':16}
            elif(challengerBid<=optimumBid and challengerBid!=0):
                # we don't have to bid more than challenger we can just match the bid
                return {'bid':challengerBid}
        # sathi le defend gariraxa opponent ko higher score bata

    return {"bid": 0}


'''
{'playerId': 'You-1', 
'playerIds': ['You-0', 'Opponent-0', 'You-1', 'Opponent-1'],
'cards': ['7S', 'JS', 'TS', '9H'], 
'timeRemaining': 1483, 
'bidHistory': [['You-0', 0], ['Opponent-0', 16], ['You-1', 20], ['Opponent-0', 0], ['Opponent-1', 0]]}
'''

def predictTrump(game):
    print("Predicting Trump for : ")
    print(game)
    # tara bid history bata keii keii infer garna sakinxa
    trump=selectTrump(game['cards'])
    return {"suit":trump }


'''
{'playerId': 'You-1',
'playerIds': ['You-0', 'Opponent-0', 'You-1', 'Opponent-1'],
'cards': ['QC', 'QD', 'JS', 'TS', 'TH', '9H', '8S', '7S'],
'timeRemaining': 1468, 
'bidHistory': [['You-0', 0], ['Opponent-0', 16], ['You-1', 20], ['Opponent-0', 0], ['Opponent-1', 0]], 
'played': ['JC', '7C'], 
'teams':[{'players': ['You-0', 'You-1'], 'bid': 20, 'won': 0}, 
        {'players': ['Opponent-0', 'Opponent-1'],'bid': 0, 'won': 0}], 
'handsHistory': [], 
'trumpSuit': 'S', 
'trumpRevealed': False}
'''
def predictPlay(game):
    print("Predicting play for : ")
    print(game)
    return {"card": random.choice(game['cards'])}


if __name__ == '__main__':
    print(
    predictBidValue({'playerId': 'You-0', 'playerIds': ['You-0', 'Opponent-0', 'You-1', 'Opponent-1'], 'cards': ['KS', '1S', '8D', '9S'], 'timeRemaining': 1500, 'bidHistory': [], 'bidState': {'defenderId': 'You-0', 'challengerId': 'Opponent-0', 'defenderBid': 0, 'challengerBid': 0}})
    )
    #HCDS

