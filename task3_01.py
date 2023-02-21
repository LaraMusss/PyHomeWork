n=int(input('Введите n= '))
num_list=[]
for i in range(n):
    num=int(input("Введите num= "))
    num_list.append(num)
x=int(input("Введите x= "))
count=0
for i in range (len(num_list)):
    if x==num_list[i]:
        count+=1
print(count)