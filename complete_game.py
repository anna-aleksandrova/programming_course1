# Команда: Александрова Анна, Качуровська Юлія, Ужвенко Юлія
import time
from random import *
import random
begg = """
█▀▄▀█ ▄███▄   ▄█▄     ▄  █     ██   ██▄       ▄   ▄███▄      ▄     ▄▄▄▄▀ ▄   █▄▄▄▄ ▄███▄
█ █ █ █▀   ▀  █▀ ▀▄  █   █     █ █  █  █       █  █▀   ▀      █ ▀▀▀ █     █  █  ▄▀ █▀   ▀
█ ▄ █ ██▄▄    █   ▀  ██▀▀█     █▄▄█ █   █ █     █ ██▄▄    ██   █    █  █   █ █▀▀▌  ██▄▄
█   █ █▄   ▄▀ █▄  ▄▀ █   █     █  █ █  █   █    █ █▄   ▄▀ █ █  █   █   █   █ █  █  █▄   ▄▀
   █  ▀███▀   ▀███▀     █         █ ███▀    █  █  ▀███▀   █  █ █  ▀    █▄ ▄█   █   ▀███▀
  ▀                    ▀         █           █▐           █   ██        ▀▀▀   ▀
                                ▀            ▐
    Ласкаво просимо, мандрівнику!

    Ви опинилися біля входу в таємниче та старовинне підземелля.
Повітря насичене очікуванням, і єдине джерело світла -- ваш
надійний факел. Ваше серцебиття прискорюється, коли ви готуєтеся
вирушити в небезпечну подорож, сповнену викликів, скарбів і
неймовірних пригод.

    Ваша доля чекає глибоко в цих темних і звивистих коридорах.
Докажете, що ви герой, чи підземелля забере ще одну жертву?
Вибір за вами.

    Приготуйтеся, відважний шукачу пригод, і нехай ваша кмітливість
і відвага проведуть вас через невідоме. Ваша пригода починається зараз!
"""
print(begg)


if input("Ви бажаєте розпочати гру? (так/ні)\n>>>---> ") != "так":
    exit(0)

game_over = """
  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █
 ███     █    █  ▀███▀               █  █  ▀███▀     █
        █    ▀                        █▐            ▀
       ▀                              ▐
"""

beg = ">>>--->"
x0 = """
▄█▄     ▄  █ ██   █▄▄▄▄ ██   ▄█▄      ▄▄▄▄▀ ▄███▄   █▄▄▄▄
█▀ ▀▄  █   █ █ █  █  ▄▀ █ █  █▀ ▀▄ ▀▀▀ █    █▀   ▀  █  ▄▀
█   ▀  ██▀▀█ █▄▄█ █▀▀▌  █▄▄█ █   ▀     █    ██▄▄    █▀▀▌
█▄  ▄▀ █   █ █  █ █  █  █  █ █▄  ▄▀   █     █▄   ▄▀ █  █
▀███▀     █     █   █      █ ▀███▀   ▀      ▀███▀     █
         ▀     █   ▀      █                          ▀
              ▀          ▀
"""

print(x0)
print("Перш ніж ви вирушите у свою епічну подорож, нам потрібно створити вашого персонажа. Для початку надайте такі відомості: \nІм'я:")
name = input(f"{beg}: ")

x1 = """
Виберіть расу свого персонажа з наступних варіантів:
    - Карлик
    - Ельф
    - Людина
    - Дракононароджений
    - Орк
    - Гоблін"""
print(x1)
race = input(f"{beg}: ")


while True:
    if race != "Карлик" and race != "Ельф" and race != "Людина" and race != "Дракононароджений" and race != "Орк" and race != "Гоблін" and race != "карлик" and race != "ельф" and race != "людина" and race != "дракононароджений" and race != "орк" and race != "гоблін":
        print("Ви неправильно ввели расу. Повторіть ще раз")
        race = input(f"{beg}: ")
    else:
        break


print('Ви чоловік чи жінка? (якщо не бажаєте говорити, впишіть "не бажаю говорити")')
s = input(f"{beg}: ")
while True:
    if s != "Чоловік" and s != "чоловік" and s != "Жінка" and s != "жінка" and s != "не бажаю говорити" and s!= "Не бажаю говорити":
        print("Ви неправильно ввели стать. Повторіть ще раз")
        s = input(f"{beg}: ")
    else:
        break

print("Скільки років ви прожили?")
age = input(f"{beg} ")
age = int(age)
while True:
    if age < 0 or age > 150:
        print("Ви неправильно ввели вік. Повторіть ще раз")
        age = input(f"{beg}")
        age = int(age)
    else:
        break

print("""\nМаєте 10 очків для розподілення між Вашою Силою, Спритністю та Інтелектом.
Після кожного пройденого рівня Вам додається ще одне очко. Розподіл - на Ваш вибір.\n""")
#Початкова кількість очків
n = 10
power = input("Введіть значення Сили: ")
agility = input("Введіть значення Спритності: ")
intelligence = input("Введіть значення Інтелекту: ")
power = int(power)
agility = int(agility)
intelligence = int(intelligence)
while True:
    if power + agility + intelligence != 10:
        e = """\nВи неправильно розподілили очки. Нагадую, що їх всього десять. Спробуйте ще раз.
            """
        print(e)
        power = input("Введіть значення Сили: ")
        agility = input("Введіть значення Спритності: ")
        intelligence = input("Введіть значення Інтелекту: ")
        power = int(power)
        agility = int(agility)
        intelligence = int(intelligence)
    else:
        break

### LEVEL1###
level_game = 1
lvl_1 = """
█     ▄███▄      ▄   ▄███▄   █         ████▄    ▄   ▄███▄
█     █▀   ▀      █  █▀   ▀  █         █   █     █  █▀   ▀
█     ██▄▄   █     █ ██▄▄    █         █   █ ██   █ ██▄▄
███▄  █▄   ▄▀ █    █ █▄   ▄▀ ███▄      ▀████ █ █  █ █▄   ▄▀
    ▀ ▀███▀    █  █  ▀███▀       ▀           █  █ █ ▀███▀
                █▐                           █   ██
                ▐

Ласкаво просимо, хоробрий шукачу пригод, до Кімнати чарівної загадки.
Щоб продовжити, Ви повинні довести свою кмітливість.

Ось я загадую Вам загадку: є число від 0 до 10, приховане в тумані часу
й магії. У вас є три спроби розкрити таємницю. Вгадайте правильне число,
і шлях відкриється. Обирайте мудро.
"""

print(lvl_1)

o = random.randint(0, 10)

beg = ">>>--->"

while True:
    for i in range(3):
        if i == 2:
            print("\nАх, ви дійшли до своєї останньої спроби. Подивимося, чи прихильною до вас сьогодні буде доля.\n")
        numb = input("\nВведіть число (від 0 до 10)\n>>>---> ")
        numb = int(numb)
        while True:
            if numb < 0 or numb > 10:
                print("Ви неправильно ввели число")
                numb = input(f"{beg}")
                numb = int(numb)
            else:
                break
        if numb == o:
            print("Вітаю, відважний шукачу пригод! Ви розкрили таємницю Зачарованої загадки. Магія в кімнаті відповідає вашій мудрості.")
            break
        elif numb != o and numb > o:
            print("Вихор заворушився, але ваша здогадка не зовсім вірна. Справжнє число менше. Спробуйте ще раз.")
        elif numb != o and numb < o:
            print("Вихор заворушився, але ваша здогадка не зовсім вірна. Справжнє число більше. Спробуйте ще раз.")
    if numb == o:
        break
    else:
        print("\nСьогодні доля тобі не була прихильною, відважний шукачу пригод. Твоїх знань виявилося недостатньо, і ти не пройшов випробування.\n")
        print(game_over)
        exit(0)



menu ="""
МЕНЮ:
1. Грати наступний рівень
2. Показати всю інформацію про персонажа (рівень, ім'я, раса, вік, характеристики)
3. Змінити ім'я
4. Використати додаткові очки характеристик, які були зароблені після проходження рівнів
5. Вийти
"""
print(menu)
option = input(f"Оберіть опцію(номер):\n{beg}")
option = int(option)
while True:
    if option < 1 or option > 5:
        print("\nВи ввели неправильний номер. Спробуйте ще раз.\n")
        option = input(f"Оберіть опцію(номер):\n{beg}")
        option = int(option)
    else:
        break

while True:
    if option == 1:
        break
    elif option == 2:
        print(f"Ім'я: {name}")
        print(f"Раса: {race}")
        print(f"Стать: {s}")
        print(f"Вік: {age}")
        print(f"Рівень: {level_game}")
        break
    elif option == 3:
        name = input(f"Введіть нове ім'я:\n{beg}")
        break
    elif option == 4:
            n += 1
            print("""\nВи маєте одне додаткове очко. Введіть його в характеристику,
рівень якої бажаєте підвищити. Для інших - введіть 0.""")
            power1 = input("Додати до Сили: ")
            agility1 = input("Додати до Спритності: ")
            intelligence1 = input("Додати до Інтелекту: ")
            power1 = int(power1)
            agility1 = int(agility1)
            intelligence1 = int(intelligence1)
            while True:
                if power1 + agility1 + intelligence1 != 1:
                    print("Ви маєте тільки 1 додатковий бал. Спробуйте ще раз.")
                    power1 = input("Додати до Сили: ")
                    agility1 = input("Додати до Спритності: ")
                    intelligence1 = input("Додати до Інтелекту: ")
                    power1 = int(power1)
                    agility1 = int(agility1)
                    intelligence1 = int(intelligence1)
                else:
                    power = power + power1
                    agility = agility + agility1
                    intelligence = intelligence + intelligence1
                    break
            print("Hello")
            break

    elif option == 5:
        exit(0)


###LEVEL 2
level_game = 2
k = """
█     ▄███▄      ▄   ▄███▄   █            ▄▄▄▄▀ ▄ ▄   ████▄
█     █▀   ▀      █  █▀   ▀  █         ▀▀▀ █   █   █  █   █
█     ██▄▄   █     █ ██▄▄    █             █  █ ▄   █ █   █
███▄  █▄   ▄▀ █    █ █▄   ▄▀ ███▄         █   █  █  █ ▀████
    ▀ ▀███▀    █  █  ▀███▀       ▀       ▀     █ █ █
                █▐                              ▀ ▀
                ▐


Ласкаво просимо назад, безстрашний шукачу пригод,
у місце, де буде перевірена інтуїція. Ви стоїте перед
парадоксом Монті Голла - головоломкою ймовірностей і варіантів.
Чи готові Ви розгадати його таємниці?

За одними з трьох дверей ховається неймовірний скарб,
а за двома іншими, ну, скажімо так, є щось менш бажане.
Ваша мета проста: вибрати одні двері.

Зробіть цей вибір мудро, авантюристe, і нехай парадокс Монті Голла
почнеться!
"""
print(k)

win = random.randint(1, 3)
print("Введіть номер дверей: ")
choice = input(f"{beg}" )
choice = int(choice)

while True:
    if choice != 1 and choice != 2 and choice != 3:
        print("Ви ввели неправильний номер. Повторіть ще раз")
        choice = input(f"{beg}" )
        choice = int(choice)
    else:
        break

wrong1 = not win
while wrong1 < 1 or wrong1 == win:
    wrong1 += 1
while wrong1 > 3 or wrong1 == win:
    wrong1 -= 1

wrong2 = not win
while wrong2 < 1 or wrong2 == win or wrong2 == wrong1:
    wrong2 += 1
while wrong2 > 3 or wrong2 == win or wrong2 == wrong1:
    wrong2 -= 1

if choice == win:
    wrong_door = random.randint(wrong1, wrong2)
elif choice == wrong1:
    wrong_door = wrong2
else:
    wrong_door = wrong1


l = f"""
Чудово, відважний шукачу пригод. Ви вибрали Двері {choice}.

Тепер давайте додамо родзинку цьому виклику. Перш ніж я покажу,
що знаходиться за вибраними Вами дверима,
дозвольте мені зробити речі цікавішими. З двох дверей, що залишилися,
вам буде показана одна, що розкриє результат, якого ви б уникали...

Отож за Дверима {wrong_door} - кровожерливі тигри.

Розумієте, авантюристе, тепер у Вас є унікальна можливість.
Ви можете залишитися при своєму початковому виборі або
перейти до інших невідкритих дверей. Рішення за Вами. Обирайте.
"""
print(l)

print("Введіть номер дверей: ")
choice = input(f"{beg}" )
choice = int(choice)

while True:
    if choice != 1 and choice != 2 and choice != 3:
        print("Ви ввели неправильний номер. Повторіть ще раз")
        choice = input(f"{beg}" )
        choice = int(choice)
    else:
        break

m = """
Вітаю, мудрий шукачу пригод! Ви подолали парадокс Монті-Голла та
заволоділи бажаним скарбом. Ваша інтуїція та сміливість виправдалися!
"""

n = """
Лихо спіткало Вас, авантюристе. За дверима, які ви вибрали,
чекала неприборкана й небезпечна доля. Тигри прагнуть наступної
їжі, і, здається, Ви в меню.

Скарб, який ви шукали, назавжди залишається недосяжним,
а Парадокс Монті Холла набуває нового та жахливого значення.

Запам’ятайте цю історію як повчальну
для тих, хто наважується вирушити в невідоме.

Гра закінчена, відважний авантюристе.
Нехай Ви знайдете спокій у іншому світі.
"""

if choice == win:
    print(m)
else:
    print(n)
    print(game_over)
    exit(0)


print(menu)
option = input(f"Оберіть опцію(номер):\n{beg}")
option = int(option)
while True:
    if option < 1 or option > 5:
        print("\nВи ввели неправильний номер. Спробуйте ще раз.\n")
        option = input(f"Оберіть опцію(номер):\n{beg}")
        option = int(option)
    else:
        break

while True:
    if option == 1:
        break
    elif option == 2:
        print(f"Ім'я: {name}")
        print(f"Раса: {race}")
        print(f"Стать: {s}")
        print(f"Вік: {age}")
        print(f"Рівень: {level_game}")
        break
    elif option == 3:
        name = input(f"Введіть нове ім'я:\n{beg}")
        break
    elif option == 4:
        if level_game == 2 and power + intelligence + agility > 10:
                print("""\nВи маєте ще одне додаткове очко. Введіть його в характеристику,
рівень якої бажаєте підвищити. Для інших - введіть 0.""")
                power21 = input("Додати до Сили: ")
                agility21 = input("Додати до Спритності: ")
                intelligence21 = input("Додати до Інтелекту: ")
                power21 = int(power21)
                agility21 = int(agility21)
                intelligence21 = int(intelligence21)
                while True:
                    if power21 + agility21 + intelligence21 != 1:
                        print("Ви маєте тільки 1 додатковий бал. Спробуйте ще раз.")
                        power21 = input("Додати до Сили: ")
                        agility21 = input("Додати до Спритності: ")
                        intelligence21 = input("Додати до Інтелекту: ")
                        power21 = int(power21)
                        agility21 = int(agility21)
                        intelligence21 = int(intelligence21)
                        power = power + power21
                        agility = agility + agility21
                        intelligence = intelligence + intelligence21
                    else:
                        power = power + power21
                        agility = agility + agility21
                        intelligence = intelligence + intelligence21
                        break
                break

        elif level_game == 2 and power + intelligence + agility == 10:
                n = n + 2
                print("""\nВи маєте 2 додаткових очки. Додайте їх до характеристик(и),
рівень яких/якої бажаєте підвищити. Для інших - введіть 0.""")
                power22 = input("Додати до Сили: ")
                agility22 = input("Додати до Спритності: ")
                intelligence22 = input("Додати до Інтелекту: ")
                power22 = int(power22)
                agility22 = int(agility22)
                intelligence22 = int(intelligence22)
                while True:
                    if power22 + agility22 + intelligence22 != 2:
                        print("Ви маєте 2 додаткових бали. Спробуйте ще раз.")
                        power22 = input("Додати до Сили: ")
                        agility22 = input("Додати до Спритності: ")
                        intelligence22 = input("Додати до Інтелекту: ")
                        power22 = int(power22)
                        agility22 = int(agility22)
                        intelligence22 = int(intelligence22)
                    else:
                        power = power + power22
                        agility = agility + agility22
                        intelligence = intelligence + intelligence22
                        break
                break
        else:
            break
    elif option == 5:
        exit(0)

level_game = 3
### LEVEL3
g = """
На жаль, шукачу пригод, пісок часу вичерпався.
Магія цих рівнянь залишається загадкою, а ціна за невдачу
висока.

Гра закінчена, відважний авантюристе. Нехай Ваш дух знайде
спокій серед магії, яка зараз оточує Вас.
"""
h = """
Чудово! Ваш інтелект і рішучість розкрили секрети
Кімнати містичних рівнянь. Ви використали магію всередині
себе й заслужили право продовжити
"""


f = """
█     ▄███▄      ▄   ▄███▄   █            ▄▄▄▄▀ ▄  █ █▄▄▄▄ ▄███▄   ▄███▄
█     █▀   ▀      █  █▀   ▀  █         ▀▀▀ █   █   █ █  ▄▀ █▀   ▀  █▀   ▀
█     ██▄▄   █     █ ██▄▄    █             █   ██▀▀█ █▀▀▌  ██▄▄    ██▄▄
███▄  █▄   ▄▀ █    █ █▄   ▄▀ ███▄         █    █   █ █  █  █▄   ▄▀ █▄   ▄▀
    ▀ ▀███▀    █  █  ▀███▀       ▀       ▀        █    █   ▀███▀   ▀███▀
                █▐                               ▀    ▀
                ▐

Ласкаво просимо, шукачу знань, у Кімнату містичних рівнянь.
Тут сама тканина магії переплітається з математикою,
і ваші навички будуть перевірені у найнезвичайніший спосіб.

Перед вами лежить низка зачарованих рівнянь, кожне з яких тримає ключ,
щоб відкрити наступну частину Вашої подорожі.
Ці рівняння — не звичайні головоломки; вони — втілення магічних сил,
які чекають, поки ви розгадаєте їхні таємниці.

Щоб рухатися вперед, ви повинні розв’язати ці містичні рівняння.
Час — ваш ворог, бо магія, яка зв’язує їх, швидкоплинна.
Швидко розв’язуйте кожне рівняння, або можливість зникне.

Приготуйтеся, відважний шукачу пригод. Кімната містичних рівнянь чекає,
і лише Ваш інтелект і швидке мислення відкриють шлях вперед.
"""
print(f)

### РІВНЯННЯ 1

print("Рівняння 1:\n")
while True:
    a1 = random.randint(-100, 100)
    b1 = random.randint(-100, 100)
    c1 = random.randint(-100, 100)
    if a1 != 0:
        break
if a1 > 0 and b1 > 0:
    print(f"{a1}x + {b1} = {c1}")
elif a1 > 0 and b1 < 0:
    print(f"{a1}x - {abs(b1)} = {c1}")
elif a1 < 0 and b1 > 0:
    print(f"-{abs(a1)}x + {b1} = {c1}")
elif a1 < 0 and b1 < 0:
    print(f"-{abs(a1)}x - {abs(b1)} = {c1}")
elif a1 < 0 and b1 == 0:
    print(f"-{abs(a1)}x = {c1}")
else:
    print(f"{a1}x = {c1}")
x1 = (c1 - b1) / a1
correct1 = x1
print("\nВведіть відповідь (за необхідності округліть її до двох знаків після коми)\n")
t01 = time.time()
answer1 = input(f"{beg} ")
answer1 = float(answer1)
error = 0.01
t11 = time.time()
if (t11 - t01) <= 60 + 10*intelligence:
    if abs(correct1 - answer1) < error:
        print("GOOD")
    else:
        print("Неправильна відповідь")
        print(game_over)
        exit(0)
elif (t11 - t01) > 60 + 10*intelligence:
    print(g)
    print(game_over)
    exit(0)
else:
    pass

### РІВНЯННЯ 2
print("\nРівняння 2:\n")
while True:
    a2 = round(random.uniform(-20, 20), 2)
    b2 = round(random.uniform(-20, 20), 2)
    c2 = round(random.uniform(-20, 20), 2)
    if a2 != 0:
        break
if a2 > 0 and b2 > 0:
    print(f"{a2}x + {b2} = {c2}")
elif a2 > 0 and b2 < 0:
    print(f"{a2}x - {abs(b2)} = {c2}")
elif a2 < 0 and b2 > 0:
    print(f"-{abs(a2)}x + {b2} = {c2}")
elif a2 < 0 and b2 < 0:
    print(f"-{abs(a2)}x - {abs(b2)} = {c2}")
elif a2 < 0 and b2 == 0:
    print(f"-{a2}x = {c2}")
else:
    print(f"{a2}x = {c2}")
x2 = (c2 - b2) / a2
correct2 = x2
print("\nВведіть відповідь (за необхідності округліть її до двох знаків після коми)\n")
t02 = time.time()
answer2 = input(f"{beg} ")
answer2 = float(answer2)
error = 0.01
t12 = time.time()
if (t12 - t02) <= 60 + 10*intelligence:
    if abs(correct2 - answer2) < error:
        print("GOOD")
    else:
        print("Неправильна відповідь")
        print(game_over)
        exit(0)
elif (t12 - t02) > 60 + 10*intelligence:
    print(g)
    print(game_over)
    exit(0)
else:
    pass

### РІВНЯННЯ 3
print("Рівняння 3:\n")
while True:
    a3 = random.randint(-3, 3)
    b3 = random.randint(-10, 10)
    c3 = random.randint(-15, 15)
    dis3 = b3**2 - 4*a3*c3
    if a3 != 0 and b3 != 0 and dis3 > 0:
        break
if b3 > 0 and c3 > 0:
    print(f"{a3}x^2 + {b3}x + {c3} = 0")
elif b3 < 0 and c3 < 0:
    print(f"{a3}x^2 - {abs(b3)}x - {abs(c3)} = 0")
elif b3 < 0 and c3 > 0:
    print(f"{a3}x^2 - {abs(b3)}x + {c3} = 0")
elif b3 > 0 and c3 < 0:
    print(f"{a3}x^2 + {b3}x - {abs(c3)} = 0")
else:
    pass
x3_1 = ((-1)*b3 + dis3**0.5) / (2*a3)
x3_2 = ((-1)*b3 - dis3**0.5) / (2*a3)
correct3 = max(x3_1, x3_2)
print("\nВведіть значення більшого кореня (за необхідності округліть його до двох знаків після коми)\n")
t03 = time.time()
answer3 = input(f"{beg} ")
answer3 = float(answer3)
error = 0.01
t13 = time.time()
if (t13 - t03) <= 60 + 10*intelligence:
    if abs(correct3 - answer3) < error:
        print("GOOD")
    else:
        print("Неправильна відповідь")
        print(game_over)
        exit(0)
elif (t13 - t03) > 60 + 10*intelligence:
    print(g)
    print(game_over)
    exit(0)
else:
    pass

### РІВНЯННЯ 4
print("Рівняння 4:\n")
while True:
    a4 = random.randint(-10, 10)
    b4 = random.randint(-15, 15)
    c4 = random.randint(-30, 30)
    dis4 = b4**2 - 4*a4*c4
    if a4 != 0 and b4 != 0 and dis4 >= 0:
        break
if b4 > 0 and c4 > 0:
    print(f"{a4}x^2 + {b4}x + {c4} = 0")
elif b4 < 0 and c4 < 0:
    print(f"{a4}x^2 - {abs(b4)}x - {abs(c4)} = 0")
elif b4 < 0 and c4 > 0:
    print(f"{a4}x^2 - {abs(b4)}x + {c4} = 0")
elif b4 > 0 and c4 < 0:
    print(f"{a4}x^2 + {b4}x - {abs(c4)} = 0")
else:
    pass

if dis4 > 0:
    x4_1 = ((-1)*b4 + dis4**0.5) / (2*a4)
    x4_2 = ((-1)*b4 - dis4**0.5) / (2*a4)
    correct4 = max(x4_1, x4_2)
else:
    x4 = (-1)*b4 / (2*a4)
    correct4 = x4
print("""\nВведіть значення кореня. Якщо коренів два, введіть значення більшого з них.
(за необхідності округліть це значення до двох знаків після коми)\n""")
t04 = time.time()
answer4 = input(f"{beg} ")
answer4 = float(answer4)
error = 0.01
t14 = time.time()
if (t14 - t04) <= 60 + 10*intelligence:
    if abs(correct4 - answer4) < error:
        print("GOOD")
    else:
        print("Неправильна відповідь")
        print(game_over)
        exit(0)
elif (t14 - t04) > 60 + 10*intelligence:
    print(g)
    print(game_over)
    exit(0)
else:
    pass

### РІВНЯННЯ 5
print("Рівняння 5:\n")
while True:
    a5 = round(random.uniform(-2, 2), 1)
    b5 = round(random.uniform(-2, 2), 1)
    c5 = round(random.uniform(-2, 2), 1)
    dis5 = b5**2 - 4*a5*c5
    if a5 != 0 and b5 != 0 and dis5 >= 0:
        break
if b5 > 0 and c5 > 0:
    print(f"{a5}x^2 + {b5}x + {c5} = 0")
elif b5 < 0 and c5 < 0:
    print(f"{a5}x^2 - {abs(b5)}x - {abs(c5)} = 0")
elif b5 < 0 and c5 > 0:
    print(f"{a5}x^2 - {abs(b5)}x + {c5} = 0")
elif b5 > 0 and c5 < 0:
    print(f"{a5}x^2 + {b5}x - {abs(c5)} = 0")
else:
    pass

if dis5 > 0:
    x5_1 = ((-1)*b5 + dis5**0.5) / (2*a5)
    x5_2 = ((-1)*b5 - dis5**0.5) / (2*a5)
    correct5 = max(x5_1, x5_2)
else:
    x5 = (-1)*b5 / (2*a5)
    correct5 = x5
print("""\nВведіть значення кореня. Якщо коренів два, введіть значення більшого з них.
(за необхідності округліть це значення до двох знаків після коми)\n""")
t05 = time.time()
answer5 = input(f"{beg} ")
answer5 = float(answer5)
error = 0.01
t15 = time.time()
if (t15 - t05) <= 60 + 10*intelligence:
    if abs(correct5 - answer5) < error:
        print("GOOD")
    else:
        print("Неправильна відповідь")
        print(game_over)
        exit(0)
elif (t15 - t05) > 60 + 10*intelligence:
    print(g)
    print(game_over)
    exit(0)
else:
    pass
win_3 = 1
if win_3 == 1:
    print(h)

print(menu)
option = input(f"Оберіть опцію(номер):\n{beg}")
option = int(option)
while True:
    if option < 1 or option > 5:
        print("\nВи ввели неправильний номер. Спробуйте ще раз.\n")
        option = input(f"Оберіть опцію(номер):\n{beg}")
        option = int(option)
    else:
        break

while True:
    if option == 1:
        break
    elif option == 2:
        print(f"Ім'я: {name}")
        print(f"Раса: {race}")
        print(f"Стать: {s}")
        print(f"Вік: {age}")
        print(f"Рівень: {level_game}")
        break
    elif option == 3:
        name = input(f"Введіть нове ім'я:\n{beg}")
        break
    elif option == 4:
        if level_game == 3 and power + intelligence + agility == 10:
                n = n + 3
                print("""\nВи маєте 3 додаткових очки. Додайте їх до характеристик(и),
рівень яких/якої бажаєте підвищити. Для інших - введіть 0.""")
                power31 = input("Додати до Сили: ")
                agility31 = input("Додати до Спритності: ")
                intelligence31 = input("Додати до Інтелекту: ")
                power31 = int(power31)
                agility31 = int(agility31)
                intelligence31 = int(intelligence31)
                while True:
                    if power31 + agility31 + intelligence31 != 3:
                        print("Ви маєте тільки 3 додаткових бали. Спробуйте ще раз.")
                        power31 = input("Додати до Сили: ")
                        agility31 = input("Додати до Спритності: ")
                        intelligence31 = input("Додати до Інтелекту: ")
                        power31 = int(power31)
                        agility31 = int(agility31)
                        intelligence31 = int(intelligence31)
                    else:
                        power = power + power31
                        agility = agility + agility31
                        intelligence = intelligence + intelligence31
                        break
                break

        elif level_game == 3 and power + intelligence + agility == 11:
                n = n + 2
                print("""\nВи маєте 2 додаткових очки. Додайте їх до характеристик(и),
рівень яких/якої бажаєте підвищити. Для інших - введіть 0.""")
                power32 = input("Додати до Сили: ")
                agility32 = input("Додати до Спритності: ")
                intelligence32 = input("Додати до Інтелекту: ")
                power32 = int(power32)
                agility32 = int(agility32)
                intelligence32 = int(intelligence32)
                while True:
                    if power32 + agility32 + intelligence32 != 2:
                        print("Ви маєте тільки 3 додаткових бали. Спробуйте ще раз.")
                        power32 = input("Додати до Сили: ")
                        agility32 = input("Додати до Спритності: ")
                        intelligence32 = input("Додати до Інтелекту: ")
                        power32 = int(power32)
                        agility32 = int(agility32)
                        intelligence32 = int(intelligence32)
                    else:
                        power = power + power32
                        agility = agility + agility32
                        intelligence = intelligence + intelligence32
                        break
                break

        elif level_game == 3 and power + intelligence + agility == 12:
                n += 1
                print("""\nВи маєте 1 додаткове очко. Додайте його до характеристики,
рівень якої бажаєте підвищити. Для інших - введіть 0.""")
                power33 = input("Додати до Сили: ")
                agility33 = input("Додати до Спритності: ")
                intelligence33 = input("Додати до Інтелекту: ")
                power33 = int(power33)
                agility33 = int(agility33)
                intelligence33 = int(intelligence33)
                while True:
                    if power33 + agility33 + intelligence33 != 1:
                        print("Ви маєте тільки 1 додатковий бал. Спробуйте ще раз.")
                        power33 = input("Додати до Сили: ")
                        agility33 = input("Додати до Спритності: ")
                        intelligence33 = input("Додати до Інтелекту: ")
                        power33 = int(power33)
                        agility33 = int(agility33)
                        intelligence33 = int(intelligence33)
                    else:
                        power = power + power33
                        agility = agility + agility33
                        intelligence = intelligence + intelligence33
                        break
                break
        else:
            break


    elif option == 5:
        exit(0)