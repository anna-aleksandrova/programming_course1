with open("input.txt") as file:
    squares_of_odd = [int(el) for el in file.readlines() if int(el) > 0 and ((int(el))**0.5) % 2 == 1]
print(len(squares_of_odd))