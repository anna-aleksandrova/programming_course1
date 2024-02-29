class Vector:

    def __init__(self, vector: str):

        if isinstance(vector, Vector):
            self.elements = vector.elements
        else:
            self.elements = [float(el) for el in vector.split()]

    def __repr__(self):
        return self.elements

    def size(self):
        return len(self.elements)
    
    def dimension(self):
        return f"1 x {self.size()}"
    
    def average(self):
        if self.size() == 0:
            return None
        else:  
            sum = 0
            for el in self.elements:
                sum += el
            return sum / self.size()

    def max_el(self):
        max = self.elements[0]
        for el in self.elements:
            if el > max:
                max = el
        return max

    
    def min_el(self):
        min = self.elements[0]
        for el in self.elements:
            if el < min:
                min = el
        return min

def sizes(name):
    """Функція за назвою файлу повертає словник, у якому парі ключ-значення
    відповідає пара рядок-довжина вектора, де рядок містить координати відповідного вектора.

        :param name: ім'я файлу
        :return: словник
        """
    SIZES = {}

    with open(name) as file:
        for line in file.readlines():
            SIZES[line] = Vector(line).size()
    return SIZES

def max_size(name):
    """Функція за назвою файлу повертає вектор із найбільшою розмірністю/довжиною.

    :param name: ім'я файлу
    :return: вектор із найбільшою розмірністю
    """
    SIZES = sizes(name)
    max_size = max(SIZES.values())
    res = None
    for vector, size in SIZES.items():
        if size == max_size:
            res = Vector(vector)
    return res.__repr__()


def average(name):
    """Функція за назвою файлу повертає середнє значення довжини його векторів.

    :param name: ім'я файлу
    :return: середнє значення довжини векторів із набору
    """
    SIZES = sizes(name)
    sum = 0
    for value in SIZES.values():
        sum += value
    return sum / len(SIZES.keys())

def more_than_average(name):
    """Функція за назвою файлу повертає кількість векторів,
    довжина яких більша за середню довжину векторів набору.

    :param name: ім'я файлу
    :return: кількість векторів, що задовольняють умову
    """
    aver = average(name)
    SIZES = sizes(name)
    amount = 0
    for size in SIZES.values():
        if size > aver:
            amount += 1
    return amount

def dict_max_elements(lines_vectors):
    """Функція за списком рядків повертає словник, у якому парі ключ-значення
    відповідає пара рядок - максимальна компонента вектора, де рядок містить
    компоненти відповідного вектора.

    :param lines_vectors: список рядків, кожен із яких містить компоненти відповідного вектора
    :return: словник
    """
    MAX_ELEMENTS = {}

    for line in lines_vectors:
        if line.split() == '\n'.split():
            pass
        else:
            MAX_ELEMENTS[line] = Vector(line).max_el()
    return MAX_ELEMENTS

def dict_min_elements(lines_vectors):
    """Функція за списком рядків повертає словник, у якому парі ключ-значення
    відповідає пара рядок - мінімальна компонента вектора, де рядок містить
    компоненти відповідного вектора.

    :param lines_vectors: список рядків, кожен із яких містить компоненти деякого вектора
    :return: словник
    """
    MIN_ELEMENTS = {}

    for line in lines_vectors:
        if line.split() == '\n'.split():
            pass
        else:
            MIN_ELEMENTS[line] = Vector(line).min_el()
    return MIN_ELEMENTS

def vect_max_value(name):
    """Функція за назвою файлу повертає вектор, що має найбільше значення максимальної
    компоненти. Якщо таких векторів більше за один, то функція повертає той,
    у якого найменше значення мінімальної компоненти.

    :param name: ім'я файлу
    :return: вектор, що задовольняє умову
    """
    with open(name) as file:
        lines = file.readlines()
    MAX_ELEMENTS = dict_max_elements(lines)
    max_value = max(MAX_ELEMENTS.values())
    res = []
    for vector, value in MAX_ELEMENTS.items():
        if value == max_value:
            res.append(vector)
    if len(res) == 1:
        return Vector(res[0]).__repr__()
    else:
        MIN_ELEMENTS = dict_min_elements(res)
        min_value = min(MIN_ELEMENTS.values())
        res = None
        for vector, value in MIN_ELEMENTS.items():
            if value == min_value:
                res = vector
        return Vector(res).__repr__()

def vect_min_value(name):
    """Функція за назвою файлу повертає вектор, що має найменше значення мінімальної
    компоненти. Якщо таких векторів більше за один, то функція повертає той,
    у якого найбільше значення максимальної компоненти.

    :param name: ім'я файлу
    :return: вектор, що задовольняє умову
    """
    with open(name) as file:
        lines = file.readlines()
    MIN_ELEMENTS = dict_min_elements(lines)
    min_value = min(MIN_ELEMENTS.values())
    res = []
    for vector, value in MIN_ELEMENTS.items():
        if value == min_value:
            res.append(vector)
    if len(res) == 1:
        return Vector(res[0]).__repr__()
    else:
        MAX_ELEMENTS = dict_max_elements(res)
        max_value = max(MAX_ELEMENTS.values())
        res = None
        for vector, value in MAX_ELEMENTS.items():
            if value == max_value:
                res = vector
        return Vector(res).__repr__()