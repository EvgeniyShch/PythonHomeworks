with open("task6.txt", "r") as new_file_task6:
    summa_temp, summa_final = 0, 0
    dict_examle, string = {}, ""
    for i in new_file_task6:
        stroka = i.split(" ", 1) # пошел путем разделения строки на 2 части и прогонки 2 части на цифры для суммы часов
        for i in stroka[1]: # но интересны другие варианты решений
            if i.isdigit():
                string += str(i)
                summa_temp = int(string)
            else:
                summa_final += summa_temp
                summa_temp, string = 0, ""
                continue
        dict_examle[f'{stroka[0]}'] = f'{summa_final}'
        summa_final = 0
    print(dict_examle)