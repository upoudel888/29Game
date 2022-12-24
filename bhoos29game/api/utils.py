from functools import reduce

# cards
cards = ['J', '9', 'A', 'T', 'K', 'Q', '8', '7']
card_weights = [3, 2, 1.5, 1, 0.3, 0.2, 0.1, 0]
enumWeights = dict(zip(cards, card_weights))

suit = ['H', 'C', 'D', 'S']


# need to find more ways/reasons to increase optimum bid
#check for maximum bid that can be made
def optimumBidVal(cards):
    
    my_suits=[x[1] for x in cards]
    # count number of suits in cards
    suit_count= [my_suits.count(x) for x in suit]
    # find maximum number of same suit
    max_num=max(suit_count)
    max_index=suit_count.index(max_num)
    # find how many of each cards you have
    all_cards=[card[0] for card in cards]
    jacks=all_cards.count('J')
    nines=all_cards.count('9')
    aces=all_cards.count('1')
    tens=all_cards.count('T')
    # king=all_cards.count('K')
    # queen=all_cards.count('Q')
    # eights=all_cards.count('8')
    # sevens=all_cards.count('7')

    # find total points i have 
    sum_all=jacks*3+nines*2+aces*1+tens*1
    #assume that every jack wins two more points 
    my_bid=sum_all+jacks*2
    #having more cards of same suit will earn more points if you get to pick the trump
    if(max_num>2):
      
        #check if there is J in suit with maximum card
        js=cards.count('J'+suit[max_index])
        ns=cards.count('9'+suit[max_index])
        Acs=cards.count('1'+suit[max_index]) 
        # increase bid according to presence of high ranking cards in suit with maximum cards
        if(js and ns):
            sum_all+=+max_num+5+Acs*2
        if(js>0 and ns==0):
            sum_all+=max_num+4+Acs*2
        elif(js==0 and ns>0):
            sum_all+=max_num+3+Acs*2
        else:
            sum_all+=max_num+2+Acs
        # having jack increases the more points winning chances
    elif(max_num==2):
        # if one suits have two card and rest have 1 cards
        if(suit_count.count(max_num)==1):
            #check if there is J and 9 in suit with maximum card
            js=cards.count('J'+suit[max_index])
            ns=cards.count('9'+suit[max_index])
            Acs=cards.count('1'+suit[max_index]) 
            sum_all+=(js+ns+Acs)*2+2
        #if two suits have two cards 
        else:
            # check jack and 9 in first suit
            js=cards.count('J'+suit[max_index])
            ns=cards.count('9'+suit[max_index])
            Acs=cards.count('1'+suit[max_index]) 
            if(js and ns):
                sum_all+=max_num+3+Acs
            elif(js>0 and ns==0):
                sum_all+=max_num+2+Acs
            elif(js==0 and ns>0):
                sum_all+=max_num+1+Acs
            else:
                sum_all+=2+Acs
            # check jack and 9 in second suit
            max_index=suit_count.index(max_num,max_index,4)
            js=cards.count('J'+suit[max_index])
            ns=cards.count('9'+suit[max_index])
            Acs=cards.count('1'+suit[max_index]) 
            if(js and ns):
                sum_all+=max_num+3+Acs*2
            elif(js>0 and ns==0):
                sum_all+=max_num+3+Acs*2
            elif(js==0 and ns>0):
                sum_all+=max_num+1+Acs
            else:
                sum_all+=2+Acs
        
    else:
        sum_all+=jacks*2+nines+2
        
    return sum_all

def compareSuitsWeights(cards,suits_index=0):
    suitWeights = [0,0,0,0]
    index=0
    for x in suit:
        current_suit_weights=[enumWeights[j[0]] for j in cards if j[1]==x]
        if(len(current_suit_weights)):
            suitWeights[index]=sum(current_suit_weights)
        index+=1
    return suitWeights

def selectTrump(cards):
    my_suits=[x[1] for x in cards]
    # count number of suits in cards
    suit_count= [my_suits.count(x) for x in suit]
    # find maximum number of same suit
    max_num=max(suit_count)
    #find suit with maximum number of cards 
    max_index=suit_count.index(max_num)
    # if any suit is more than 2 select that suit i.e 3 or 4
    if(max_num>2):
        return suit[max_index]
    # if any suit is 2 and rest suit are only one select that suit
    elif(max_num==2 and suit_count.count(max_num)==1):
        return suit[max_index]
    #if two suits have 2 cards or every suit has one card we find suit with highest weight
    else:
        weights =compareSuitsWeights(cards)
        max_weight=max(weights)
        max_weight_index=weights.index(max_weight)
        return(suit[max_weight_index])
    

