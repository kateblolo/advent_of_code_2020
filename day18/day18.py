with open("input_day18.txt", "r") as myfile:
    input = myfile.read().split("\n")


def solve_line(line):
    print(line)
    line = line.replace(" ", "")
    res = [0]
    cpt = 0
    operation = ["+"]
    for i in range(len(line)):
        if line[i] == "(":
            cpt += 1
            res.append(0)
            operation.append("+")
        elif line[i] == ")":
            cpt -= 1
            if operation[cpt] == "+":
                res[cpt] += res[cpt+1]
            else:
                res[cpt] *= res[cpt+1]
            res = res[:cpt+1]
            operation = operation[:cpt+1]
        elif line[i] == "+":
            operation[cpt] = "+"
        elif line[i] == "*":
            operation[cpt] = "*"
        elif line[i].isnumeric():
            if operation[cpt] == "+": res[cpt] += int(line[i])
            else: res[cpt] *= int(line[i])
    return res[0]


def solve(input):
    res = 0
    for i in input:
        res += solve_line(i)
    return res

print(solve(input))