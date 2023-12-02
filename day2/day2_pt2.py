def cubes(games):
    games = games.split("\n")

    nums = ["1","2","3","4","5","6","7","8","9","0"]
    col = ["b", "r", "g"]
    result = 0

    for game in games:
        game = game.strip()
        splitter = game.split(":")

        sets = splitter[1]
        sets = sets.split(";")

        colors = {"b" : 0, "r" : 0, "g" : 0}

        for one_set in sets:

            one_set = one_set.strip()
            counter = ""

            for i in range(len(one_set)):
                if one_set[i] in nums:
                    counter += one_set[i]
                if one_set[i] in col and one_set[i-1]  not in col:
                    colors[one_set[i]] = max(int(counter), colors[one_set[i]])
                    counter = ""

        sub_result = 1
        for color, num in colors.items():
            sub_result *= num
        result += sub_result
    return result



if __name__ == "__main__":


    s =  """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    print(cubes(s))

    f = open("day2_input.txt")
    data = f.read().strip()
    print(cubes(data))