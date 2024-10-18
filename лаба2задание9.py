n = int(input('введите количество пловцов:'))
a = []
s = []
for i in range(n):
    a.append(int(input('результат пловца номер ' + str(i+1) + ': ' )))
if a.count(min(a)) == 1:
    print('лучший результат: '+ str(min(a)), "победил пловец номер " + str(a.index(min(a)) + 1 ))
else:
    for j in range(len(a)):
        if a.count(a[j])>1 and a[j] == min(a):
            s.append(str(j+1))
    s = ' '.join(s)
    print("лучший результат: " + str(min(a))  + " победили пловцы номер " + s)