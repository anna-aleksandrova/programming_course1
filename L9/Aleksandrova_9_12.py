"""
Чи можна з літер слова a скласти слово b, причому кожну з літер можна використовувати декілька разів?

Вхідні дані
Слово a в першому рядку, b - в другому, що складаються з англійських літер.

Вихідні дані
Вивести Ok при позитивній відповіді і No у протилежному випадку.

Приклад

Вхідні дані #1
abrakadabra
kabak
Вихідні дані #1
Ok

Вхідні дані #2
abrakadabra
kakadu
Вихідні дані #2
No

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15334349
"""
word_a = input()
word_b = input()

letters_word_a = set(word_a)
letters_word_b = set(word_b)

if letters_word_b <= letters_word_a:
    print("Ok")
else:
    print("No")