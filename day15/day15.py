with open("input_day15.txt", "r") as myfile:
    input = myfile.read().split(",")

input = [int(i) for i in input]

def solve(input, n):
    spoken = {}
    for i in range(len(input)):
        spoken[input[i]] = [i+1]
    previous = input[len(input)-1]
    for i in range(len(input)+1, n+1):
        if len(spoken[previous]) < 2:
            previous = 0
            if 0 not in spoken:
                spoken[0] = [i]
            else:
                spoken[0].append(i)
                if len(spoken[0]) > 2 : spoken[0].pop(0)
        else:
            s = spoken[previous][1] - spoken[previous][0]
            previous = s
            if s not in spoken:
                spoken[s] = [i]
            else:
                spoken[s].append(i)
                if len(spoken[s]) > 2 : spoken[s].pop(0)
    return previous

print(solve(input, 30000000))