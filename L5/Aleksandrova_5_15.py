"""
Дано масив з n цілих чисел. Замінити всі найбільші елементи на 
найменший, а найменші елементи на найбільший.

Вхідні дані
В першому рядку записано число n (n ≤ 100). В наступному рядку записано 
n цілих чисел, кожне з яких за модулем не перевищує 100.

Вихідні дані
Вивести оновлений масив.

Приклад

Вхідні дані #1 
7
3 5 -7 7 5 -9 -4

Вихідні дані #1 
3 5 -7 -9 5 7 -4

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14751727
O(n) + O(n) = O(n)
"""
n = int(input())
lst = [int(el) for el in input().split()]
min_el = lst[0]
max_el = lst[0]

for i in range(len(lst)):
	if lst[i] < min_el:
		min_el = lst[i]
	if lst[i] > max_el:
		max_el = lst[i]

for i in range(len(lst)):
	if lst[i] == min_el:
		lst[i] = max_el
	elif lst[i] == max_el:
		lst[i] = min_el
	else:
		pass
		
print(*lst)