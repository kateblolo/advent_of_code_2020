import itertools

with open("input_day14.txt", "r") as myfile:
    input = myfile.read().split("\n")

def write_in_memory(memory, loc, value, mask):
    res = ""
    value = format(value, '036b')
    for i in range(36):
        if mask[i] == "X":
            res += value[i]
        else:
            res += mask[i]
    memory[loc] = int(res, 2)
    return memory

def solve(input):
    mask = ""
    memory = {}
    for i in input:
        if i[:2] == "ma":
            mask = i[-36:]
        else:
            memory = write_in_memory(memory, int(i.split("[")[1].split("]")[0]), int(i.split("= ")[1]), mask)
    return sum(memory.values())

def write_in_memory2(memory, address, value, mask):
    bits = []
    ad = ""
    address = format(address, '036b')
    for i in range(36):
        if mask[i] == '0':
            ad += address[i]
        else:
            ad += mask[i]
    for i in range(1, len(ad)+1):
        if ad[i*-1] == "X":
            bits.append(2**(i-1))
    ad = ad.replace("X", "0")
    for i in range(0, len(bits) + 1):
        for j in itertools.combinations(bits, i):
            memory[int(ad, 2) + sum(j)] = value
    return memory

def solve2(input):
    mask = ""
    memory = {}
    for i in input:
        if i[:2] == "ma":
            mask = i[-36:]
        else:
            v = int(i.split("= ")[1])
            memory = write_in_memory2(memory, int(i.split("[")[1].split("]")[0]), v, mask)
    return sum(memory.values())

print(solve(input))
print(solve2(input))



