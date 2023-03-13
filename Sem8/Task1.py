def input_data():
    with open("data.txt", "a") as f:
        for i in range(int(input("введите кол-во новых записей в справочник - "))):
            f.write(input("введите ФИО и номер телефона: ") + "\n".upper())


def read_data():
    with open("data.txt") as f:
        print(f.read())


def find_data():
    with open("data.txt") as f:
        find_feature = input("введите одну из характеристик для поиска(фио или телефон - ").upper()
        flag = False
        for i in f:
            list_feature = i.split()
            if find_feature in list_feature:
                print(i, end="")
                flag = True
        if not flag:
            print("такой записи не найдено")


def replace_data():
    edit_data = input("введите Имя или Фамилию для редактирования данных : ").upper()
    with open("data.txt") as f:
        list_temp = []
        for line in f:
            if edit_data in line.split():
                list_temp.append(input(f"{line} -->  ").upper() + "\n")
            else:
                list_temp.append(line)
    with open("data.txt", "w") as f:
        f.writelines(list_temp)


def remove_data():
    edit_data = input("введите Имя или Фамилию для удаления записи из справочника : ").upper()
    with open("data.txt") as f:
        list_temp = []
        for line in f:
            if edit_data in line.split():
                print(f'{line} удалена ')
                continue
            else:
                list_temp.append(line)
    with open("data.txt", "w") as f:
        f.writelines(list_temp)


while True:
    get_choice = (int(input(
        """\n введите 
         1 - для добавления записи,
         2 - для вывода всего справочника, 
         3 - для поиска, 
         4 - для изменения данных
         5 - для удаления данных         
         6 - для завершения работы : 
         => """)))
    match get_choice:
        case 1:
            input_data()
        case 2:
            read_data()
        case 3:
            find_data()
        case 4:
            replace_data()
        case 5:
            remove_data()
        case _:
            break