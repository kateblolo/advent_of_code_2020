with open ("input_day3.txt", "r") as myfile:
    input=myfile.read().split("\n")

def count_trees(input, right, down):
    input = input[down::down]
    len_line = len(input[0])
    trees = 0
    current_position = 0
    for i in input:
        current_position = (current_position + right) % len_line
        if i[current_position] == "#":
            trees += 1
    return trees

def multiply_slopes(input, lst_moves):
    trees = 1
    for i in lst_moves:
        trees *= count_trees(input, i[0], i[1])
    return trees

#print(count_trees(input, 3))
lst_moves = [(1, 1), (3, 1), (5,1), (7, 1), (1, 2)]
print(multiply_slopes(input, lst_moves))