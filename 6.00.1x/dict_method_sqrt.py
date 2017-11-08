x = -0.08
epsilon = 0.01
count = 0

low = min(-1.0, -abs(x))
high = max(1.0, abs(x))
ans = (low + high)/2
print("staring low", low, "starting high", high, "staring ans", ans)

while abs(ans**3 - x) >= epsilon:
    print("low", low, "high", high, "ans", ans, "delta", abs(ans**3 - x))
    if ans**3 > x:
        high = ans
    else:
        low = ans
    ans = (low + high)/2
    print("low", low, "high", high, "ans", ans, "delta", abs(ans**3 - x), "\n")

    count += 1

print("Count =", count)
print("Sqrt =", ans)