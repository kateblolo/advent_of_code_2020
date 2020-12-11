with open("input_day11.txt", "r") as myfile:
    input = myfile.read().split("\n")

def should_be_replaced(x, y, input):
    char = input[y][x]
    surroundings = []
    for j in range(-1,2):
        for i in range(-1, 2):
            if not (i == 0 and j == 0) and y+j >= 0 and y+j < len(input) and x+i >= 0 and x+i < len(input[0]):
                if input[y + j][x + i] != ".":
                    surroundings.append(input[y+j][x+i])
    if char == "#":
        if surroundings.count('#') >= 4:
            return True
    if char == "L":
        if surroundings.count("#") == 0:
            return True
    return False

def replace_seats(lst, input):
    input2 = input[:]
    for seats in lst:
        x = seats[0]
        y = seats[1]
        if input[y][x] == "#":
            input2[y] = input2[y][:x] + "L" + input2[y][x+1:]
        else:
            input2[y] = input2[y][:x] + "#" + input2[y][x+1:]
    return input2

def replace_input(input):
    to_replace = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if should_be_replaced(x, y, input):
                to_replace.append((x, y))
    return replace_seats(to_replace, input)

def solve(input):
    input2 = replace_input(input)
    while input2 != input:
        input = input2
        input2 = replace_input(input)
    for i in input2:
        input2 = [seat for rows in input2 for seat in rows]
    return input2.count("#")

print(solve(input))

