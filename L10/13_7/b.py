with open("input.txt") as file:
    strings = file.readlines()
words_sum = 0
for string in strings:
    words_sum += len(string.split())
print(words_sum)