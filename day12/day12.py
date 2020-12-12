with open("input_day12.txt", "r") as myfile:
    input = myfile.read().split("\n")

def move(direction, value, d):
    if direction in ['N', 'E']:
        d[direction] += value
    elif direction in ['S', 'W']:
        d[direction] -= value
    return d

def change_facing(facing, value, dir):
    value = int(value/360*4)
    if dir == 'L':
        directions = ['N', 'W', 'S', 'E', 'N', 'W', 'S']
    else:
        directions = ['N', 'E', 'S', 'W', 'N', 'E', 'S']
    facing = directions[directions.index(facing)+value]
    return facing

def solve(input):
    facing = 'E'
    d = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    for direction in input:
        if direction[0] in ['N', 'S', 'E', 'W']:
            d = move(direction[0], int(direction[1:]), d)
        elif direction[0] == 'F':
            d = move(facing, int(direction[1:]), d)
        else:
            facing = change_facing(facing, int(direction[1:]), direction[0])
    return abs(d['N']+d['S']) + abs(d['E'] + d['W'])

print(solve(input))