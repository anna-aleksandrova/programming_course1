"""
Підрахунок одиниць

Вхідні дані
В одному рядку дано два цілих числа a і b (1 <= a <= b <= 1016)

Вихідні дані
Вивести загальну кількість одиниць у числах від a до b, що
записані у двійковій системі.

Приклад
Вхідні дані #1 
2 12
Вихідні дані #1 
21

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15006992
"""
def sum_of_1_in_number(number):

   lst_with_remainders = []
   while number >= 2:
      lst_with_remainders.append(number % 2)
      number //= 2
   lst_with_remainders.append(number)
   amount_of_1 = lst_with_remainders.count(1)

   return amount_of_1

def sum_of_1_in_numb_from_0_to_n(number):
   if number == 0:
      return 0 
   if number % 2 != 0:
      return 2 * sum_of_1_in_numb_from_0_to_n(number // 2) + (number + 1) // 2
   return sum_of_1_in_numb_from_0_to_n(number - 1) + sum_of_1_in_number(number)

a, b = [int(el) for el in input().split()]
result = sum_of_1_in_numb_from_0_to_n(b) - sum_of_1_in_numb_from_0_to_n(a - 1)

print(result)