with open("input_day13.txt", "r") as myfile:
    input = myfile.read().split("\n")

timestamp = int(input[0])
#buses = [int(i) for i in input[1].split(",") if i != "x"] #PART 1
buses = [i for i in input[1].split(",")] #PART2

def solve(timestamp, buses):
    init = timestamp
    while True:
        for b in buses:
            if float(timestamp/b).is_integer():
                return (timestamp - init)*b
        timestamp += 1

def group_id(timestamp, max_id, step):
    found = False
    while not found:
        if float((timestamp+max_id[1])/max_id[0]).is_integer():
            return timestamp, max_id[0]*step
        timestamp += step

def solve2(timestamp, buses):
    buses_id = [int(i) for i in buses if i != "x"]
    found = False
    step = 1
    while not found:
        max_id = [max(buses_id)]
        max_id.append(buses.index(str(max_id[0])))
        timestamp, step = group_id(timestamp, max_id, step)
        if len(buses_id) == 1:
            return timestamp
        buses_id.pop(buses_id.index(max_id[0]))


#print(solve(timestamp, buses))
print(solve2(timestamp, buses))