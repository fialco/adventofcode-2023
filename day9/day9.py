
def extrapolate(info):
    info = info.split("\n")

    result = []
    for line in info:
        line = line.strip()
        line = [int(x) for x in line.split()]
        cycler = line[:]


        seq = 0
        seq_dict = {}
        while True:
            
            seq_dict[seq] = []
            for i in range(1, len(cycler)):
                seq_dict[seq].append(cycler[i]-cycler[i-1])

            cycler = seq_dict[seq]
            if set(seq_dict[seq]) == {0}:
                break

            seq += 1
        
        next_value = 0
        seq_dict = dict(sorted(seq_dict.items(), reverse=True))
        for key, value in seq_dict.items():
            next_value = value[-1] + next_value
        
        result.append(line[-1] + next_value)
    
    return sum(result)

def extrapolate2(info):
    info = info.split("\n")

    result = []
    for line in info:
        line = line.strip()
        line = [int(x) for x in line.split()]
        cycler = line[:]


        seq = 0
        seq_dict = {}
        while True:
            
            seq_dict[seq] = []
            for i in range(1, len(cycler)):
                seq_dict[seq].append(cycler[i]-cycler[i-1])

            cycler = seq_dict[seq]
            if set(seq_dict[seq]) == {0}:
                break

            seq += 1
        
        next_value = 0
        seq_dict = dict(sorted(seq_dict.items(), reverse=True))
        for key, value in seq_dict.items():
            next_value = value[0] - next_value
        
        result.append(line[0] - next_value)
    
    return sum(result)


if __name__ == "__main__":
    s =  """0 3 6 9 12 15
            1 3 6 10 15 21
            10 13 16 21 30 45"""
    print(extrapolate(s)) #114
    print(extrapolate2(s)) #2


    f = open("day9_input.txt")
    data = f.read().strip()
    print(extrapolate(data)) #2043183816
    print(extrapolate2(data)) 

