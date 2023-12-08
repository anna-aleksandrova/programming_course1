with open("input.txt") as file:
    strings = file.readlines()

f = open("output_e.txt", "w")
for string in strings:
    words = string.split()
    am_letters = len("".join(words))
    t = (80 - am_letters) // (len(words) - 1)
    if (80 - am_letters) % (len(words) - 1) == 0:
        string_formatted = (t*" ").join(words)
    else:
        remainder = (80 - am_letters) % (len(words) - 1)
        temp_wh = t + 1
        str_temp1 = (temp_wh*" ").join(words[0:remainder + 1])
        str_temp2 = (t * " ").join(words[remainder + 1:len(words)])
        string_formatted = str_temp1 + t * " " + str_temp2
    print(string_formatted, file = f)
f.close()

