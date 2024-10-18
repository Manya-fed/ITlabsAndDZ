n = int(input('введите количество координат:'))
mi = 10 ** 8
s = []
a = []
for i in range(n):
    x, y = map(int, input('введите координаты №' + str(i + 1) + ' ').split())
    s.append([x, y])
for i in range(len(s)):
    g = (s[i][0] ** 2 + s[i][1] ** 2) ** 0.5
    a.append(g)
    mi = min(mi, g)
for i in range(len(a)):
    if a[i] == mi:
        print('точка ближайшая к началу координат - точка №' + str(i + 1))
        print('расстояние от нее до начала координат:', mi)
