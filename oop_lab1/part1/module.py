import math
from copy import copy
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def attrs(self):
        return ["a", "b", "c"]
    
    def perimeter(self):
        if not (self.a < self.b + self.c and
                self.b < self.a + self.c and
                self.c < self.a + self.b):
            perimeter = 0
        else:
            perimeter = self.a + self.b + self.c
        return perimeter
    
    def area(self):
        if not (self.a < self.b + self.c and
        self.b < self.a + self.c and
        self.c < self.a + self.b):
            area = 0
        else:
            p = (self.a + self.b + self.c) / 2
            area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return area

    def __repr__(self):
        return f"Triangle: a = {self.a}, b = {self.b}, c = {self.c})"

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def attrs(self):
        return ["a", "b"]

    def perimeter(self):
        return 2 * (self.a + self.b)  

    def area(self):
        return self.a * self.b

    def __repr__(self):
        return f"Rectangle: a = {self.a}, b = {self.b}"
    
class Trapeze:

    def __init__(self, base1, base2, lat1, lat2):
        self.b1 = base1
        self.b2 = base2
        self.l1 = lat1
        self.l2 = lat2

    def attrs(self):
        return ["base1", "base2", "lat1", "lat2"]

    def perimeter(self):
        return self.b1 + self.b2 + self.l1 + self.l2
    
    def area(self):
        a = min(self.b1, self.b2)
        b = max(self.b1, self.b2)
        c = self.l1
        d = self.l2
        if b - a == 0:
            area = 0
        else:
            p = (c + d + b - a) / 2
            temp_area = (p * (p - c) * (p - d) * (p - b + a)) ** 0.5
            h = 2 * temp_area / (b - a)
            area = (a + b) * h / 2
        return area

    def __repr__(self):
        return f"Trapeze: base1 = {self.b1}, base2 = {self.b2}, lat1 = {self.l1}, lat2 = {self.l2}"
    
class Parallelogram:

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def attrs(self):
        return ["a", "b", "h"]

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.h * self.a       # вважаємо, що h - висота, проведена до сторони a

    def __repr__(self):
        return f"Parallelogram: a = {self.a}, b = {self.b}, h = {self.h}"
        
class Circle:
    def __init__(self, r):
        self.r = r

    def attrs(self):
        return ["r"]

    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r ** 2

    def __repr__(self):
        return f"Circle: radius = {self.r}"

CLASSES = {
    "Triangle": Triangle(a = 0, b = 0, c = 0),
    "Rectangle": Rectangle(a = 0, b = 0),
    "Trapeze": Trapeze(base1 = 0, base2 = 0, lat1 = 0, lat2 = 0),
    "Parallelogram": Parallelogram(a = 0, b = 0, h = 0),
    "Circle": Circle(r = 0)
}

def str_to_obj(string):
    """Функція за рядком повертає об'єкт певного класу із значеннями атрибутів, що задані в цьому рядку.

    :param string: рядок
    :return: об'єкт
    """
    obj = copy(CLASSES[string.split()[0]])
    attrs = obj.attrs()
    attrs_values = [float(el) for el in string.split()[1:]]
    for i in range(len(attrs)):
        setattr(obj, attrs[i], attrs_values[i])
    return obj

def figure_max_area(file_name):
    """Функція за назвою файлу повертає об'єкт (за допомогою __repr__), що має найбільшу площу.

    :param file_name: рядок, у якому міститься ім'я файлу
    :return: об'єкт, що має найбільшу площу
    """
    AREAS = {}
    with open(file_name) as f:
        for line in f.readlines():
            AREAS[line] = str_to_obj(line).area()
    max_value = max(AREAS.values())
    res = []
    for line, value in AREAS.items():
        if value == max_value:
            res.append(str_to_obj(line).__repr__())
    return res

def figure_max_perimeter(file_name):
    """Функція за назвою файлу повертає об'єкт (за допомогою __repr__), що має найбільший периметр.

    :param file_name: рядок, у якому міститься ім'я файлу
    :return: об'єкт, що має найбільший периметр
    """
    PERIMETERS = {}
    with open(file_name) as f:
        for line in f.readlines():
            PERIMETERS[line] = str_to_obj(line).perimeter()
    max_value = max(PERIMETERS.values())
    res = []
    for line, value in PERIMETERS.items():
        if value == max_value:
            res.append(str_to_obj(line).__repr__())
    return res

def output(file_name):
    """Функція за назвою файла виводить фігуру(фігури), що мають найбільшу площу,
    фігуру(фігури), що мають найбільший периметр

    :param file_name
    :return: рядок, у якому міститься ім'я файлу
    """
    with open(file_name) as f:
        res_areas = figure_max_area(file_name)
        res_perimeters = figure_max_perimeter(file_name)

    print(f"-------Файл {file_name}-------\n")

    if len(res_areas) == 1:
        print("Фігура, що має найбільшу площу: ")
        print(res_areas[0])
    else:
        print("Фігури, що мають найбільшу площу: ")
        for i in range(len(res_areas)):
            print(res_areas[i])
    print("")
    if len(res_perimeters) == 1:
        print("Фігура, що має найбільший периметр: ")
        print(res_perimeters[0])
    else:
        print("Фігури, що мають найбільший периметр: ")
        for i in range(len(res_perimeters)):
            print(res_perimeters[i])
    print("")