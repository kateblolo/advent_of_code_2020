from math import floor, ceil

with open ("input_day5.txt", "r") as myfile:
    input=myfile.read().split("\n")

def dichot(code, max, lower_end):
    min = 0
    for i in range(0, len(code)-1):
        if code[i] == lower_end:
            max = min + floor((max - min)/2)
        else:
            min = min + ceil((max - min) / 2)
    if code[len(code)-1] == lower_end:
        res = min
    else:
        res = max
    return res

def solve(input):
    lst_res = []
    for code in input:
        row_code = code[:7]
        column_code = code[7:]
        row = dichot(row_code, 127, "F")
        column = dichot(column_code, 7, "L")
        lst_res.append(row * 8 + column)
    return max(lst_res)

print(solve(input))
