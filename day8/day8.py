with open ("input_day8.txt", "r") as myfile:
    input=myfile.read().split("\n")

def solve(input):
    acc = 0
    i = 0
    it = []
    while i not in it:
        if input[i][:3] == "acc":
            it.append(i)
            if "+" in input[i]:
                acc += int(input[i].split("+")[1])
            else:
                acc -= int(input[i].split("-")[1])
            i += 1
        elif input[i][:3] == "jmp":
            it.append(i)
            if "+" in input[i]:
                i += int(input[i].split("+")[1])
            else:
                i -= int(input[i].split("-")[1])
        else:
            i += 1
    return acc

print(solve(input))