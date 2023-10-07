"""
На вході програми маємо послідовність цілих чисел, що закінчується числом 0. Потрібно знайти суму даної послідовності, не враховуючи останнього нуля.

Вхідні дані
Послідовність цілих чисел, по одному числу в кожному рядку.

Вихідні дані
Одне число - суму даної послідовності.

Приклад
Вхідні дані #1
7
-1
4
-6
0

Вихідні дані #1
4

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14590177
"""
res_sum = 0
while True:
	n = int(input())
	res_sum += n 
	if n == 0:
		break
print(res_sum)