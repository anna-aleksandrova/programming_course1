"""
Знайти суму парних цифр натурального числа n.

Вхідні дані
Натуральне число n.

Вихідні дані
Сума парних цифр числа n або -1, якщо такі цифри відсутні.

Приклад
Вхідні дані #1
234
Вихідні дані #1
6

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14477922
"""
n = int(input())
suma = 0
suma_add = 0
while n > 0:
	last = n % 10
	if last % 2 == 0 and last != 0:
		suma += last
		suma_add += last
	elif last % 2 == 0 and last == 0:
		suma += last
		suma_add += 1
	else:
		pass
	n //= 10
if suma_add > 0:
	print(suma)
else:
	print("-1")