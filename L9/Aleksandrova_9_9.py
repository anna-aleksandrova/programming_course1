"""
Більшість голосів

Вхідні дані
Перший рядок містить кількість тестів (від 1 до 100 включно). Перший рядок кожного тесту
містить кількість голосів n (від 1 до 1000), за яким ідуть n рядків, кожен із них містить
одне число від 1 до 1000.

Вихідні дані
Для кожного тесту вивести в окремому рядку найпопулярніше число. Якщо таких чисел декілька,
вивести найменше число з максимальною кількістю голосів.

Приклад

Вхідні дані

3
3
42
42
19
4
7
99
99
7
5
11
12
13
14
15

Вихідні дані

42
7
11

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15299616
"""
test_am = int(input())
res = []
for _ in range(test_am):
    dict = {}
    voices_am = int(input())
    for voice in range(voices_am):
        number = int(input())
        if number not in dict:
            dict[number] = 1
        else:
            dict[number] += 1
    _res = []
    max_count = max(dict.values())
    for number, count in dict.items():
        if count == max_count:
            _res.append(number)
    res.append((min(_res)))
for item in res:
    print(item)