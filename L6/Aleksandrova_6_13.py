"""
Впорядкування

Задано рядок, що складається з маленьких латинських літер. Виведіть усі його літери, 
впорядковані за алфавітом (в порядку зростання ASCII кодів його символів).

Вхідні дані
Один рядок, що складається з не більш ніж 200 маленьких латинських літер.

Вихідні дані
Виведіть усі літери рядка, впорядковані за алфавітом.

Приклад

Вхідні дані #1 
abrakadabra

Вихідні дані #1 
aaaaabbdkrr

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14804143

O(n) + O(n*log(n))= O(n*log(n))
"""
string = input()
lst = list(string)
lst.sort()
for i in range(len(lst)):
	print(lst[i], end = "")