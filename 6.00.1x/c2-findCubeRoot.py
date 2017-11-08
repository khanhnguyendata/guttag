x = int(input("Input an integer: "))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
elif x < 0:
    ans = -ans
    print(ans, "is the cube root of", x)
else:
    print(ans, "is the cube root of", x)
