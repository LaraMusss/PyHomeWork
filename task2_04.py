n = int(input('Введите число N '))
a = 2
for i in range(n):
    a = a ** i
    if a <= n:
        print(a)
        a = 2