"""
Цікавий добуток

Визначити всі можливі значення добутку i*j, якщо цілочислові значення змінних
i та j змінюються відповідно від a до b та від c до d (1≤a,b,c,d≤10).

Вхідні дані
В одному рядку містяться 4 числа a, b, c та d (a може бути більшим за b,
с може бути більшим за d).

Вихідні дані
Виведіть кількість можливих варіантів добутку.

Приклад
Вхідні дані #1 content_copy
1 10 1 10
Вихідні дані #1 content_copy
42

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14749930

O(n^3)
"""
a, b, c, d = [int(el) for el in input().split()]
lst = []
if a > b:
	a, b = b, a
if c > d:
	c, d = d, c
for i in range(a, b + 1):
	for j in range(c, d + 1):
		el = i * j
		if lst.count(el) == 0:
			lst.append(el)
print(len(lst))