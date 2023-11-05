"""
НСД та НСК
Задано два натуральних числа A та B. Знайти кількість таких пар чисел (P, Q), 
що для них A є НСД(P, Q), а B - НСК(P, Q).

Вхідні дані
У єдиному рядку два натуральних числа A та B (A < 105, B ≤ 106).

Вихідні дані
Єдине число - шукана кількість пар.

Приклад

Вхідні дані #1 
3 60
Вихідні дані #1 
4

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15008817
"""
import math

def gcd_and_lcm(A, B):

	if B % A != 0:
		print(0)
	elif A == B:
		print(1)
	else:
		interval = int((B - A) / math.gcd(A, B)) #довжина рівних відрізків між P i Q
		possible_P_and_Q = (el for el in range(A, B + 1, int((B - A) / interval)) if B % el == 0)
		lst = []
		for el in possible_P_and_Q:
			lst.append(el)

		lst_with_results = []
		for P in lst:
			for Q in lst:
				if math.gcd(P, Q) == A and (P * Q) / A == B:
					lst_with_results.append((P, Q))
		print(len(lst_with_results))


A, B = [int(el) for el in input().split()]
gcd_and_lcm(A, B)