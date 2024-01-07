

def mirror(info):
    info = info.split("\n")
    
    maps = []
    temp = []
    for part in info: #get list of seperate maps
        part = part.strip()
        if part == "":
            maps.append(temp)
            temp = []
            continue
        temp.append(part)
    maps.append(temp)
    
    
    result = 0
    for map in maps: #test vertical mirrors
        vertic_mirrors = {x : True for x in range(1, len(map[0]))} #gaps indexed by how many symbols on left

        for i in range(len(map)): #loops lines
            for j in range(1, len(map[i])): #not optimized at all
                left = map[i][:j]
                right = map[i][j:]

                if len(left) == len(right):
                    continue
                elif len(left) < len(right):
                    right = right[:len(left)]
                else:
                    left = left[-len(right):]
                
                if left != right[::-1]:
                    vertic_mirrors[j] = False
        vertic_list = [index for index, bool in vertic_mirrors.items() if bool] #get mirrored gaps
        result += sum(vertic_list)

    for map in maps: #test horizontal mirrors
        horiz_mirrors = {x : True for x in range(1, len(map))} #gaps indexed by how many symbols on top

        for i in range(1, len(map)): # loops lines
            top = map[:i]
            bot = map[i:]

            if len(top) == len(bot):
                continue
            elif len(top) < len(bot):
                bot = bot[:len(top)]
            else:
                top = top[-len(bot):]
            

            if top != list(reversed(bot)):
                horiz_mirrors[i] = False
        horiz_list = [index for index, bool in horiz_mirrors.items() if bool]
        result += sum(horiz_list)*100
    
    return result



if __name__ == "__main__":
    s =  """#.##..##.
            ..#.##.#.
            ##......#
            ##......#
            ..#.##.#.
            ..##..##.
            #.#.##.#.

            #...##..#
            #....#..#
            ..##..###
            #####.##.
            #####.##.
            ..##..###
            #....#..#"""
    print(mirror(s)) #405
    #print(mirror2(s)) 


    f = open("day13_input.txt")
    data = f.read().strip()
    print(mirror(data)) 
    #print(mirror2(data)) 

