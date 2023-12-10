with open("input.txt") as file:
    even_numbers = [int(el) for el in file.readlines() if int(el) % 2 == 0]
print(len(even_numbers))