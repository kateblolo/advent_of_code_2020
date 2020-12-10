with open("input_day10.txt", "r") as myfile:
    input = myfile.read().split("\n")

input = [int(x) for x in input]
input = [0] + sorted(input)
print(input)

def solve(input):
    d = {1:0, 2:0, 3:1}
    for i in range(len(input)-1):
        d[input[i+1]-input[i]] += 1
    return d[1] * d[3]

print(solve(input))