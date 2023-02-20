n = abs(int(input('Введите число N ')))
con = 0
a = 2
for i in range(n):
    if con != 1:
        a = a ** i
        if a <= n:
            print(a, end=' ')
            a = 2
        else:
            con = 1
    else:
        i = n