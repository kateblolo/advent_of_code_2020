with open("input_day18.txt", "r") as myfile:
    input = myfile.read().split("\n")


# PART2 -- adds parenthesis around "+" elements
def add_priority(line):
    line2 = line[:]
    appended = 0
    nxt_app = []
    for c in range(len(line)):
        if nxt_app:
            if c+appended == min(nxt_app):
                appended += 1
                nxt_app.remove(min(nxt_app))
        if line[c] == "+":
            cpt = 0
            c2 = c-1+appended
            while not line2[c2].isnumeric() or cpt != 0:
                if line2[c2] == ")":
                    cpt += 1
                elif line2[c2] == "(":
                    cpt -=1
                    if cpt == 0:
                        break
                c2 -= 1
            line2 = line2[:c2] + "(" + line2[c2:]
            appended += 1
            c2 = c+1+appended
            while not line2[c2].isnumeric() or cpt != 0:
                if line2[c2] == "(":
                    cpt += 1
                elif line2[c2] == ")":
                    cpt -=1
                    if cpt == 0:
                        break
                c2 += 1
            line2 = line2[:c2+1] + ")" + line2[c2+1:]
            nxt_app = [i+2 for i in nxt_app]
            nxt_app.append(c2+1)
    return line2


def solve_line(line):
    line = line.replace(" ", "")
    ##PART2 v
    line = add_priority(line)
    ##PART2 ^
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