"""
Задано число n у десятковій системі числення. Переведіть це число у тринадцяткову систему числення.

Вхідні дані
Одне число n (1 ≤ n ≤ 1000).

Вихідні дані
Виведіть число n у тринадцятковій системі числення.

Приклад

Вхідні дані #1 
1
Вихідні дані #1 
1

Вхідні дані #2 
10
Вихідні дані #2 
A

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15118177
"""
alphabet = "0123456789ABC"

def convert(number):            # from 10 to 13
	if number < 13:
		return alphabet[number]
	else:
		number_in_13 = str(convert(number // 13)) + str(convert(number % 13))
		return number_in_13

number = int(input())
print(convert(number))