from module import *
FILES = {
    1: "input01.txt",
    2: "input02.txt",
    3: "input03.txt",
    4: "input04.txt"
}

for key, file_name in FILES.items():
    print(f"\nНабір векторів із {file_name}")
    print(f"1. Вектор, що має найбільшу розмірність: {max_size(file_name)}")
    print(f"2. Середня довжина вектора: {average(file_name)}")
    print(f"3. Кількість векторів, довжина яких більша за середню довжину векторів набору: {more_than_average(file_name)}")
    print(f"4. Вектор із максимальною найбільшою компонентою: {vect_max_value(file_name)}")
    print(f"5. Вектор із мінімальною найменшою комппонентою: {vect_min_value(file_name)}")