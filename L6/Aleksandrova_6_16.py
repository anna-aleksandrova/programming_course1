"""
Задано рядок s довжиною більше десяти символів. Враховуємо, що перший 
символ рядка має індекс 0. Знайти і вивести отаке.

Слово, що утворюють третій, сьомий і одинадцятий символ рядка s.

Слово, що утворюють перший і два останніх символа рядка s.

Слово, що утворюють сім перших символів рядка s.

Рядок s без чотирьох перших символів.

Слово, що утворюють усі символи з непарними індексами, починаючи з другого символа рядка s..

Довжину слова з попереднього пункту.

Рядок s у зворотному порядку.

Приклад

Вхідні дані #1
abrakadabra

Вихідні дані #1
rda
ara
abrakad
kadabra
baaar
5
arbadakarba

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14826326

O(n)
"""
st = str(input())
print(st[2] + st[6] + st[10])
print(st[0] + st[len(st) - 2] + st[len(st) - 1])
print(st[:7])
print(st[4:len(st)])
print(st[1:len(st) + 1: 2])
print(len(st[1:len(st) + 1: 2]))
print(st[::-1])