with open("input_day9.txt", "r") as myfile:
    input = myfile.read().split("\n")

input = [int(i) for i in input]

def is_sum_previous_numbers(input, nb):
    input = sorted(input, reverse=True)
    for i in range(len(input)):
        j = len(input) - 1
        while input[i] + input[j] < nb and j > i:
            j -= 1
        if input[i] + input[j] == nb :
            return True
    return False


def solve(input, preamble):
    for i in range(preamble, len(input)):
        if not is_sum_previous_numbers(input[i-preamble:i], input[i]):
            return input[i]
    return False

print(solve(input, 25))