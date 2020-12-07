with open ("input_day4.txt", "r") as myfile:
    input=myfile.read().replace("\n", " ").split("  ")


def is_valid_passport(input):
    valid = 0
    for entry in input:
        e = [i[-3:] for i in entry.split(":")[:-1]]
        if len(e) == 8:
            valid += 1
        elif len(e) == 7:
            if "cid" not in e:
                valid += 1
    return valid

print(is_valid_passport(input))