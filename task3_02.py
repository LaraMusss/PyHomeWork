n=int(input('Введите n= '))
num_list=[]
for i in range(n):
    num=int(input("Введите num= "))
    num_list.append(num)
x=int(input("Введите x= "))
if x==num_list[i]:
    print(x)
elif (x+1)==num_list[i] or (x-1)==num_list[i]:
    print(num_list[i])
elif (x+2)==num_list[i] or (x-2)==num_list[i]:
    print(num_list[i])
elif (x+3)==num_list[i] or (x-3)==num_list[i]:
    print(num_list[i])
