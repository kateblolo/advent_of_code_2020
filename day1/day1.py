with open ("input.txt", "r") as myfile:
    input=myfile.read().replace("\n", " ").split()

input = [int(i) for i in input]
input = sorted(input, reverse=True)

def day1(input):
    for i in range(len(input)):
        j = len(input) - 1
        while input[i] + input[j] < 2020 and j > i:
            j -= 1
        if input[i] + input[j] == 2020 :
            return input[i] * input[j]

print(day1(input))

def day1_part2(input):
    for i in range(len(input)):
        j = len(input) - 1
        while input[i] + input[j] < 2020 and j > i:
            if j-i > 1:
                for k in range(j-1, i, -1):
                    if input[i] + input[j] + input[k] > 2020:
                        break
                    elif input[i] + input[j] + input[k] == 2020:
                        return input[i] * input[j] * input[k]
            j -= 1

print(day1_part2(input))