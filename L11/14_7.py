#lst = [0, 3, 4, 5, 6, 23, 4, 345, 453, 23456]
lst_add = lst.copy()
counter = 0
suma = 0
while True:
    try:
        el = lst.pop(0)
    except IndexError:
        print(f"Кількість елементів у списку: {counter}")
        print(f"Сума елементів у списку: {suma}")
        break
    else:
        counter += 1
        suma += el

max_ratio = 0
i = 0
while True:
    try:
        ratio = lst_add[i + 1] / lst_add[i]
    except ZeroDivisionError:
        print("Неможливо знайти максимальне відношення: список містить нуль.")
        break
    except IndexError:
        print(f"Максимальне відношення між сусіднімми елементами: {max_ratio}")
        break
    else:
        if ratio > max_ratio:
            max_ratio = ratio
        i += 1


