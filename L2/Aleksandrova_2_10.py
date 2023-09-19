x = abs(int(input()))
digit_3 = x % 10
x1 = x // 10
digit_2 = x1 % 10
digit_1 = x1 // 10
if digit_1 > digit_3:
    print (digit_1)
elif digit_3 > digit_1:
    print(digit_3)
else:
    print("=")