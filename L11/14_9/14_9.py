try:
    with open("context.txt") as main:
        files = []
        for string in main.readlines():
            for el in string.split():
                files.append(el)
except FileNotFoundError:
    print("Файл \"content.txt\" не існує за вказаним розташуванням.")
else:
    suma = 0
    for i in range(len(files)):
        try:
            with open(files[i]) as file:
                strings = file.readlines()
        except FileNotFoundError:
            print(f"Файл \"{files[i]}\" не існує за вказаним розташуванням.")
            suma = 0
            break
        else:
            try:
                for string in strings:
                    for el in string.split():
                        el = float(el)
                        suma += el
            except ValueError:
                suma = 0
                print(f"Файл \"{files[i]}\" містить не лише дійсні числа.")
                break
    print(suma)