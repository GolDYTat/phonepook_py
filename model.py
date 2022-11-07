import os

path = 'phonebook.txt'
contacts = []

def read_file():
    global contacts
    with open(path) as f:
        contacts = [i.strip('\n').split(';') for i in f.readlines()]
    return contacts

def get_contacts():
    global contacts
    return contacts  

def add_contact():
    global contacts
    name = input(f'Введите имя: ')
    phone = input(f'Введите телефон: ')
    comment = input(f'Введите комментарий: ')
    new_id = str(len(contacts))
    new_contact = [new_id, name, phone, comment]
    contacts.append(new_contact)     

def save_file():
    global contacts
    with open(path, 'w', encoding = 'utf_8') as f:
        for i in range(0, len(contacts)):
            s = " ".join(contacts[i])
            s = s.replace(' ',';')
            f.write(f'{s} \n')

def change_contact():
    global contacts
    id = int(input(f'Введите id контакта: '))
    info = int(input(f'Введите 1, если хотите изменить имя: \
                \nВведите 2,  если хотите изменить телефон: \
                \nВведите 3,  если хотите изменить комментарий: \
                \n'))
    info_replace = input(f'Введите новую информацию: ')
    data = [i.strip('') for i in contacts[id]]
    data[info] = info_replace
    contacts[id] = data
    return contacts[id]

def delete_contact():
    global contacts
    id = int(input(f'Введите id контакта: '))
    for i in contacts:
        i[0] = int(i[0])
        if i[0] > id:
           i[0] -= 1 
    contacts.pop(int(id))
    return contacts
    

def search_contact():
    search = input(f'Введите ключевое слово или номер: ')
    for i in contacts:
        for j in i:
            if search == j:
                print(f'\n {i} \n')
    