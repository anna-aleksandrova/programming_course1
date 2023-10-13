"""
Знайти кількість двозначних чисел, які не змінюють свою суму 
цифр при множені числа на однозначне ціле число n (n = 0 .. 9).

Вхідні дані
Ціле число n (0 ≤ n ≤ 9).

Вихідні дані
Вивести шукану кількість двозначних чисел.

Приклад
Вхідні дані #1 
2

Вихідні дані #1 
10

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14594694
"""

n = int(input())
counter = 0
a = 10
while a < 100:
	res_sum_2 = 0
	k = a
	k1 = n*a
	last1 = k % 10
	last2 = k // 10
	res_sum_1 = last1 + last2
	while k1 > 0:
		last = k1 % 10
		res_sum_2 += last
		k1 = k1 // 10
	if res_sum_1 == res_sum_2:
		counter += 1
	a += 1
print(counter)