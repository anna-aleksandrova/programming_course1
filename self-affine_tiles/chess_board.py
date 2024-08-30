import random
import matplotlib.pyplot as plt

A = [
[2, 0],
[0, 2]
]

#список векторів (алфавіт)
D = [
[0, 0],
[1, 0],
[0, 1],
[1, 1]
]

q = 4   #модуль визначника матриці А

x_0 = [0.5, 0.5]

N = 100000
k = 100

result_points = [] #список для точок
c = [] #список для кольорів

for _ in range(N):
    x = x_0.copy()
    sequence_with_i = [] #для індексів і_1, i_2, ..., i_k
    sequence_with_d = [] #для векторів d_1, d_2, ..., d_k
    for i in range(k):
        ####результат множення A на x
        B_0 = A[0][0]*x[0] + A[0][1] * x[1]
        B_1 = A[1][0]*x[0] + A[1][1] * x[1]

        #### результат додавання результату множення і рандомного d із D
        result_for_x = []
        rand = random.choice(D)

        sequence_with_d.append(rand)                    

        res_0 = B_0 + rand[0]
        result_for_x.append(res_0)
        res_1 = B_1 + rand[1]
        result_for_x.append(res_1)


        # тут результат матричного множення і додавання векторів
        x = result_for_x
    result_points.append(x)

    for numb in range(2):                    #індекси i_1, i_2, ..., i_k векторів d_1, d_2, ..., d_k у списку D
        i = D.index(sequence_with_d[numb])   
        sequence_with_i.append(i)            
    sequence_with_i = sequence_with_i[::-1]
    C = 0                                        #унікальний номер m-тої послідовності d_1, ..., d_k
    for numb in range(2):                        # 0 < m < N
        C += (q**numb) * sequence_with_i[numb]
    c.append(C)
    

x, y = zip(*result_points)

 

plt.figure(figsize=(12, 12))
plt.scatter(x, y,
            s = 0.5,
            c = c,         # кольори передаються окремим списком 
            cmap='plasma'  # палітра
           )  

plt.legend()     # додати легенду (себто підпис) на малюнок
plt.show() 
