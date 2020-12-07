with open ("input_day3.txt", "r") as myfile:
    input=myfile.read().split("\n")

def count_trees(input, right):
    len_line = len(input[0])
    trees = 0
    current_position = 0
    for i in input[1:]:
        current_position = (current_position + right) % len_line
        if i[current_position] == "#":
            trees += 1
    return trees

print(count_trees(input, 3))