with open("input_day8.txt", "r") as myfile:
    input = myfile.read().split("\n")

def solve(input):
    acc = 0
    i = 0
    it = []
    while i not in it and i < len(input):
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
    if i == len(input):
        return acc, True
    else:
        return acc, False

def get_changed_input(input, last_changed):
    input2 = input[:]
    if last_changed == -1:
        for i in range(len(input)):
            if input[i][:3] == "nop":
                input2[i] = input[i].replace("nop", "jmp")
                last_changed = i
                break
            elif input[i][:3] == "jmp":
                input2[i] = input[i].replace("jmp", "nop")
                last_changed = i
                break

    else:
        if input[last_changed][:3] == "nop":
            input2[last_changed] = input[last_changed].replace("nop", "jmp")
        elif input[last_changed][:3] == "jmp":
            input2[last_changed] = input[last_changed].replace("jmp", "nop")
        for i in range(last_changed+1, len(input)):
            if input[i][:3] == "nop":
                input2[i] = input[i].replace("nop", "jmp")
                last_changed = i
                break
            elif input[i][:3] == "jmp":
                input2[i] = input[i].replace("jmp", "nop")
                last_changed = i
                break
    return input2, last_changed


def solve2(input):
    last_changed = -1
    acc, ended = solve(input)
    while not ended:
        input, last_changed = get_changed_input(input, last_changed)
        acc, ended = solve(input)
    return acc

# print(solve(input))
print(solve2(input))