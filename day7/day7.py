with open ("input_day7.txt", "r") as myfile:
    input=myfile.read().split("\n")

dico = dict()
lst_bags = []
#removing numbers which are useless, removing commas, dots, splitting contains to get the object ( rule ) and the contenant ( information )
for bag in input:
    lst_bags.append(bag.split(" contain")[0].replace(" bags", ""))
    no_digits = ''.join([i for i in bag if not i.isdigit()])
    b = no_digits.split("contain")
    rule, information = b[0].strip().replace(" bags", ""), b[1].strip().replace(".", "").replace(" bags", "").replace(" bag", "").split(",  ")
    dico[rule] = information


print(lst_bags)
print(dico)

#['light lime', 'faded green', 'clear olive', 'dim bronze']
def is_shiny_bearer(bags, dico):
    if "shiny gold" in bags:
        return True
    else:
        for b in bags:
            if b in dico:
                if is_shiny_bearer(dico[b], dico):
                    return True
        return False

def solve(lst_bags, dico):
    res = 0
    for bag in lst_bags:
        if is_shiny_bearer(dico[bag], dico):
            res += 1
    return res

print(solve(lst_bags, dico))
