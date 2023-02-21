n=int(input('Введите кол-во 1 множества n= '))
set_1=set()
for i in range(n):
    num=int(input("Введите num= "))
    set_1.add(num)
m=int(input('Введите кол-во 2 множества m= '))
set_2=set()
for i in range(m):
    num=int(input("Введите num= "))
    set_2.add(num)

i=set_1.intersection(set_2)
print(i)
