# перший елемент матриці = a11
M = int(input("Введіть кількість рядків: "))
A = []
for i in range(M):
	row = map(float, input(f"Рядок {i + 1}: ").split()) #вводиться i-тий рядок, елементи розділяються
	A.append(row)
lst_of_results = []
for i, row in enumerate(A):
	for j, elem in enumerate(row):
		if elem != 0:
			index_of_non_zero_elem = (i + 1, j + 1)
			lst_of_results.append(index_of_non_zero_elem)
print(*lst_of_results)