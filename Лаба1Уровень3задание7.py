
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
        l = (x**(2*i))/(math.factorial(2*i))
        s += l
    s -= l
    y = (math.exp(x) + math.exp(-1*x))/2
    print(y, s)
    x += h