x, y, x1, y1, x2, y2 = [int(el) for el in input().split()]
print("1") if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) else print("0")