import re
from math import ceil
with open("input_day19.txt", "r") as myfile:
    input = myfile.read().split("\n\n")

rules = input[0].split("\n")
rules = {rules[i].split(":")[0]:rules[i].split(": ")[1].replace("\"", "").split() for i in range(len(rules))}
messages = input[1].split("\n")

def rule_to_regex(rules, key, max_len):
    regex = "("
    last_loop = False
    for r in rules[key]:
        if r == key and rules[key][len(rules[key])-1] == key:
            last_loop = True
            break
        elif r == key and rules[key][len(rules[key])-1] != key:
            regex = "("
            for i in range(1, ceil(max_len/2)+1):
                for r2 in rules[key]:
                    if r2 != "|":
                        for j in range(0, i):
                            regex += rule_to_regex(rules, r2, max_len)
                    else:
                        regex += "|"
                        break
            return regex[:-1] + ")"
        if r == "|":
            regex += "|"
        elif not r.isnumeric():
            return r
        else:
            regex += rule_to_regex(rules, r, max_len)
    regex += ")"
    if last_loop:
        regex += "+"
    return regex

def solve(rules, messages):
    max_len = max([len(m) for m in messages])
    p = rule_to_regex(rules, '0', max_len)
    print(len(p))
    pattern = re.compile("^" + p + "$")
    cpt = 0
    for m in messages:
        print("")
        if pattern.match(m): cpt+=1
    return cpt

print(solve(rules, messages))