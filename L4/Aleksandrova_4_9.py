"""
Деякі числа непарні. Наприклад, число 3 непарне, так як не ділиться на два. Числа, які діляться на два, непарними не будуть, вони називаються парними. Більш точно, якщо число n можна представити у вигляді n = 2 * k для деякого цілого k, то n парне. Наприклад, 6 = 2 * 3 парне.

Деякі люди плутаються, чи є число парнv або непарнм. Щоб розібратися, Ви можете задати запит інтернет пошукачу "чи є число парним або непарним?" (Не виконуйте пошук! Розв'яжіть задачу!)

Напишіть програму для таких людей.

Bхідні дані
Починається рядком з кількістю вхідних даних n (1 ≤ n ≤ 20). Кожен з наступних n рядків містить одне ціле число x (-10 ≤ x ≤ 10).

Вихідні дані
Для кожного x виведіть або 'x is odd', або 'x is even' в залежності від того, чи є x непарним або парним.

Приклад
Вхідні дані #1 
3
10
9
-5
Вихідні дані #1 
10 is even
9 is odd
-5 is odd
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14574104
"""
n = int(input()) 
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        print(f"{k} is even")
    else:
        print(f"{k} is odd")