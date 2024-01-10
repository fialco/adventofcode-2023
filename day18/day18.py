#https://www.tutorialspoint.com/How-to-convert-hex-string-into-int-in-Python

def calculate(dir, length, next_coord, area): #vector calculator

    next_coord += dir[0] * length
    area += dir[1] * length * next_coord + length / 2

    return next_coord, area

def lavaduct(info):
    dir_dict = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}

    info = info.split("\n")
    next_coord = 0
    area = 1

    for i in range(len(info)):
        info[i] = info[i].split()

        dir = dir_dict[info[i][0]]
        length = int(info[i][1])

        next_coord, area = calculate(dir, length, next_coord, area)
        
    return int(area)

def lavaduct2(info):
    dir_dict = {"3": (0,-1), "1": (0,1), "2": (-1,0), "0": (1,0)}

    info = info.split("\n")
    next_coord = 0
    area = 1

    for i in range(len(info)):
        info[i] = info[i].split()

        dir = dir_dict[info[i][2][7]]
        length = int(info[i][2][2:7], 16)

        next_coord, area = calculate(dir, length, next_coord, area)
        
    return int(area)

if __name__ == "__main__":
    s =  """R 6 (#70c710)
        D 5 (#0dc571)
        L 2 (#5713f0)
        D 2 (#d2c081)
        R 2 (#59c680)
        D 2 (#411b91)
        L 5 (#8ceee2)
        U 2 (#caa173)
        L 1 (#1b58a2)
        U 2 (#caa171)
        R 2 (#7807d2)
        U 3 (#a77fa3)
        L 2 (#015232)
        U 2 (#7a21e3)"""
    print(lavaduct(s)) #62
    print(lavaduct2(s)) #952408144115


    f = open("day18_input.txt")
    data = f.read().strip()
    print(lavaduct(data)) #40714
    print(lavaduct2(data)) #129849166997110