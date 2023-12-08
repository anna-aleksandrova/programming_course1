"""
За заданим натуральним числом n вивести усі перестановки з цілих чисел від 
1 до n у лексикографічному порядку.

Вхідні дані
Одне натуральне число n (1≤ n ≤8).

Вихідні дані
Вивести усі перестановки з цілих чисел від 1 до n у лексикографічному порядку. 
Кожну перестановку слід виводити в окремому рядку.

Приклад

Вхідні дані #1 
3
Вихідні дані #1 
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15126991
"""
def permutations(elements):
	if len(elements) == 1:
		return [elements]
	else:
		perms = permutations(elements[1:])
		fixed_el = [elements[0]]
		_result = []

		for perm in perms:
			for i in range(len(perm) + 1):
				_result.append(perm[:i] + fixed_el + perm[i:])

		return _result

n = int(input())
elements = [el for el in range(1, n + 1)]
result = permutations(elements)           # список списків із усіма можливими перестановками

_add = []
for el in result:
	s = ' '
	_el = s.join(map(str, el))
	_add.append(_el)
_add.sort()                               # відсортований список перестановок

for el in _add:
	print(el)

