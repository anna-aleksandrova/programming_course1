"""
Задано натуральне число n. Потрібно збільшити на 1 усі його парні цифри 
та зменшити на 1 усі його непарні цифри.

Приклад
Вхідні дані #1
983210
Вихідні дані #1
892301

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14481315
"""
import math
n = int(input())
suma = 0
numbers_amount = math.trunc((math.log10(n))) + 1
for i in range(1, numbers_amount + 1):
	first_digit = n // (10 ** (numbers_amount - i))
	if first_digit % 2 == 0:
		first_digit += 1
	else:
		first_digit -= 1
	suma = 10 * suma + first_digit
	n = n % (10 ** (numbers_amount - i))
print(suma)

