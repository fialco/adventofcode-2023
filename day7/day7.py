def hand_transform(hand):
    hand = [*hand]
    
    for i in range(len(hand)):
        if hand[i] == "T":
            hand[i] = 10
        elif hand[i] == "J":
            hand[i] = 11
        elif hand[i] == "Q":
            hand[i] = 12
        elif hand[i] == "K":
            hand[i] = 13
        elif hand[i] == "A":
            hand[i] = 14
    return [int(i) for i in hand]

def hand_calc(hand):
    
    if len(set([*hand])) == 1: #Five of a kind
        return 7
    
    values = {}
    for card in hand:
        if card not in values:
            values[card] = 0
        values[card] += 1
    
    if 4 in values.values(): #Four of a kind
        return 6
    
    elif 3 in values.values() and 2 in values.values(): #Full house
        return 5
    
    elif 3 in values.values(): #Three of a kind
        return 4
    
    elif list(values.values()).count(2) == 2: #Two pair
        return 3
    
    elif 2 in values.values(): #One pair:
        return 2
    
    else: #High card
         return 1


def poker(stakes):
    stakes = stakes.split("\n")

    stats = []

    for stake in stakes:
        stake = stake.strip().split()
        
        hand = stake[0]
        bid = int(stake[1])

        hand_type = hand_calc(hand) 
        transformed = hand_transform(hand)
        
        stats.append((hand_type, transformed, bid))
    stats.sort()
    stats = list(enumerate(stats, start=1))

    result = 0
    for i in stats:
        result += i[0]*i[1][2]


    return result


def hand_transform2(hand):
    hand = [*hand]
    
    for i in range(len(hand)):
        if hand[i] == "T":
            hand[i] = 10
        elif hand[i] == "J":
            hand[i] = 1
        elif hand[i] == "Q":
            hand[i] = 12
        elif hand[i] == "K":
            hand[i] = 13
        elif hand[i] == "A":
            hand[i] = 14
    return [int(i) for i in hand]

def hand_calc2(hand):

    if len(set([*hand])) == 1: #Five of a kind
        return 7
    
    values = {}
    for card in hand:
        if card not in values:
            values[card] = 0
        values[card] += 1
    
    if "J" in values:
        if values["J"] >= 2:
            pass
        j = values["J"]
        del values["J"]
        largest = max(values, key=values.get)
        values[largest] += j


    if 5 in values.values(): #Five of a kind
        return 7

    elif 4 in values.values(): #Four of a kind
        return 6
    
    elif 3 in values.values() and 2 in values.values(): #Full house
        return 5
    
    elif 3 in values.values(): #Three of a kind
        return 4
    
    elif list(values.values()).count(2) == 2: #Two pair
        return 3
    
    elif 2 in values.values(): #One pair:
        return 2
    
    else: #High card
         return 1


def poker2(stakes):
    stakes = stakes.split("\n")

    stats = []

    for stake in stakes:
        stake = stake.strip().split()
        
        hand = stake[0]
        bid = int(stake[1])

        hand_type = hand_calc2(hand) 
        transformed = hand_transform2(hand)
        
        stats.append((hand_type, transformed, bid))
    stats.sort()
    stats = list(enumerate(stats, start=1))

    result = 0
    for i in stats:
        result += i[0]*i[1][2]


    return result


if __name__ == "__main__":
    s =  """32T3K 765
            T55J5 684
            KK677 28
            KTJJT 220
            QQQJA 483"""
    print(poker(s))
    print(poker2(s))

    f = open("day7_input.txt")
    data = f.read().strip()
    print(poker(data))
    print(poker2(data))

    