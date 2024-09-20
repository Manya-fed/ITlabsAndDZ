import math
a = 0.1
b = 1
h = 0.1
e = 0.0001
i = 0

while a <= b:
    x = a
    s = 999
    sum = 0
    while abs(s) > e:
        s = ((-1) ** i * ((x ** (2 * i)) / math.factorial(2 * i)))

        sum = sum + s

        if abs(s) < e:
            sum = sum - s
            y = math.cos(x)
            print(sum, y)
        i += 1
    

    a += 0.1


