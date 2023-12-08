with open("input.txt") as file:
    strings = file.readlines()

f = open("output_c.txt", "w")
for string in strings:
    appr_words = []
    for i in range(len(string.split())):
        if len(string.split()[i]) != 1:
            appr_words.append(string.split()[i])
    new_string = " ".join(appr_words)
    print(new_string, file = f)
f.close()