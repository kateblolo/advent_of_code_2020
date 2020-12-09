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


def get_invalid_number(input, preamble):
    for i in range(preamble, len(input)):
        if not is_sum_previous_numbers(input[i-preamble:i], input[i]):
            return input[i], i
    return False

def solve2(input):
    sum_numbers = []
    invalid_number, index = get_invalid_number(input, 25)
    for i in range(0,index):
        sum_numbers.append(input[i])
        while sum(sum_numbers) > invalid_number:
            sum_numbers.pop(0)
        if sum(sum_numbers) == invalid_number:
            return min(sum_numbers) + max(sum_numbers)

print(solve2(input))