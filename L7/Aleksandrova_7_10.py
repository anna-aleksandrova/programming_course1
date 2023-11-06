"""
Системи числення

Дано ціле невід'ємне число у m-й системі числення. Потрібно вивести це число 
в k-й системі числення.

Вхідні дані
Вхідний файл у першому рядку містить два числа m і k (у десятковій системі 
числення), у другому рядку - число для переведення.

2 ≤ m, k ≤ 36, для представлення цифр 10...35 використовуються прописні 
латинські літери A...Z відповідно, число розрядів заданого числа не перевищує 1000.

Вихідні дані
У вихідний файл виведіть шукане число без ведучих нулів.

Приклад

Вхідні дані #1 
10 36
29234652

Вихідні дані #1 
HELLO

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15010526
"""
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def from_m_to_decimal(m, k, number):    
	                           
	lst_with_digits_of_number = []
	for el in number:
		lst_with_digits_of_number.append(alphabet.index(el))

	number_in_decimal = 0
	for i in range(len(list(reversed(lst_with_digits_of_number)))):
		number_in_decimal += list(reversed(lst_with_digits_of_number))[i] * (m**i)
	return number_in_decimal


def from_decimal_to_k(number_in_decimal, k):

	lst_with_remainders = []
	while number_in_decimal >= k:
		lst_with_remainders.append(alphabet[number_in_decimal % k])
		number_in_decimal //= k
	lst_with_remainders.append(alphabet[number_in_decimal])

	lst_with_remainders_reversed = map(str, lst_with_remainders[::-1])
	
	number_in_system_with_base_k = ""
	number_in_system_with_base_k = number_in_system_with_base_k.join(lst_with_remainders_reversed)
	return number_in_system_with_base_k


m, k = [int(el) for el in input().split()]
number = str(input())                               #number in base m
number_in_decimal = from_m_to_decimal(m, k, number)
result = from_decimal_to_k(number_in_decimal, k)
print(result)
