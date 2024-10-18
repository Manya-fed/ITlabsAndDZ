#из массива размером 12 удалить все отрицательные элементы
a = []
s = []
for i in range(12):
    a.append(int(input('введите элемент массива: ')))

a = [x for x in a if x >= 0]

print(a)

