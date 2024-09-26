
import math

a = 0.1
b = 1
h = 0.05

x = a
while x <= b + 0.00001:
    s = 1
    l = 1
    i = 0
    while abs(l) >= 0.0001:
        i += 1
        l = ((2*x)**i)/math.factorial(i)
        s += l
    s -= l
    y = math.exp(x) * math.exp(x)
    print(y, s)
    x += h