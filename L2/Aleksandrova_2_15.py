a, b, c = [int(el) for (el) in input().split()]
if a != 0:
    D = b**2 - 4*a*c
    if D < 0:
        print("No roots")
    elif D == 0:
        x = - b / (2*a)
        print("One root:", int(x))
    else:
        x1 = (- b - D**0.5) / (2*a)
        x2 = (- b + D**0.5) / (2*a)
        print("Two roots:", int(min(x1, x2)), int(max(x1, x2)))