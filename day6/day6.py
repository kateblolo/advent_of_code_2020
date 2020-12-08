with open ("input_day6.txt", "r") as myfile:
    input=myfile.read().replace("\n", " ").split("  ")

#input = [i.replace(" ", "") for i in input] ##part1
input = [i.split(" ") for i in input] ##part2

def solve(input):
    res = 0
    for answers in input:
        res += len(''.join(set(answers)))
    return res

def solve2(input):
    res = 0
    for answers in input:
        if len(answers) == 1:
            res += len(set(answers[0]))
        else:
            s = set(answers[0])
            for i in range(len(answers)-1):
                s = s.intersection(answers[i+1])
            res += len(s)
    return res

#print(solve(input))
print(solve2(input))