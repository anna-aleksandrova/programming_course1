"""
Дано массив цілих чисел а з n елементів і число k. Виведіть k-ий елемент 
у відсортованому масиві a (нумерація масиву починаєтся з 1).

Вхідні дані
Перший рядок містить два числа n і k (1 ≤ n ≤ 2000, 1 ≤ k ≤ n). Другий 
рядок містить n цілих чисел a[i] (1 ≤ i ≤ n, 1 ≤ a[i] ≤ 2000).

Вихідні дані
Виведіть k-ий елемент у відсортованому масиві а.

Приклад

Вхідні дані #1 
2 1
2 1
Вихідні дані #1
1 

Вхідні дані #2 
5 3
4 7 1 8 12
Вихідні дані #2 
7

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14751577

O(n*log(n))
"""
n, k = [int(el) for el in input().split()]
lst = [int(el) for el in input().split()]
lst.sort()
print(lst[k-1])