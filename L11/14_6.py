while True:
    try:
        a, b, c = [float(el) for el in input("Введіть коефіцієнти a, b, c: ").split()]
        assert a != 0
        D = b ** 2 - 4 * a * c
        assert D >= 0
    except AssertionError:
        print("Неправильно введені дані.")
    except ValueError:
        print("Неправильно введені дані.")
    else:
        break
if D == 0:
    print(f"x = {(- b + D ** 0.5) / (2 * a)}")
else:
    print(f"x1 = {(- b + D ** 0.5) / (2 * a)}")
    print(f"x2 = {(- b - D ** 0.5) / (2 * a)}")

