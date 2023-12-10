with open("input.txt") as file:
    lines = file.readlines()
try:
    even_numbers = [int(el) for el in lines if int(el) % 2 == 0]
    odd_numbers = [int(el) for el in lines if int(el) % 2 == 1]
    print(max(even_numbers) - min(odd_numbers))
except ValueError:
    if len(odd_numbers) == 0:
        print("Немає непарних чисел.")
    if len(even_numbers) == 0:
        print("Немає парних чисел.")
