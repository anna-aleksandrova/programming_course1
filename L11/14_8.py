c_runtime = 0
c_type = 0
c_value = 0
while True:
    expr = input()
    if expr == "досить":
        print(f"Runtime errors: {c_runtime}")
        print(f"Type errors: {c_type}")
        print(f"Value errors: {c_value}")
        break
    try:
        x = float(expr)
    except ValueError:
        print("Введений вираз не є числом.")
    else:
        if x > 9:
            c_runtime += 1
        elif x < 0:
            c_type += 1
        elif not expr.isdecimal():
            c_value += 1