n=int(input("Введите n: "))
m=int(input("Введите m: "))
k=int(input("Введите k: "))
if k<n*m and ((k%n==0) or (k%m==0)):
    print("Можно разломить на", k ,"дол.")
else:
    print("Нельзя разломить на", k ,"дол.")