"""
Визначте, чи належить точка C заданій прямой, променю та відрізку, утвореним точками A та B.

Вхідні дані
   У першому рядку вхідного файлу задано два цілих числа - координати точки C. У двох наступних рядках у такому ж форматі задано точки A та B (A ≠ B). Усі числа у вхідному файлі по модулю не перевищують 10000.

Вихідні дані
   У першому рядку виведіть YES, якщо точка C належить прямій AB, і NO у протилежному випадку. У другому та третьому рядках аналогічно виведіть відповіді для променя AB (A - початок променя) та відрізка AB.

Приклад
Вхідні дані #1
1 6
3 7
5 8

Вихідні дані #1
YES
NO
NO

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14304449
"""
xc, yc = [int(el) for (el) in input().split()]
xa, ya = [int(el) for (el) in input().split()]
xb, yb = [int(el) for (el) in input().split()]

print("YES") if (xc - xa)*(yb - ya) == (xb - xa)*(yc - ya) else print("NO")

print("YES") if (xc - xa)*(yb - ya) == (xb - xa)*(yc - ya) and ((min(xa, xb) <= xc <= max(xa, xb) and min(ya, yb) <= yc <= max(ya, yb)) or (min(xa, xc) <= xb <= max(xa, xc) and min(ya, yc) <= yb <= max(ya, yc))) else print("NO")

print("YES") if (xc - xa)*(yb - ya) == (xb - xa)*(yc - ya) and min(xa, xb) <= xc <= max(xa, xb) and min(ya, yb) <= yc <= max(ya, yb) else print("NO")
