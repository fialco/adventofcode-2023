
def library(info): #pt1
    info = info.split(",")
    result = []
    for command in info:
        total = 0
        for character in command:
            total += ord(character)
            total *= 17
            total %= 256
        result.append(total)
    return sum(result)

def hashmap(info):
    result = []
    label = ""
    lens = 0
    total = 0

    for i in range(len(info)):
                
        if info[i] == "-":
            inst = "-"
            break

        elif info[i] == "=":
            inst = "="
            lens = int(info[i+1])
            info[i] == "="
            break

        else:
            label += info[i]

            total += ord(info[i])
            total *= 17
            total %= 256 
    result.append(total)

    return sum(result), label, inst, lens


def library2(info): #pt2
    info = info.split(",")
    result = []

    boxes = {x : [] for x in range(256)}
    labels = {}

    for command in info:
        box, label, instruction, lens = hashmap(command)

        if instruction == "-":
            if label in labels:
                boxes[box].remove(label)
                del labels[label] 

        elif instruction == "=":
            labels[label] = lens
            if label not in boxes[box]:
                boxes[box].append(label)
   
    for box, slots in boxes.items():
        for i in range(len(slots)):
            result.append((1+box) * (i+1) * labels[slots[i]])
    return sum(result)


if __name__ == "__main__":
    s =  """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    #print(library(s)) #1320
    print(library2(s)) #145


    f = open("day15_input.txt")
    data = f.read().strip()
    #print(library(data)) #516469
    print(library2(data)) #221627

