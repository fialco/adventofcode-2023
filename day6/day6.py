#pretty unoptimized implementation
def calculate(t, d):
    t = int(t)
    d = int(d)
    res = 0
    for i in range(1, int(t)):
        if (t - i) * i > d:
            res += 1
    return res


def wait(stats):
    stats = stats.split("\n")

    time = stats[0].strip().split()[1:]
    distance = stats[1].strip().split()[1:]

    result = 1
    for i in range(len(time)):
        result *= calculate(time[i], distance[i])

    return result

def wait2(stats):
    stats = stats.split("\n")

    time = stats[0].strip().split()[1:]
    distance = stats[1].strip().split()[1:]

    time = "".join(time)
    distance = "".join(distance)

    result = calculate(time, distance)

    return result

    
if __name__ == "__main__":
    s =  """Time:      7  15   30
        Distance:  9  40  200"""
    print(wait(s))
    print(wait2(s))

    f = open("day6_input.txt")
    data = f.read().strip()
    print(wait(data))
    print(wait2(data))

    