"""
Нагадаємо, що паліндромом називається рядок, який однаково читається з обох сторін. 
Наприклад, рядок abba є паліндромом, а рядок abc - ні. 

Необхідно визначити, у яких системах числення з основою від 2 до 36 подання цього числа є паліндромом.

У системах числення з основою більше 10 у якості цифр використовуються літери 
латинського алфавіту: a, b, ..., z. Наприклад, a11 = 1010, z36 = 3510.

Вхідні дані
Вхідний файл містить ціле число n, задане у десятковій системі числення (1 ≤ n ≤ 109).

Вихідні дані
Якщо відповідна основа системи числення визначається єдиним чином, то виведіть у першому 
рядку вихідного файлу слово unique, якщо ж вона не єдина - виведіть у першому рядку 
вихідного файлу слово multiple. Якщо ж такої основи системи числення не існує - виведіть 
у першому рядку вихідного файлу слово none.

У випадку існування хоча б однієї потрібної основи системи числення виведіть через пропуск 
у зростаючому порядку у другому рядку усі основи систем числення, які задовільняють вимогам.

Приклад

Вхідні дані #1 
123
Вихідні дані #1 
unique
6

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15003116
"""
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

def from_decimal_to_k(n, k):

	lst_with_remainders = []
	while n >= k:
		lst_with_remainders.append(n % k)
		n //= k
	lst_with_remainders.append(n)

	for numb in range(10, 26):                                         #заміна 10, 11, ..., 25 відповідними a, b, ..., z
		if numb in lst_with_remainders:
			for el in range(len(lst_with_remainders)):
				if lst_with_remainders[el] == numb:
					lst_with_remainders[el] = alphabet[numb]
				else:
					pass
		else:
			pass

	lst_with_remainders = list(map(str, lst_with_remainders))
	lst_with_remainders_reversed = list(map(str, lst_with_remainders[::-1]))

	elements_of_lists_are_equal = True
	for i in range(len(lst_with_remainders)):
		if lst_with_remainders[i] != lst_with_remainders_reversed[i]:
			elements_of_lists_are_equal = False

	if elements_of_lists_are_equal:
		return k 
	else:
		pass

n = int(input())
bases = []
for k in range(2, 37):
	if from_decimal_to_k(n, k) == k:
		bases.append(from_decimal_to_k(n, k))

if len(bases) == 0:
	print("none")
elif len(bases) == 1:
	print("unique")
	print(*bases)
elif len(bases) > 1:
	print("multiple")
	print(*bases)