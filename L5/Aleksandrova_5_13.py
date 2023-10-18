"""
Задано послідовність дійсних чисел. Визначити середнє арифметичне додатних чисел.

Вхідні дані
У першому рядку задано кількість чисел n (0 < n ≤ 100). У наступному рядку задано 
n дійсних чисел, значення яких не перевищують за модулем 100.

Вихідні дані
Вивести середнє арифметичне додатних чисел з 2 десятковими знаками. У випадку 
відсутності додатних чисел вивести повідомлення "Not Found" (без лапок).

Приклад

Вхідні дані #1 
3
5.2 -2 4
Вихідні дані #1 
4.60

Вхідні дані #2 
3
-5.2 -2 -4
Вихідні дані #2 
Not Found

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14751282

O(n) + O(n) = O(n)
"""
n = int(input())
lst = [float(el) for el in input().split()]
positive_numbers = []
suma = 0
for i in range(len(lst)):
	if lst[i] > 0:
		positive_numbers.append(lst[i])
	else:
		pass
if positive_numbers != []:
	for i in range(len(positive_numbers)):
		suma += positive_numbers[i]
	average = suma / len(positive_numbers)
	print(format(average, ".2f"))
else:
	print("Not Found")
