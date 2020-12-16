with open("input_day16.txt", "r") as myfile:
    input = myfile.read().split("\n\n")

input = [i.split("\n") for i in input]

#combine ranges , e.g. 1 - 4 and 4 - 6 become 1 - 6
def optimise_ranges(ranges):
    ranges2 = ranges[:]
    for i in range(len(ranges)):
        for j in range(i):
            if ranges[i][0] in range(ranges2[j][0], ranges2[j][1]+1) and ranges[i][1] not in range(ranges2[j][0], ranges2[j][1]+1):
                ranges[i] = [ranges2[j][0], ranges[i][1]]
                ranges[j] = [0, 0]
            elif ranges[i][1] in range(ranges2[j][0], ranges2[j][1]+1) and ranges[i][0] not in range(ranges2[j][0], ranges2[j][1]+1):
                ranges[i] = [ranges[i][0], ranges2[j][1]]
                ranges[j] = [0, 0]
            elif ranges[i][0] < ranges2[j][0] and ranges[i][1] > ranges2[j][0]:
                ranges[j] = [0, 0]
    return list(filter(([0, 0]).__ne__, ranges))

#get all the different ranges
def get_valid_ranges(rules):
    ranges = []
    for r in rules:
        ran = r.split(": ")[1].split(" or ")
        r1 = ran[0].split("-")
        r2 = ran[1].split("-")
        ranges.append([int(r1[0]), int(r1[1])+1])
        ranges.append([int(r2[0]), int(r2[1])+1])
    print(ranges)
    ranges2 = optimise_ranges(ranges)
    print(ranges2)
    while ranges != ranges2:
        ranges = ranges2
        ranges2 = optimise_ranges(ranges)
        print(ranges2)
    return ranges2

#check if a ticket is valid
def is_valid_ticket(ranges, ticket):
    incorrect = []
    items = ticket.split(",")
    for i in items:
        valid = False
        for r in ranges:
            if int(i) in range(r[0], r[1]):
                valid = True
                break
        if valid == False:
            incorrect.append(int(i))
    return incorrect if incorrect else False


def solve(input):
    incorrects = []
    ranges = get_valid_ranges(input[0])
    for ticket in input[2][1:]:
        incorrect = is_valid_ticket(ranges, ticket)
        if incorrect:
            incorrects += incorrect
    return sum(incorrects)

print(solve(input))