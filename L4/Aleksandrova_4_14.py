"""
Для заданого натурального числа n виведіть його найбільший дільник, 
відмінний від n.

Вхідні дані
Одне натуральне число n (1 < n < 2^31)

Вихідні дані
Виведіть найбільший дільник числа n, відмінний від n.

Приклад

Вхідні дані #1
21
Вихідні дані #1
7

Вхідні дані #2
97
Вихідні дані #2
1

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14595827
"""
n = int(input())
prime = True
i = 2
while i < int((n)**0.5) + 1:
	if n % i == 0:
		prime = False
		break
	else:
		i += 1
if prime == True:
	print(1)
else:                 
	for k in range(2, int((n)**0.5) + 1):
		if n % k == 0:
			b = n / k
			break
	print(int(b))


