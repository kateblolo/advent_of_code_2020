import copy
import numpy as np
with open("input_day17.txt", "r") as myfile:
    grid = myfile.read().split("\n")

def split(word):
    return [0 if char == '.' else 1 for char in word]

grid = [split(line) for line in grid]
#input = [grid] #PART1
input = [[grid]] #PART2

def add_inactive_extremities(input):
    line = [0 for i in range(len(input[0][0]))]
    grid = [line[:] for i in range(len(input[0]))]
    input.insert(0, copy.deepcopy(grid))
    input.append(copy.deepcopy(grid))
    for g in input:
        g.insert(0, line[:])
        g.append(line[:])
        for l in g:
            l.insert(0, 0)
            l.append(0)
    return input

def add_inactive_extremities2(input):
    line = [0 for i in range(len(input[0][0][0]))]
    grid = [line[:] for i in range(len(input[0][0]))]
    w_dim = [copy.deepcopy(grid) for i in range(len(input[0]))]
    input.insert(0, copy.deepcopy(w_dim))
    input.append(copy.deepcopy(w_dim))

    for gds in input:
        gds.insert(0, copy.deepcopy(grid))
        gds.append(copy.deepcopy(grid))
        for g in gds:
            g.insert(0, line[:])
            g.append(line[:])
            for l in g:
                l.insert(0, 0)
                l.append(0)
    return input


def sum_surroundings(input, z, y, x, maxz, maxy, maxx):
    minz = 0 if z-1 < 0 else z-1
    miny = 0 if y-1 < 0 else y-1
    minx = 0 if x-1 < 0 else x-1
    maxz = z+1 if z+1 < maxz else maxz-1
    maxy = y+1 if y+1 < maxy else maxy-1
    maxx = x+1 if x+1 < maxx else maxx-1


    res = 0
    for z2 in range(minz, maxz+1):
        for y2 in range(miny, maxy+1):
            for x2 in range(minx, maxx+1):
                if not (z2 == z and y2 == y and x2 == x):
                    res += input[z2][y2][x2]
    return res

def sum_surroundings2(input, w, z, y, x, maxw, maxz, maxy, maxx):
    minz = 0 if z-1 < 0 else z-1
    miny = 0 if y-1 < 0 else y-1
    minx = 0 if x-1 < 0 else x-1
    minw = 0 if w-1 < 0 else w-1
    maxz = z+1 if z+1 < maxz else maxz-1
    maxy = y+1 if y+1 < maxy else maxy-1
    maxx = x+1 if x+1 < maxx else maxx-1
    maxw = w+1 if w+1 < maxw else maxw-1

    res = 0
    for w2 in range(minw, maxw+1):
        for z2 in range(minz, maxz+1):
            for y2 in range(miny, maxy+1):
                for x2 in range(minx, maxx+1):
                    if not (w2 == w and z2 == z and y2 == y and x2 == x):
                        res += input[w2][z2][y2][x2]
    return res


def replace_cubes(input):
    input = add_inactive_extremities(input)
    input2 = copy.deepcopy(input)
    for z in range(len(input)):
        for y in range(len(input[z])):
            for x in range(len(input[z][y])):
                if input[z][y][x] == 0:
                    if sum_surroundings(input, z, y, x, len(input), len(input[z]), len(input[z][y])) == 3:
                        input2[z][y][x] = 1
                else:
                    if sum_surroundings(input, z, y, x, len(input), len(input[z]), len(input[z][y])) not in [2, 3]:
                        input2[z][y][x] = 0
    return input2

def replace_cubes2(input):
    input = add_inactive_extremities2(input)
    input2 = copy.deepcopy(input)
    for w in range(len(input)):
        for z in range(len(input[w])):
            for y in range(len(input[w][z])):
                for x in range(len(input[w][z][y])):
                    if input[w][z][y][x] == 0:
                        if sum_surroundings2(input, w, z, y, x, len(input), len(input[w]), len(input[w][z]), len(input[w][z][y])) == 3:
                            input2[w][z][y][x] = 1
                    else:
                        if sum_surroundings2(input, w, z, y, x, len(input), len(input[w]), len(input[w][z]), len(input[w][z][y])) not in [2, 3]:
                            input2[w][z][y][x] = 0
    return input2


def nb_cubes(input):
    c = 0
    for g in input:
        for l in g:
            c += sum(l)
    return c

def nb_cubes2(input):
    c = 0
    for w in input:
        for gds in w:
            for l in gds:
                c += sum(l)
    return c


def solve(input, n):
    for i in range(n):
        input = replace_cubes(input)
    return nb_cubes(input)

def solve2(input, n):
    for i in range(n):
        input = replace_cubes2(input)
    return nb_cubes2(input)

#print(solve(input, 6))
print(solve2(input, 6))