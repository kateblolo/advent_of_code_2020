with open("input_day12.txt", "r") as myfile:
    input = myfile.read().split("\n")

###PART1

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


### PART2

def move_waypoint(direction, value, d):
    if direction == 'N':
        d['N/S'] += value
    elif direction == 'S':
        d['N/S'] -= value
    if direction == 'E':
        d['E/W'] += value
    elif direction == 'W':
        d['E/W'] -= value
    return d

def move_ship(value, waypoint, ship):
    ship['N/S'] += waypoint['N/S'] * value
    ship['E/W'] += waypoint['E/W'] * value
    return ship

def switch_waypoint(waypoint, invert = True, opposite = []):
    if invert:
        temp = waypoint['N/S']
        waypoint['N/S'] = waypoint['E/W']
        waypoint['E/W'] = temp
    if opposite:
        for i in opposite:
            waypoint[i] *= -1
    return waypoint

def rotate_waypoint(waypoint, direction, value):
    value = int(value/360*4)
    if value == 3:
        value = 1
        direction = "R" if direction == "L" else "L"

    if value == 2:
        waypoint = switch_waypoint(waypoint, False, ['N/S', 'E/W'])
    elif value == 1 and direction == 'R':
        waypoint = switch_waypoint(waypoint, True, ['N/S'])
    elif value == 1 and direction == 'L':
        waypoint = switch_waypoint(waypoint, True, ['E/W'])
    return waypoint

def solve2(input):
    waypoint = {'N/S': 1, 'E/W':10}
    ship = {'N/S':0, 'E/W':0}
    for direction in input:
        if direction[0] in ['N', 'S', 'E', 'W']:
            waypoint = move_waypoint(direction[0], int(direction[1:]), waypoint)
        elif direction[0] == 'F':
            ship = move_ship(int(direction[1:]), waypoint, ship)
        else:
            waypoint = rotate_waypoint(waypoint, direction[0], int(direction[1:]))
    return abs(ship['N/S']) + abs(ship['E/W'])

print(solve2(input))