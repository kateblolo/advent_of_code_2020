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


def should_be_replaced2(x, y, input):
    char = input[y][x]
    surroundings = []
    #left
    left = [x-1, y]
    while left[0] >= 0:
        if input[left[1]][left[0]] != "." :
            surroundings.append(input[left[1]][left[0]])
            break
        left[0] -= 1
    #right
    right = [x+1,y]
    while right[0] < len(input[0]):
        if input[right[1]][right[0]] != "." :
            surroundings.append(input[right[1]][right[0]])
            break
        right[0] += 1
    #up
    up = [x,y-1]
    while up[1] >= 0:
        if input[up[1]][up[0]] != "." :
            surroundings.append(input[up[1]][up[0]])
            break
        up[1] -= 1
    down = [x, y+1]
    while down[1] < len(input):
        if input[down[1]][down[0]] != "." :
            surroundings.append(input[down[1]][down[0]])
            break
        down[1] += 1
    #first diagonal
    diag1 = [x-1, y-1]
    while diag1[0] >= 0 and diag1[1] >= 0:
        if input[diag1[1]][diag1[0]] != ".":
            surroundings.append(input[diag1[1]][diag1[0]])
            break
        diag1[0] -= 1
        diag1[1] -= 1
    diag1 = [x+1, y+1]
    while diag1[0] < len(input[0]) and diag1[1] < len(input):
        if input[diag1[1]][diag1[0]] != ".":
            surroundings.append(input[diag1[1]][diag1[0]])
            break
        diag1[0] += 1
        diag1[1] += 1
    #second diagonal
    diag2 = [x+1, y-1]
    while diag2[0] < len(input[0]) and diag2[1] >= 0:
        if input[diag2[1]][diag2[0]] != ".":
            surroundings.append(input[diag2[1]][diag2[0]])
            break
        diag2[0] += 1
        diag2[1] -= 1
    diag2 = [x-1, y+1]
    while diag2[0] >= 0 and diag2[1] < len(input):
        if input[diag2[1]][diag2[0]] != ".":
            surroundings.append(input[diag2[1]][diag2[0]])
            break
        diag2[0] += 1
        diag2[1] += 1

    if char == "#":
        if surroundings.count('#') >= 5:
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

def replace_input(input, part):
    to_replace = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if part == 1:
                if should_be_replaced(x, y, input):
                    to_replace.append((x, y))
            elif part == 2:
                if should_be_replaced2(x, y, input):
                    to_replace.append((x, y))
    return replace_seats(to_replace, input)

def solve(input, part):
    input2 = replace_input(input, part)
    while input2 != input:
        input = input2
        input2 = replace_input(input, part)
    for i in input2:
        input2 = [seat for rows in input2 for seat in rows]
    return input2.count("#")

print(solve(input, 1))
print(solve(input, 2))