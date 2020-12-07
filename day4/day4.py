with open ("input_day4.txt", "r") as myfile:
    input=myfile.read().replace("\n", " ").split("  ")


def is_valid_passport(input):
    valid = 0
    for entry in input:
        e = [i[-3:] for i in entry.split(" ")[:-1]]
        if len(e) == 8:
            valid += 1
        elif len(e) == 7:
            if "cid" not in e:
                valid += 1
    return valid

def is_valid_passport2(input):
    valid = 0
    for entry in input:
        d = dict()
        e = entry.split(" ")
        for pair in e:
            p = pair.split(":")
            d[p[0]] = p[1]
        print(e)
        if len(e) == 8 or len(e) == 7 and "cid" not in d:
            if (
                int(d["byr"]) in range(1920, 2003)
                and int(d["iyr"]) in range(2010, 2021)
                and int(d["eyr"]) in range(2020, 2031)
                and d["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
                and len(d["pid"]) == 9
                and d["hcl"][0] == "#" and len(d["hcl"]) == 7 and all(c in "0123456789abcdef" for c in d["hcl"][1:])
            ):
                print("coucou")
                if d["hgt"][-2:] == "cm":
                    print("hgt cm coucou")
                    if int(d["hgt"][:-2]) in range(150, 194):
                        valid += 1
                elif d["hgt"][-2:] == "in":
                    if int(d["hgt"][:-2]) in range(59, 77):
                        valid += 1
    return valid

#print(is_valid_passport(input))
print(is_valid_passport2(input))