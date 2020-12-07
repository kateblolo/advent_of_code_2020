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

def day2(input):
    return sum([is_valid_pwd(i) for i in input])

print(day2(input))