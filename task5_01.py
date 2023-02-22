def power(x,n):
    if n==0:
        return 1
    if n/2==0:
        return power(x,n//2)*power(x,n//2)
    else:
        return power(x,n-1)*x
x=int(input('Введите А= '))
n=int(input('Введите B= '))
print(power(x,n))