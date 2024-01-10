
def wasteland(info):
    info = info.split("\n")

    graph = {}
    route = info[0]

    info = info[2:]
    for line in info:
        line = line.strip()
        node = line[:3]
        path = line[6:]
        graph[node] = path

    looper = 0
    result = 0

    location = "AAA"
    while True:
        if looper == len(route): #loops the route
            looper = 0

        if route[looper] == "L":
            location = graph[location][1:4]
        else:
            location = graph[location][6:-1]

        result += 1
        looper += 1

        if location == "ZZZ":
            return result

def wasteland2(info): #Doesn't work, waaaay too slow
    info = info.split("\n")

    graph = {}
    route = info[0]

    info = info[2:]
    for line in info:
        line = line.strip()
        node = line[:3]
        path = line[6:]
        graph[node] = path

    looper = 0
    result = 0

    locations = {}
    enum = 0
    for key, value in graph.items():
        if key[2] == "A":
            locations[enum] = key
            enum += 1


    while True:
        if looper == len(route): #loops the route
            looper = 0


        for i in range(len(locations)):
            if route[looper] == "L":
                locations[i] = graph[locations[i]][1:4]
            else:
                locations[i] = graph[locations[i]][6:-1]

        result += 1
        looper += 1

        done = True
        for key, value in locations.items():
            if value[2] != "Z":
                done = False
                break
        if done:
            return result


if __name__ == "__main__":
    s =  """RL

        AAA = (BBB, CCC)
        BBB = (DDD, EEE)
        CCC = (ZZZ, GGG)
        DDD = (DDD, DDD)
        EEE = (EEE, EEE)
        GGG = (GGG, GGG)
        ZZZ = (ZZZ, ZZZ)"""
    #print(wasteland(s))


    s =  """LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)"""
    #print(wasteland(s))



    s =  """LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)"""
    #print(wasteland2(s))


    f = open("day8_input.txt")
    data = f.read().strip()
    #print(wasteland(data))
    #print(wasteland2(data))

