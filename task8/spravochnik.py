def all_contacts():
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
                print(line)

def find_contact(name):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)

def add_contact(new_contact):
    with open('phone_number.txt', 'a', encoding='utf8') as data:
        data.write('\n')
        data.write(new_contact)

def delet_contact(nickname_to_delete):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        lines = data.readlines()
    with open('phone_number.txt', 'w', encoding='utf8') as data:    
        for line in lines:
            if line.strip("\n") != "nickname_to_delete":
                data.write(line)

def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input ('Введите имя для поиска: ')
        find_contact(name)
    elif numb == 3:
        data=input("Введите новый контакт: ")
        add_contact(data) 
    elif numb == 4:
        nickname_to_delete=("ВВедите имя для удаления: ")
        delet_contact(nickname_to_delete)
while True:
    numb=int(input('Введите 1 для печати справочника; 2 для поиска контакта;'
    ' 3 для записи контакта; 4 для удаления контакта; 5 выхода из меню:  '))
    if numb == 5:
        break
    main_menu(numb)