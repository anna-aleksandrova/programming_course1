"""
Просте додавання

Вхідні дані
Складається з декількох тестів. Кожен рядок містить два невід'ємних цілих числа p та q 
(p ≤ q), відокремлених пропуском. p та q є 32-бітними знаковими цілими. Останній рядок містить 
два від'ємні цілі числа та не обробляється.

Вихідні дані
Для кожної пари p та q в окремому рядку вивести значення S (p, q).

Приклад

Вхідні дані #1 
1 10
10 20
30 40
-1 -1

Вихідні дані #1 
46
48
52

https://www.eolymp.com/uk/submissions/15127378
"""
def F(i):
	if i % 10 > 0:
		return i % 10
	elif i == 0:
		return 0
	else:
		return F(i / 10)

def S(p, q):
	suma = 0
	for i in range(p, q + 1):
		suma += F(i)
	return int(suma)

results = []
while True:
	p, q = [int(el) for el in input().split()]
	if p == -1 and q == -1:
		break
	else:
		results.append(S(p, q))

for el in results:
	print(el)