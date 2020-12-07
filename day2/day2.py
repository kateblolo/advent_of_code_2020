with open ("input_day2.txt", "r") as myfile:
    input=myfile.read().split("\n")

def is_valid_pwd(line):
    line = line.split(":")
    rules, pwd = line[0], line[1].strip()
    rules = rules.split(" ")
    occurences, letter = rules[0], rules[1]
    occurences = occurences.split("-")
    min, max = int(occurences[0]), int(occurences[1])

    if pwd.count(letter) in range(min, max+1):
        return True
    return False

def is_valid_pwd2(line):
    line = line.split(":")
    rules, pwd = line[0], line[1].strip()
    rules = rules.split(" ")
    occurences, letter = rules[0], rules[1]
    occurences = occurences.split("-")
    pos1, pos2 = int(occurences[0])-1, int(occurences[1])-1

    if (pwd[pos1] == letter or pwd[pos2] == letter) and (pwd[pos1] != pwd[pos2]):
        return True
    return False

def day2(input):
    return sum([is_valid_pwd(i) for i in input])

def day2_part2(input):
    return sum([is_valid_pwd2(i) for i in input])

#print(day2(input))
print(day2_part2(input))