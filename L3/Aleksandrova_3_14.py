"""
Знайти кількість цифр у запису факторіалу натурального числа n. (Факторіал числа n – це добуток усіх натуральних чисел від 1 до n)

Вхідні дані
Одне число n (1 ≤ n ≤ 1000000).

Вихідні дані
Вивести кількість цифр у числі n!.

Приклад
Вхідні дані #1
7
Вихідні дані #1
4

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14483971
"""
import math
n = int(input())
k = 1
fact = 1
for i in range(1, n+1):
	fact = fact * k
	k += 1
number_amount = int(math.log10(fact)) + 1
print(number_amount)