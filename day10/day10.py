with open("input_day10.txt", "r") as myfile:
    input = myfile.read().split("\n")

input = [int(x) for x in input]
input = [0] + sorted(input)

def solve(input):
    d = {1:0, 2:0, 3:1}
    for i in range(len(input)-1):
        d[input[i+1]-input[i]] += 1
    return d[1] * d[3]

def solve2(input):
    res = 1
    previous = [1]
    for i in range(len(input)-2):
        if len(previous)<3:
            if input[i+2]-input[i] <= 3:
                res *= 2
                previous.append(res)
            else:
                previous = [previous[len(previous)-1]]
        else:
            if input[i + 2] - input[i] <= 3:
                res, previous = weird_seq(previous)
            else:
                previous = [previous[len(previous)-1]]
    return res

def weird_seq(lst):
    res = lst[0] + lst[1] + lst[2]
    lst2 = [lst[1], lst[2], res]
    return res, lst2

print(solve2(sorted(input)))