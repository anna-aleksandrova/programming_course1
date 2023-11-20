"""
Вхідні дані
Кожний рядок є окремим тестом та містить два цілих числа n та m 
(1 ≤ n, m ≤ 10^18). Кількість тестів не перевищує 1000.

Вихідні дані
Для кожного тесту в окремому рядку вивести значення F(НСД(n, m)), обчислене за модулем 10^8.

Приклад

Вхідні дані #1 
2 3
1 1
100 200

Вихідні дані #1 
1
1
61915075

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15206401
"""
import math

def matrix_product(A, B):
	a1, b1, c1, d1 = A
	a2, b2, c2, d2 = B

	return [
	a1 * a2 + b1 * c2,
	a1 * b2 + b1 *  d2,
	c1 * a2 + d1 * c2,
	c1 * b2 + d1 * d2]

def matrix_exp(A, m):
	if m == 0:
		return [1, 0, 0, 1]
	elif m == 1:
		return A
	else:
		B = A
		n = 2
		while n <= m:
			B = matrix_product(B, B)
			n = n * 2
		remainder = matrix_exp(A, m - n // 2)
		return matrix_product(B, remainder)

def fib(number):
	 F1 = [1, 1, 1, 0]
	 return matrix_exp(F1, number)[1]


with open("input.txt") as f:
    for line in f:
        n, m = [int(el) for el in line.split()]
        number = math.gcd(n, m)
        res = fib(number)
        print(res % (10 ** 8))