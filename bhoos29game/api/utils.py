from functools import reduce

# cards
cards = ['J', '9', 'A', 'T', 'K', 'Q', '8', '7']
card_weights = [3, 2, 1.5, 1, 0.3, 0.2, 0.1, 0]
enumWeights = dict(zip(cards, card_weights))

suit = ['H', 'C', 'D', 'S']

def hello():
    return "Hello world"


# yo function lai takka conditions herera ramro banauna parxa
def scoreInHandCards(cards):
    myCardWeights = [enumWeights[i[0]] for i in cards]  # weight of my cards
    return 10 + reduce(lambda a, b: a+b, myCardWeights) * 1.5 # yo 1.5 tettikae banako ho haii


def compareSuits(cards,suits_index=0):
    {
        if(suits_)
    }

def selectTrump(cards):
    my_suits=[x[1] for x in cards]
    # count number of suits in cards
    suit_count= [my_suits.count(x) for x in suit]
    # find maximum number of same suit
    max_num=max(suit_count)
    #find suit with maximum number of cards 
    max_index=suit_count.index(max_num)
    # if any suit is more than 2 select that suit
    if(max_num>2):
        return suit[max_index]
    # if any suit is 2 and rest suit are only one select that suit
    elif(max_num==2 and suit_count.count(max_num)==1):
        return suit[max_index]
    #if two suits have 2 cards then find out best suit to select
    elif(max_num==2 and suit_count.count(max_num)==2):
        sec_index=suit_count.index(max_num,max_index,4)
        select =compareSuits(cards,(max_index,sec_index))
        return(suit[select])
    else:

