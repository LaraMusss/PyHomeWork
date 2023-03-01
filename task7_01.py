_list = [len([i for i in el if i.lower() in "уеёэоаыяию"])\
     for el in input("Введите фразу: ").split()]

if all([i == _list[0] for i in _list]):
    print("Парам пам-пам")
else:
   print("Пам парам")
#   def print_operation_table(operation, num_rows=6, num_columns=6):
#   for i in range(1, num_rows + 1):
#       a = []
#       for j in range(1, num_columns + 1):
#           a.append(str(operation(i, j)))
#       print(''.join(f'{e:<4}' for e in a))
#
#print_operation_table(lambda x, y: x * y)
# таблица, почемуто не залилась на гитхаб, повтор