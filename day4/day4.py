

def scratchcards(cards):
    cards = cards.split("\n")

    result = 0
    for card in cards:
        card = card.split(":")
        own_nums = ((card[1].split("|")[0]).strip()).split(" ")
        win_nums = ((card[1].split("|")[1]).strip()).split(" ")

        points = 0
        for i in own_nums:
            if i in win_nums and i != "":
                if points == 0:
                    points = 1
                else:
                    points *= 2
            
        result += points

    return result

def scratchcards2(cards):
    cards = cards.split("\n")

    card_counter = {}

    for i in range(len(cards)):
        cards[i]= cards[i].split(":")
        own_nums = ((cards[i][1].split("|")[0]).strip()).split(" ")
        win_nums = ((cards[i][1].split("|")[1]).strip()).split(" ")

        if i not in card_counter:
            card_counter[i] = 0

        points = 0
        card_counter[i] += 1
        for j in range(len(own_nums)):
            if own_nums[j] in win_nums and own_nums[j] != "":
                points += 1
                if i+points not in card_counter:
                    card_counter[i+points] = 0
                card_counter[i+points] += card_counter[i]
        
    return sum(card_counter.values())


if __name__ == "__main__":
    s =  """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
            Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
            Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
            Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
            Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    #print(scratchcards(s))
    print(scratchcards2(s)) #30

    f = open("day4_input.txt")
    data = f.read().strip()
    #print(scratchcards(data)) #25010
    print(scratchcards2(data)) #9924412