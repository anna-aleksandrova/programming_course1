def columns(matrix):
    matrix_columns = []
    for j in range(len(matrix[0])):
        column = []
        for i in range(len(matrix)):
            column.append(matrix[i][j])
        matrix_columns.append(column)
    return matrix_columns

def square_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    else:
        return True

def del_zero_rows(matrix):
    res = []
    for row in matrix:
        for el in row:
            if el != 0:
                res.append(row)
                break
    return res

def zero_row(row):
    for el in row:
        if el != 0:
            return False
    else:
        return True

def vectors_proportional(vect1, vect2):
    if len(vect1) != len(vect2):
        print("Вектори різної довжини.")
    else:
        for i in range(len(vect1)):
            if vect2[i] != 0:
                k = vect1[i] / vect2[i]
                break
        for i in range(len(vect1)):
            if vect1[i] != k * vect2[i]:
                return False
        else:
            return True

def del_prop_vect(matrix):
    for i in range(0, len(matrix) // 2 + 1):
        for j in range(len(matrix) // 2, len(matrix)):
            if vectors_proportional(matrix[i], matrix[j]):
                matrix[i] = matrix[j]
    res = []
    for row in matrix:
        if row not in res:
            res.append(row)
    return res

#--------------------1--------------------
def row_isnumeric(row):
    _row = row.replace(".", "").replace("-", "")

    for el in row.split():
        if el == ".":
            return False
        if el == "-":
            return False
    else:
        for el in _row.split():
            if not el.isnumeric():
                return False
        else:
            return True

def matrix_input():
    while True:
        try:
            m = int(input("Введіть кількість рядків: "))
        except ValueError:
            print("Неправильно введене значення.")
        else:
            if m < 1:
                print("Неправильно введене значення.")
            else:
                break
    while True:
        try:
            n = int(input("Введіть кількість стовпців: "))
        except ValueError:
            print("Неправильно введене значення.")
        else:
            if n < 1:
                print("Неправильно введене значення.")
            else:
                break
    matrix = []
    for row_number in range(1, m + 1):
        while True:
            row = input(f"Введіть рядок №{row_number}: ")
            if not row_isnumeric(row):
                print("Усі елементи рядка мають бути числовими.")
            elif len(row.split()) != n:
                print("Кількість елементів у рядку не відповідає вказаній кількості стовпчиків.")
            else:
                break
        matrix.append(list(map(float, row.split())))
    return matrix

#--------------------2--------------------
def matrix_output(matrix):
    col = columns(matrix)
    for i in range(len(col)):
        col[i] = list(map(str, col[i]))
        max_len = 0
        for el in col[i]:
            if len(el) > max_len:
                max_len = len(el)
        for k in range(len(col[i])):
            difference = max_len - len(col[i][k])
            col[i][k] += " " * difference
    rows = columns(col)
    for row in rows:
        print(*row)

#--------------------3--------------------
def dot_product(row_matrix1, column_matrix2):
    res = 0
    for i in range(len(row_matrix1)):
        res += row_matrix1[i] * column_matrix2[i]
    return res

def matrix_product(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Неможливо помножити матриці.")
    else:
        res_product = [[0] * len(matrix2[0]) for i in range(len(matrix1))]
        matrix2_col = columns(matrix2)
        for i in range(len(res_product)):
            for j in range(len(res_product[0])):
                res_product[i][j] = dot_product(matrix1[i], matrix2_col[j])
        return res_product

#--------------------4--------------------
def matrix_vector_pr(matrix, vector):
    if len(matrix[0]) != len(vector):
        print("Множення неможливе.")
    else:
        res = [0] * len(matrix)
        for i in range(len(matrix)):
            res[i] = dot_product(matrix[i], vector)
        return res

#--------------------5--------------------
def vector_matrix_pr(vector, matrix):
    if len(matrix) != 1:
        print("Множення неможливе.")
    else:
        res = [[0] * len(matrix[0]) for i in range(len(vector))]
        for i in range(len(vector)):
            for j in range(len(matrix[0])):
                res[i][j] = vector[i] * matrix[0][j]
        return res

#--------------------6--------------------
def perm_of_rows(matrix, n1, n2):
    if n1 not in range(len(matrix)) or n2 not in range(len(matrix)):
        print("Рядок із таким номером відсутній.")
    else:
        matrix[n1], matrix[n2] = matrix[n2], matrix[n1]
        return matrix

#--------------------7--------------------
def perm_of_columns(matrix, n1, n2):
    n1 -= 1
    n2 -= 1
    if n1 not in range(len(matrix[0])) or n2 not in range(len(matrix[0])):
        print("Стовпчик із таким номером відсутній.")
    else:
        matrix_columns = columns(matrix)
        matrix_columns[n1], matrix_columns[n2] = matrix_columns[n2], matrix_columns[n1]
        res = columns(matrix_columns)
        return res

#--------------------8--------------------
def row(matrix, row_numb):
    row_numb -= 1
    if row_numb not in range(len(matrix)):
        print("Рядок із таким номером відсутній.")
    else:
        return matrix[row_numb]

#--------------------9--------------------
def vect_by_numb(vector, number):
    v = [0] * len(vector)
    for i in range(len(vector)):
        v[i] = vector[i] * number
    return v

#--------------------10--------------------
def v_subtraction(matrix, vector):
    if len(matrix[0]) != len(vector):
        print("Неможливо виконати віднімання.")
    else:
        for row in matrix:
            for i in range(len(row)):
                row[i] -= vector[i]
    return matrix

#--------------------11--------------------
def vectors_addition(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Неможливо додати вектори.")
    else:
        res = [0] * len(vector1)
        for i in range(len(vector1)):
            res[i] = vector1[i] + vector2[i]
        return res

#--------------------a--------------------
def upper_triangular(matrix):
    if not square_matrix(matrix):
        print("Матриця не є квадратною.")
    else:
        n = 0
        while n < len(matrix) - 1:
            if matrix[n][n] != 0:
                for k in range(n + 1, len(matrix)):
                    op_1 = vect_by_numb(matrix[n], - matrix[k][n] / matrix[n][n])
                    matrix[k] = vectors_addition(op_1, matrix[k])
                    for el in range(len(matrix[k])):
                        matrix[k][el] = round(matrix[k][el], 3)
            else:
                if not zero_row(matrix[n + 1]):
                    matrix = perm_of_rows(matrix, n, n + 1)
                    n -= 1
                else:
                    n += 1
            n += 1
        return matrix

def upper_triangular_det(matrix):
    if not square_matrix(matrix):
        print("Матриця не є квадратною.")
    else:
        n = 0
        while n < len(matrix) - 1:
            if matrix[n][n] != 0:
                for k in range(n + 1, len(matrix)):
                    op_1 = vect_by_numb(matrix[n], - matrix[k][n] / matrix[n][n])
                    matrix[k] = vectors_addition(op_1, matrix[k])
            else:
                if not zero_row(matrix[n + 1]):
                    matrix = perm_of_rows(matrix, n, n + 1)
                    n -= 1
                else:
                    n += 1
            n += 1
        return matrix

#--------------------b--------------------
def rank(matrix):
    res = upper_triangular(matrix)
    res = del_zero_rows(res)
    res = del_prop_vect(res)
    return len(res)


#--------------------c--------------------
def det(matrix):
    matrix = upper_triangular_det(matrix)
    det = 1
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det
