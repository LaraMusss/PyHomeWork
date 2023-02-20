n=int(input("Введите кол-во монет: "))
count_orel=0
count_resh=0
for i in range(n):
    money=int(input("Сторона монеты: "))
    if money==0:
        count_orel+=1
    else:
        count_resh+=1
print('Орел=', count_orel)
print('Решка=', count_resh)
if count_orel > count_resh:
    print('Перевернуть минимум раз', count_resh)
else: print('Перевернуть минимум раз', count_orel)

