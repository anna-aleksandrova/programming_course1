"""
Степан називає додатне ціле число p щасливим простим, якщо число p і число p[1], 
яке утворено читанням десяткового запису в зворотньому порядку, різні прості числа.

Нагадаємо, що ціле додатне число називається простим, якщо воно не має дільників крім 1 і самого числа.

Знаючи число K, знайти K-те щасливе просте число.

####Вхідні дані
В єдиному рядку записано одне ціле число K (1 ≤ K ≤ 1000).

####Вихідні дані
Якщо K -те число не перевищує 10^6 , виведіть його. В іншому випадку виведіть - 1.

Приклад
Вхідні дані #1 
1
Вихідні дані #1 
13

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15000463
"""
def happy_prime_number(k):
	counter = 0
	number = 13

	while True:
		prime_number = True                    #перевірка, чи число number просте 
		for i in range(3, int((number)**0.5 + 1)):
			if number % i == 0:
				prime_number = False
				break
			else:
				pass

		if prime_number == True:               #побудова числа, що є записом number у зворотньому порядку (number_reversed)
			lst_with_digits_of_number = []
			number_add = number
			while number_add > 0:
				last = number_add % 10
				lst_with_digits_of_number.append(last)
				number_add //= 10

			number_reversed = 0
			for i in range(len(lst_with_digits_of_number)):
				number_reversed += (10**(len(lst_with_digits_of_number) - 1 - i)) * lst_with_digits_of_number[i]

			if number != number_reversed:      #перевірка, чи число number != number_reversed
				prime_number_reversed = True                    #перевірка, чи число number_reversed просте
				for i in range(2, int((number_reversed)**0.5 + 1)):
					if number_reversed % i == 0:
						prime_number_reversed = False
						break
					else:
						pass
				if prime_number_reversed == True:
					counter += 1
				else:
					pass
			else:
				pass
		else:
			pass

		if k == counter:
			if number <= 10**6:
				print(number)
			else:
				print(-1)
			break
		else:
			number += 2

k = int(input())
happy_prime_number(k)