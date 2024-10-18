# coding=utf-8
a = []
for i in range(int(input("Введите количество элементов: "))):
    a.append(float(input("Введите элемент: ")))

mi = min(a)
ma = max(a)

s = [(2 * (x - mi) / (ma - mi)) - 1 for x in a]
print("массив в диапазоне:", s)


obrat = [int(((x + 1) / 2) * (ma - mi) + mi) for x in s]

print("обратное восстановление:", obrat)