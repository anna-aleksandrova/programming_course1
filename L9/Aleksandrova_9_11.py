"""
Вхідні дані
У першому рядку вхідного файлу знаходиться два числа N і M (1 ≤ N ≤ 1000, 1 ≤ M ≤ 10000).

У наступних N рядках міститься по одному слову зі словника. Усі слова складаються з рядкових
латинських літер, довжина кожного слова не перевищує 20. Кожне слово складається хоча б з одного
имволу. Зайвих пропусків перед словом і після нього немає.

У наступних M рядках знаходиться текст твору. Текст складається з великих і маленьких латинських
літер, пропусків і розділових знаків: точок (.), ком (,), двокрапок (:), крапок з комою (;), тире (-),
апострофів ('), лапок ("), знаків оклику (!) і знаків питання (?). Загальна довжина тексту не перевищує
10^4 символів.

У даній задачі великі і маленькі літери у словах не розрізняються.

Вихідні дані
Якщо з твором усе в порядку, виведіть Everything is going to be OK.

Якщо не усі слова з тексту зустрічаються у словнику, виведіть Some words from the text are unknown.

Якщо ж попереднє неправильно, але деякі слова із словника не зустрічаються у тексті, виведіть
The usage of the vocabulary is not perfect.

Приклад

Вхідні дані #1
3 1
am
bill
i
I am Bill, am I?

Вихідні дані #1
Everything is going to be OK.

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15339611
"""
with open("input.txt") as input_file:
    lines = input_file.readlines()
N, M = [int(el) for el in lines[0].split()]

alphabet = ".,:;-\'\"!?\n"                          # видалення розділових знаків у тексті
counter = -1
for line in lines:
    counter += 1
    for symbol in line:
        if symbol in alphabet:
            line = line.replace(symbol, "")
        else:
            pass
    lines[counter] = line

words_in_dict = set()                               # множина слів у словнику
for line in lines[1:N + 1]:
    words_in_dict.add(line.lower())

words_in_text = set()                               # множина слів у тексті
for line in lines[N + 1:N + M + 1]:
    for word in line.split():
        words_in_text.add(word.lower())

text_correctness = True
all_words_from_the_text_are_in_dict = True
if len(words_in_text.intersection(words_in_dict)) < len(words_in_text):
    text_correctness = False
    all_words_from_the_text_are_in_dict = False
    print("Some words from the text are unknown.")

if len(words_in_dict.intersection(words_in_text)) < len(words_in_dict) and all_words_from_the_text_are_in_dict:
    text_correctness = False
    print("The usage of the vocabulary is not perfect.")

if text_correctness:
    print("Everything is going to be OK.")