with open("input.txt") as file:
    strings = file.readlines()

f = open("output_d.txt", "w")
for string in strings:
    new_string = " ".join(string.split())
    print(new_string, file = f)
f.close()