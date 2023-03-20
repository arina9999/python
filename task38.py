# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def info():
    print("""
    ------------------------------- \n
    1 - отобразить весь справочник 
    2 - найти aбонента по фамилии
    3 - добавить aбонента в справочник
    4 - удалить строку
    5 - закончить работу  
    ------------------------------- \n 
    """)
    '''choice = int(input())
    return choice '''



def del_empty():
    df = open('phone.txt')
    lines=df.readlines()
    non_empty_lines = (line for line in lines if not line.isspace())
    df_2 = open('phone.txt', 'w')
    df_2.writelines(non_empty_lines)
    df.close()
    df_2.close

def show_all():
    df = open('phone.txt', 'r')
    for line in df.readlines():
        print(line)
    df.close()
    comand()

def finde_line():
    df = open('phone.txt')
    str = input('Удалить: ')
    count = 0
    lines = df.readlines()
    for line in lines:
        if str in line:
            print(line, end="")
            count+=1
    if count == 0:
        print ('?')
    df.close()
    comand()

def new_row():
    df = open('phone.txt', 'a')
    print('Добавьте строку в справочник: ')
    df.write(f'\n{input()}')
    df.close()
    del_empty()
    comand()

def del_str():
    df = open('phone.txt')
    str = input('Удаление записи: ')
    count = 0
    lines = df.readlines
    str_for_del = ''
    for line in lines:
        if str in line:
            print('удалить: ')
            print(line, end="")
            str_for_del = line
            line = ''
            count+=1
    if count == 0:
        print('Не найдено: ')
        df.close()
        comand()
    else:
        acces = input('Подтвердите удаление: ')
        if acces.lower()=='yes':
            df.close()
            df.open('phone.txt', 'r').read()
            df = df.replace(str_for_del, '')
            df_2 = open('phone.txt', 'w')
            df_2.write(df)
            df_2.close()
            comand()
        else:
            df.close()
            comand()


def comand():
    comanda = int(input('Введите команду: '))
    if comanda == 1:
        show_all()
    elif comanda == 2:
        finde_line()
    elif comanda == 3:
        new_row()
    elif comanda == 4:
        del_str()
    elif comanda == 5:
        exit()

start = input('Открыть файл: ')
if start.lower()=='yes':
    try:
        data = open('phone.txt', 'r+')
    except:
        data = open('phone.txt', 'a')
    data.close()
    print(info)
    comand()

elif start.lower() == 'no':
    print('Выход')
    exit()
else:
    print('Введите корректное значение')
    exit()