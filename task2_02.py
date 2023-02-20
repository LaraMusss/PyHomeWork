sum=int(input('Введите сумму чисел х и у= '))
p=int(input('Введите произведение чисел х и у= '))
x=1
while x<=1000:
    if p%x==0:
        y=p//x
        if x+y==sum:
            print(f'x={x}, y={y}')
    x+=1
