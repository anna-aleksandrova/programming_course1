"""
Із заданого масиву цілих чисел потрібно видалити всі дублювання елементів. Тобто з декількох 
однакових елементів в масиві залишається тільки елемент з найменшим індексом.

Вхідні дані
В першому рядку записано число N. В наступному рядку записано N цілих чисел. Всі числа за модулем не перевищують 100.

Вихідні дані
Вивести елементи масиву без повторень в одному рядку через проміжок, не змінюючи початковий порядок.

Приклад

Вхідні дані #1 
7
0 1 -2 1 0 0 3

Вихідні дані #1
0 1 -2 3

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14692034

O(n) * O(n) = O(n^2)
"""
n = input()
lst1 = [int(el) for el in input().split()]
lst2 = []
for i in range(len(lst1)):
	el = lst1[i]
	if el not in lst2:
		lst2.append(el)
print(*lst2)

