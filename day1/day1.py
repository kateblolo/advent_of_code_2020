with open ("input.txt", "r") as myfile:
    input=myfile.read().replace("\n", " ").split()

input = [int(i) for i in input]
input = sorted(input, reverse=True)

def day1(input):
    for i in input:
        j = len(input) - 1
        while i + input[j] < 2020:
            j -= 1
        if i + input[j] == 2020 :
            return i * input[j]

print(day1(input))