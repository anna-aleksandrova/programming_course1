xc, yc = [int(el) for (el) in input().split()]
xa, ya = [int(el) for (el) in input().split()]
xb, yb = [int(el) for (el) in input().split()]

print("YES") if (xc - xa)*(yb - ya) == (xb - xa)*(yc - ya) else print("NO")

print("YES") if (xc - xa)*(yb - ya) == (xb - xa)*(yc - ya) and ((min(xa, xb) <= xc <= max(xa, xb) and min(ya, yb) <= yc <= max(ya, yb)) or (min(xa, xc) <= xb <= max(xa, xc) and min(ya, yc) <= yb <= max(ya, yc))) else print("NO")

print("YES") if (xc - xa)*(yb - ya) == (xb - xa)*(yc - ya) and min(xa, xb) <= xc <= max(xa, xb) and min(ya, yb) <= yc <= max(ya, yb) else print("NO")