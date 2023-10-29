"""
Назвемо пароль криптостійким, якщо виконується 5 критеріїв:

1. Пароль містить маленькі латинські латинські літери

2. Пароль містить великі латинські літери

3. Пароль містить цифри

4. Символи: ! " # $ % & ' ( ) * +

5. Довжина пароля не менше 8 символів

Потрібно за даним паролем встановити, скільки критеріїв крипто стійкості виконується.

Вхідні дані:
Вводиться один рядок, що складається тільки з латинських символів цифр і символів (п.4). 
Кількість символів не перевищує 100.

Вихідні дані
Виведіть кількість критеріїв крипто стійкості, яким задовільняє пароль.

Приклад
Вхідні дані #1 
1aA
Вихідні дані #1 
3

Вхідні дані #2 
AaBbCc12
Вихідні дані #2 
4

Вхідні дані #3 
AAAaaaAAA
Вихідні дані #3 
3

Вхідні дані #4 
#Abc23$$$
Вихідні дані #4 
5

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14803265
O(n)
"""
string = input()
counter = 0
list_of_symbols = ["!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+"]

for i in range(len(string)):
	if ord("a") <= ord(string[i]) <= ord("z"):
		counter_add_1 = 1
		break
	else:
		counter_add_1 = 0

for i in range(len(string)):
	if ord("A") <= ord(string[i]) <= ord("Z"):
		counter_add_2 = 1
		break
	else:
		counter_add_2 = 0

for i in range(len(string)):
	if ord("0") <= ord(string[i]) <= ord("9"):
		counter_add_3 = 1
		break
	else:
		counter_add_3 = 0

for i in range(len(string)):
	if string[i] in list_of_symbols:
		counter_add_4 = 1
		break
	else:
		counter_add_4 = 0

if len(string) >= 8:
	counter_add_5 = 1
else:
	counter_add_5 = 0

print(counter_add_1 + counter_add_2 + counter_add_3 + counter_add_4 + counter_add_5)