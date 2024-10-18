#все отрицательные передвинуть в конец сохранив последовательность

a = [int(x) for x in input("введите в строку через пробел все элементы массива: ").split()]
s = []
k = []
for i in a:
    if i < 0:
        s.append(i)
    else:
        k.append(i)
a2s2 = k + s
print(a2s2)