"""
Рядок складається з маленьких латинських літер, розділових знаків 
та проміжків. Подвійте в ньому всі латинські літери.

Вхідні дані
Один рядок, що складається з маленьких латинських літер, розділових знаків та проміжків.

Вихідні дані
Виведіть рядок з усіма подвоєними латинськими літерами.

Приклад

Вхідні дані #1
welcome to python!

Вихідні дані #1
wweellccoommee ttoo ppyytthhoonn!

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14802182

O(n)
"""
string = input()
for i in range(len(string)):
	if ord("a") <= ord(string[i]) <= ord("z"):
		el = 2 * string[i]
		print(el, end = "")
	else:
		el = string[i]
		print(el, end = "")