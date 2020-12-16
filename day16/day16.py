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
    ranges2 = optimise_ranges(ranges)
    while ranges != ranges2:
        ranges = ranges2
        ranges2 = optimise_ranges(ranges)
    return ranges2

#check if a ticket is valid
def is_invalid_ticket(ranges, ticket):
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
        incorrect = is_invalid_ticket(ranges, ticket)
        if incorrect:
            incorrects += incorrect
    return sum(incorrects)


######################################################PART2

def remove_invalid_tickets(input):
    ranges = get_valid_ranges(input[0])
    nb_removed = 0
    for i in range(1,len(input[2])):
        if is_invalid_ticket(ranges, input[2][i-nb_removed]):
            input[2].pop(i-nb_removed)
            nb_removed += 1
    return input[2][1:]

def get_ranges2(rules):
    ranges = {}
    for r in rules:
        name = r.split(": ")[0]
        ran = r.split(": ")[1].split(" or ")
        r1 = ran[0].split("-")
        r2 = ran[1].split("-")
        ranges[name] = []
        ranges[name].append(([int(r1[0]), int(r1[1])+1]))
        ranges[name].append(([int(r2[0]), int(r2[1])+1]))
    return ranges

def valid_fields(ranges, entry):
    vf = []
    fields = ranges.keys()
    for f in fields:
        for r in ranges[f]:
            if entry in range(r[0], r[1]):
                vf.append(f)
                break
    return vf

def remove_duplicate(pf, len_pf, fields):
    removed = []
    counter = {f:0 for f in fields}
    incorrect = True
    while incorrect:
        for f in fields:
            for i in range(len_pf):
                if f in pf[i] and len(pf[i]) == 1:
                    for j in range(len_pf):
                        if j != i and f in pf[j]:
                            pf[j].remove(f)
                            removed.append(f)
                    break
                elif f in pf[i]:
                    counter[f] += 1
            if counter[f] == 1:
                for i in range(len_pf):
                    if f in pf[i]:
                        pf[i] = [f]
                        break
        incorrect = False
        for i in range(len_pf):
            if len(pf[i]) != 1:
                incorrect = True
                break
    return pf

def det_fields(ranges, tickets):
    fields = ranges.keys()
    possible_fields = {i: fields for i in range(0,len(fields))}
    for ticket in tickets:
        ticket = ticket.split(",")
        for i in range(len(ticket)):
            possible_fields[i] = list(set(possible_fields[i]) & set(valid_fields(ranges, int(ticket[i]))))
    return remove_duplicate(possible_fields, len(fields), fields)

def get_product_departure(fields, ticket):
    res = 1
    ticket = ticket.split(",")
    keys = fields.keys()
    for f in keys:
        if 'departure' in fields[f][0]:
            res *= int(ticket[f])
    return res


def solve2(input):
    tickets = remove_invalid_tickets(input)
    ranges = get_ranges2(input[0])
    fields = det_fields(ranges, tickets)
    return get_product_departure(fields, input[1][1])

#print(solve(input))
print(solve2(input))