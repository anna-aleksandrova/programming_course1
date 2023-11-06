"""
Числа з різними цифрами

Виведіть всі чотирицифрові числа від a до b, що містять різні цифри.

Вхідні дані
Два цілих числа a і b (1000 ≤ a ≤ b ≤ 9999).

Вихідні дані
Виведіть в один рядок всі числа від a до b з різними цифрами.

Приклад
Вхідні дані #1 
2000 2015
Вихідні дані #1 
2013 2014 2015 

Вхідні дані #2 
9875 9999
Вихідні дані #2 
9875 9876 

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15007646
"""
def different_digits(number):
	list_with_digits = []
	while number > 0:
		last_digit = number % 10
		list_with_digits.append(last_digit)
		number //= 10
	
	digits_are_different = True
	list_with_unique_digits = set(list_with_digits)
	if len(list_with_digits) != len(list_with_unique_digits):
		digits_are_different = False
	return digits_are_different

a, b = [int(el) for el in input().split()]
list_with_appropriate_numbers = []
for number in range(a, b + 1):
	if different_digits(number) == True:
		list_with_appropriate_numbers.append(number)
	else:
		pass
print(*list_with_appropriate_numbers)
