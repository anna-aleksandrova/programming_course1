with open("input.txt") as file:
    symbols = file.readlines()[0]
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
appropriate_symbols = []
for symbol in symbols:
    if symbol in alphabet:
        appropriate_symbols.append(symbol)
    else:
        pass
am_strings_output = len(appropriate_symbols) // 40
if len(appropriate_symbols) % 40 != 0:
    am_strings_output += 1
else:
    pass
f = open("output.txt", "w")
for i in range(am_strings_output):
    string = "".join(appropriate_symbols[0:40])
    print(string, file = f)
    appropriate_symbols[0:40] = ""
f.close()