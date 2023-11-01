M = int(input("Введіть кількість рядків: "))
A = []
for i in range(M):
	row = map(float, input(f"Рядок {i}: ").split()) #вводиться i-тий рядок, елементи розділяються
	A.append(row)
lst_with_all_elements = []
for row in A:
	for elem in row:
		lst_with_all_elements.append(elem)
print(len(list(set(lst_with_all_elements))))