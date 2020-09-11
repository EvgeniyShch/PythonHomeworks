with open("task3.txt", "r") as new_file_task3:
    dohod = []
    for i in new_file_task3:
        stroka = i.split()
        dohod.append(float(stroka[1]))
        if float(stroka[1]) < 20000:
            print(f'Оклад сотрудника {stroka[0]} менее 20 тыс = {stroka[1]}')
    print(f'Средняя зарплата сотрудников {sum(dohod)/len(dohod)}')