"""
Істина, схована в рекурентності

Вхідні дані #1 
1234 1234 4
2323 99999999999 8
4 99999 9
888 888 8
0 0 0

Вихідні дані #1 
Case #1: 736
Case #2: 39087387
Case #3: 494777344
Case #4: 91255296

Вхідні дані #2
3 1 1
3 2 2
3 4 1
0 0 0

Вихідні дані #1
Case #1: 3
Case #2: 9
Case #3: 1

https://www.eolymp.com/uk/submissions/15205139
"""
def f(n, r, k):
	if n == 0 and r == 0:
		return 1
	elif n > 0 and r >= 0 and r < n * (k - 1) + 1:
		suma = 0
		for i in range(0, k):
			suma += f(n - 1, r - i, k)
		return suma
	else:
		return 0

result = []
while True:
    k, n, t = [int(el) for el in input().split()]
    if k == 0 and n == 0 and t == 0:
        break
    else:
        suma = 0
        for i in range(0, n * (k-1) + 1):
	        suma += f(n, i, k)
        x = suma % (10 ** t)
        result.append(x)

for i in range(len(result)):
    print(f"Case #{i + 1}: {result[i]}")


