n = int(input())
product = 1
if n >= 8:
    for i in range(1, n+1):
        if i % 8 == 0:
            product *= i
        else:
            pass
    print(product)
else:
    print(0)
