

def hand_calc(hand):
    
    if len(set([*hand])) == 1: #Five of a kind
        return 1
    
    values = {}
    for card in hand:
        if card not in values:
            values[card] = 0
        values[card] += 1
    
    if 4 in values.values(): #Four of a kind
        return 2
    
    elif 3 in values.values() and 2 in values.values(): #Full house
        return 3
    
    elif 3 in values.values(): #Three of a kind
        return 4
    
    elif list(values.values()).count(2) == 2: #Two pair
        return 5
    
    elif 2 in values.values(): #One pair:
        return 6
    
    else: #High card
         return 7


def poker(stakes):
    stakes = stakes.split("\n")
    for stake in stakes:
        stake = stake.strip().split()
        
        hand = stake[0]
        bid = int(stake[1])

        hand_type = hand_calc(hand)





    result = 1


    return result



    
if __name__ == "__main__":
    s =  """32T3K 765
            T55J5 684
            KK677 28
            KTJJT 220
            QQQJA 483"""
    print(poker(s))
    #print(wait2(s))

    f = open("day7_input.txt")
    data = f.read().strip()
    #print(poker(data))
    #print(wait2(data))

    