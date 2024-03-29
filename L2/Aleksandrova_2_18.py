"""
Визначте, чи належить точка (x, y) прямокутнику з кінцями діагоналі (x[1], y[1]), (x[2], y[2]) і сторонами, паралельними координатним осям.

Вхідні дані
Шість дійсних чисел x, y, x[1], y[1], x[2], y[2] - координати точки та координати кінців діагоналі прямокутника, відповідно. Числові значення за модулем не перевищують 100.

Вихідні дані
Вивести 1, якщо точка належить прямокутнику, та 0 інакше.

Приклад
Вхідні дані #1
1 2 3 4 0 0

Вихідні дані #1
1

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14304834
"""
x, y, x1, y1, x2, y2 = [int(el) for el in input().split()]
print("1") if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) else print("0")
