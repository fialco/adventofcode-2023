#holy jank batman!
def solver(schematic):
    nums = ["1","2","3","4","5","6","7","8","9","0"]

    schematic = schematic.split("\n")

    num_index = {}
    num_counter = 0

    sym_index = []

    part_nums = {}

    row_count = -1
    counter = ""
    for row in schematic:

        row_count += 1
        row = row.strip()

        for i in range(len(row)):
            if row[i] in nums:
                if num_counter not in num_index:
                    num_index[num_counter] = []

                num_index[num_counter].append((row_count, i))
                counter += row[i]

            elif counter != "":
                part_nums[num_counter] = int(counter)
                counter = ""
                num_counter += 1

            if row[i] != "." and row[i] not in nums:
                sym_index.append((row_count, i))
                if i != 0: #left
                    sym_index.append((row_count, i-1))
                if i != 0 and row != 0: #upleft
                    sym_index.append((row_count-1, i-1))
                if row != 0: #up
                    sym_index.append((row_count-1, i))
                if i != len(row)-1 and row != 0: #upright
                    sym_index.append((row_count-1, i+1))
                if i != len(row)-1: # right
                    sym_index.append((row_count, i+1))
                if i != len(row)-1 and row != len(schematic)-1: #dowright
                    sym_index.append((row_count+1, i+1))
                if row != len(schematic)-1: #down
                    sym_index.append((row_count+1, i))
                if i != 0 and row != len(schematic)-1: #downleft
                    sym_index.append((row_count+1, i-1))

    result = 0
    for num, coord in num_index.items():
        for i in coord:
            if i in sym_index:
                result += part_nums[num]
                break

    return result


#HOLY JANK BATMAN!
def solver2(schematic):
    nums = ["1","2","3","4","5","6","7","8","9","0"]

    schematic = schematic.split("\n")

    num_index = {}
    num_counter = 0

    check_index = []
    near_symbol = {}



    part_nums = {}

    row_count = -1
    counter = ""
    for row in schematic:
        row_count += 1
        row = row.strip()

        for i in range(len(row)):
            if row[i] in nums:
                if num_counter not in num_index:
                    num_index[num_counter] = []

                num_index[num_counter].append((row_count, i))
                counter += row[i]

            elif counter != "":
                part_nums[num_counter] = int(counter)
                counter = ""
                num_counter += 1

            if row[i] == "*" and row[i] not in nums:
                check_index.append((row_count, i))

                if (row_count, i) not in near_symbol:
                    near_symbol[(row_count, i)] = []


                if i != 0: #left
                    check_index.append((row_count, i-1))

                    near_symbol[(row_count, i)].append((row_count, i-1))
                if i != 0 and row != 0: #upleft
                    check_index.append((row_count-1, i-1))

                    near_symbol[(row_count, i)].append((row_count-1, i-1))
                if row != 0: #up
                    check_index.append((row_count-1, i))

                    near_symbol[(row_count, i)].append((row_count-1, i))
                if i != len(row)-1 and row != 0: #upright
                    check_index.append((row_count-1, i+1))

                    near_symbol[(row_count, i)].append((row_count-1, i+1))
                if i != len(row)-1: # right
                    check_index.append((row_count, i+1))

                    near_symbol[(row_count, i)].append((row_count, i+1))
                if i != len(row)-1 and row != len(schematic)-1: #dowright
                    check_index.append((row_count+1, i+1))

                    near_symbol[(row_count, i)].append((row_count+1, i+1))
                if row != len(schematic)-1: #down
                    check_index.append((row_count+1, i))

                    near_symbol[(row_count, i)].append((row_count+1, i))
                if i != 0 and row != len(schematic)-1: #downleft
                    check_index.append((row_count+1, i-1))

                    near_symbol[(row_count, i)].append((row_count+1, i-1))


    result_dict = []
    result = 0
    for num, coord in num_index.items():
        for i in coord:
            if i in check_index:

                result_dict.append((part_nums[num], i))

                break

    result = 0
    for sym, coord in near_symbol.items():
        total = 0

        adder = 1
        for i in coord:
            for j in result_dict:
                if i in j:
                    total += 1
                    adder *= j[0]
        if total == 2:
            result += adder

    return result



if __name__ == "__main__":
    s =  """467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598.."""
    print(solver(s))
    print(solver2(s))


    f = open("day3_input.txt")
    data = f.read().strip()
    print(solver(data))
    print(solver2(data))



