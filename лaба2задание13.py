

import math
a = []
r = int(input('введите значение А'  + ': '))
g = int(input('введите значение B' + ': '))
while r !=0  and g != 0:
    print('Площадь какой фигуры  вы хотите вычилить: введите цифру 1, если прямоугольник, 2 - кольцо, заключенное между двумя окружностями, 3-равнобедренный треугольник')
    d = str(input())
    x = True
    while x == True:
        if d == '2':
            print(abs((r**2 - g**2) * math.pi))
            x = False
        elif d == '3':
            print((r/4)*(4*(g**2) - r**2)**0.5)
            x = False
        elif d == '1':
            print(r * g)
            x = False
        else:
            print('введите другое число')
            d = str(input())
    r = int(input('введите значение А' + ': '))
    g = int(input('введите значение B' + ': '))