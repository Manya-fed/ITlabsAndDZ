# coding=utf-8

import math
a = []
r = int(input('введите значение'  + ': '))
while r !=0:

    print('Площадь какой фигуры  вы хотите вычилить: введите цифру 1, если круг, 2-равносторонний треугольник, 3-квадрат')
    d = str(input())
    x = True
    while x == True:
        if d == '1':

            print(r * r * math.pi)
            x = False

        elif d == '2':

            print((r * r * (3**0.5))/4)
            x = False

        elif d == '3':

            print(r * r)
            x = False

        else:
            print('введите другое число')
            d = str(input())

    r = int(input('введите значение' + ': '))

