"""
Потрібно визначити, чи є заданий рік високосним.

Нагадаємо, що рік є високосним, якщо його номер кратний 4, але не крате ий100, а також якщо він кратний 400.

Вхідні дані
Вхідний файл містить єдине число 0 ≤ N ≤ 9999, номер року.

Вихідні дані
У вихідний файл виведіть YES, якщо рік є високосним і NO у протилежному випадку.

Приклад
Вхідні дані #1
4

Вихідні дані #1
YES

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14252192
"""
n = int(input())
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("YES")
else:
    print ("NO")
