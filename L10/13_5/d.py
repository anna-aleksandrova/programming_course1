with open("input.txt") as file:
    numbers = [int(el) for el in file.readlines()]
max_length = 0
increasing_sequence = []
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        increasing_sequence.append(numbers[i])
        increasing_sequence.append(numbers[i + 1])
        if len(set(increasing_sequence)) > max_length:
            max_length = len(set(increasing_sequence))
    else:
        increasing_sequence = []
print(max_length)