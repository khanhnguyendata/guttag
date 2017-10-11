def main():
    num1 = 7
    num2 = 4
    print(gcd(num1, num2))


def gcd(x, y):
    # print(x, y)
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)
