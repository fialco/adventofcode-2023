
def tilt(info):
    info = info.split("\n")

    for i in range(len(info)):
        info[i] = info[i].strip()

        for j in range(len(info[i])):
            if info[i][j] == "O":
                rock_coord = (i,j) #coord for moved rock
                while True: #Moves rock northbound until it can't
                    if rock_coord[0] == 0:
                        break
                    elif info[rock_coord[0]-1][rock_coord[1]] == ".":

                        new_row = [*info[rock_coord[0]-1]]
                        old_row = [*info[rock_coord[0]]]

                        new_row[rock_coord[1]] = "O"
                        old_row[rock_coord[1]] = "."
                        
                        new_row = "".join(new_row)
                        old_row = "".join(old_row)
                        info[rock_coord[0]-1] = new_row
                        info[rock_coord[0]] = old_row

                        rock_coord = (rock_coord[0]-1, rock_coord[1])
                    else:
                        break
                    
    result = 0
    multiplier = len(info)
    for line in info:
        result += line.count("O") * multiplier
        multiplier -= 1
    return result
    


if __name__ == "__main__":
    s =  """O....#....
            O.OO#....#
            .....##...
            OO.#O....O
            .O.....O#.
            O.#..O.#.#
            ..O..#O..O
            .......O..
            #....###..
            #OO..#...."""
    print(tilt(s)) #136
    #print(tilt2(s)) 


    f = open("day14_input.txt")
    data = f.read().strip()
    print(tilt(data)) 
    #print(tilt2(data)) 

