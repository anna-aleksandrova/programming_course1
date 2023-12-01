"""
Вхідні дані
У першому рядку міститься єдине ціле число N - кількість англійських слів у словнику. Далі йде N описів.
У першому рядку кожного опису міститься англійське слово. У наступному рядку записано єдине число K ≥ 1 -
кількість перекладів. У наступних K рядках наведено переклади поточного англійського слова на латинський,
по одному у кожному рядку.

Кожен опис міститься у окремому рядку, у якому записано спочатку англійське слово, потім відокремлений
пропусками дефіс (символ номер 45), потім відокремлені комами з пропусками переклади цього англійського слова
на латинський. Переклади відсортовано у лексикографічному порядку. Порядок слідування англійських слів у
словнику також лексикографічний.

Всі слова складаються лише з маленьких латинських літер, довжина кожного слова не перевищує 15 символів.
Загальна кількість слів на вході не перевищує 100000.

Вихідні дані
Виведіть відповідний заданому латино-англійський словник, у точності зберігаючи формат вхідних даних. Зокрема,
першим повинен йти переклад лексикографічно мінімального латинського слова, далі - другого у цьому порядку і т.д.
Всередині перекладу англійські слова повинні бути також відсортовані лексикографічно.

Приклад
Вхідні дані #1
3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa

Вихідні дані #1
7
baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15338422
"""
N = int(input())
eng_lat_dict = {}
unnecessary_symbols = {",", "-"}
for _ in range(N):
    string = input()
    for symbol in string:
        if symbol in unnecessary_symbols:
            string = string.replace(symbol, "")
        string = string.replace("  ", " ")
    index_first__ = string.find(" ")
    x = str(string[0:index_first__])
    y = str(string[index_first__ + 1:len(string)])
    eng_lat_dict.update({x: y})


all_latin_words = []
for value in eng_lat_dict.values():
    for el in value.split():
        all_latin_words.append(el)
latin_words = list(set(all_latin_words))

lat_eng_dict = dict.fromkeys(latin_words)

for key, value in lat_eng_dict.items():
    meaning = []
    for key_, value_ in eng_lat_dict.items():
        if key in value_.split():
            meaning.append(key_)
    meaning.sort()
    lat_eng_dict[key] = ", ".join(meaning)
sorted_keys_lat_eng = [el for el in lat_eng_dict.keys()]
sorted_keys_lat_eng.sort()

print(len(sorted_keys_lat_eng))
for i in range(len(sorted_keys_lat_eng)):
    output = sorted_keys_lat_eng[i] + " - " + lat_eng_dict[sorted_keys_lat_eng[i]]
    print(output)