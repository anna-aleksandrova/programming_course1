with open("input.txt") as file:
    strings = file.readlines()
max_word = ""
for string in strings:
    for word in string.split():
        if len(word) > len(max_word):
            max_word = max_word.replace(max_word, word)
print(max_word)