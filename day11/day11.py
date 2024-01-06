from itertools import combinations

def path(info):
    info = info.split("\n")

    
    empty_cols = {x : True for x in range(len(info[0]))}
    empty_rows = []

    galaxies = []

    for i in range(len(info)): #Checks for empty rows and columns
        line = info[i].strip()
        if set(line) == {"."}: #empty row
            empty_rows.append(i)
            continue

        for j in range(len(line)):
            if line[j] == "#": #non-empty column
                empty_cols[j] = False

    empty_rows.reverse()
    for i in empty_rows: #adds rows
        info.insert(i, "." * len(info[0]))
    
    col_list = [index for index, bool in empty_cols.items() if bool] #get empty col indexes
    col_list.reverse()
    
    for i in range(len(info)): #add columns
        row = info[i].strip()
        for col in col_list:
            row = row[:col] + "." + row[col:]
        info[i] = row
    

    for i in range(len(info)): #get galaxy coords
        for j in range(len(info[i])):
            if info[i][j] == "#":
                galaxies.append((j,i))

    result = 0
    combs = list(combinations(galaxies, 2)) #galaxy combinations
    for comb in combs:
        result += abs(comb[0][0] - comb[1][0]) + abs(comb[0][1] - comb[1][1])
    return result


def path2(info):
    info = info.split("\n")

    empty_cols = {x : True for x in range(len(info[0]))}
    empty_rows = []

    galaxies = []

    for i in range(len(info)): #Checks for empty rows and columns
        line = info[i].strip()
        if set(line) == {"."}: #empty row
            empty_rows.append(i)
            continue

        for j in range(len(line)):
            if line[j] == "#": #non-empty column
                empty_cols[j] = False

    col_list = [index for index, bool in empty_cols.items() if bool] #get empty col indexes

    row_mul = 0

    for i in range(len(info)): #get galaxy coords
        info[i] = info[i].strip()
        if i in empty_rows: #adds gaps to coords
            row_mul += 999999

        col_mul = 0
        for j in range(len(info[i])):
            if j in col_list: #adds gaps to coords
                col_mul += 999999

            if info[i][j] == "#":
                galaxies.append((j + col_mul, i + row_mul))

    result = 0
    combs = list(combinations(galaxies, 2)) #galaxy combinations
    for comb in combs:
        result += abs(comb[0][0] - comb[1][0]) + abs(comb[0][1] - comb[1][1]) #calc distances with Manhattan distance
    return result

if __name__ == "__main__":
    s =  """...#......
            .......#..
            #.........
            ..........
            ......#...
            .#........
            .........#
            ..........
            .......#..
            #...#....."""
    print(path(s)) #374
    print(path2(s)) 


    f = open("day11_input.txt")
    data = f.read().strip()
    #print(path(data)) 
    print(path2(data)) 

