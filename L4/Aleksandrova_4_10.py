"""
Вивести відповідь до задачі, враховуючи, що n — номер варіанту.

n=1 : Обчислити суму трьохзначних чисел, цифри яких парні.

n=2 : Обчислити кількість трьохзначних чисел, цифри яких зростають.

n=3 : Обчислити суму трьохзначних чисел, цифри яких непарні.

n=4 : Обчислити кількість трьохзначних чисел, цифри яких спадають.

n=5 : Обчислити суму трьохзначних чисел, які дорівнюють сумі кубів своїх цифр.

n=6 : Обчислити кількість трьохзначних чисел, цифри яких різні.

Вхідні дані
Одне число n, 1 ≤ n ≤ 6

Вихідні дані
Відповідь до задачі, залежно від номеру варіанту n.

Приклад
Вхідні дані #1 
1
Вихідні дані #1 
54400

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14590076
"""
n = int(input())
if n == 1:
	a = 100
	res_sum = 0
	count_add = 0
	while a < 1000:
		n = a 
		for i in range(3):
			last = n % 10
			if last % 2 != 0:
				count_add = 0
				break
			else:
				count_add += 1
				n = n // 10
		if count_add > 0:
			res_sum += a
		a += 1
		count_add = 0
	print(res_sum)
elif n == 2:
	a = 100
	counter = 0
	while a < 1000:
		n = a
		last1 = n % 10
		n //= 10
		last2 = n % 10
		n //= 10
		last3 = n % 10
		if last1 > last2 and last2 > last3:
			counter += 1
		a += 1
	print(counter)
elif n == 3:
	a = 100
	res_sum = 0
	count_add = 0
	while a < 1000:
		n = a 
		for i in range(3):
			last = n % 10
			if last % 2 == 0:
				count_add = 0
				break
			else:
				count_add += 1
				n = n // 10
		if count_add > 0:
			res_sum += a
		a += 1
		count_add = 0
	print(res_sum)
elif n == 4:
	a = 100
	counter = 0
	while a < 1000:
		n = a
		last1 = n % 10
		n //= 10
		last2 = n % 10
		n //= 10
		last3 = n % 10
		if last1 < last2 and last2 < last3:
			counter += 1
		a += 1
	print(counter)
elif n == 5:
	a = 100
	res_sum = 0
	while a < 1000:
		n = a
		last1 = n % 10
		n //= 10
		last2 = n % 10
		n //= 10
		last3 = n % 10
		if (last1) ** 3 + (last2) ** 3 + (last3) ** 3 == a:
			res_sum += a
		a += 1
	print(res_sum)
elif n == 6:
	a = 100
	counter = 0
	while a < 1000:
		n = a
		last1 = n % 10
		n //= 10
		last2 = n % 10
		n //= 10
		last3 = n % 10
		if last1 != last2 and last2 != last3 and last3 != last1:
			counter += 1
		a += 1
	print(counter)
