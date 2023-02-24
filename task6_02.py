a=[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min=7
max=10
list_2=[]
print(a)
for i in range(len(a)):
    if min <= a[i] <= max:
        list_2.append(i)
        print(i)
