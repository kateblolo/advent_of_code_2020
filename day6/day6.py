with open ("input_day6.txt", "r") as myfile:
    input=myfile.read().replace("\n", " ").split("  ")

input = [i.replace(" ", "") for i in input]

def solve(input):
    res = 0
    for answers in input:
        res += len(''.join(set(answers)))
    return res

print(solve(input))