n = int(input('Введите n= '))
a = [0]*n
a[0] = int(input('Введите a[0]= '))
d = int(input('Введите d= '))
print(a[0],end=' ')
for i in range(1,n):
    a[i]= a[i-1]+d
    print(a[i],end=' ')
