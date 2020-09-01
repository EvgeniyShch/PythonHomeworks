while True:
    try:
        month = int(input("Введите номер месяца"))
        if month > 0 and month < 13:
            break
        else:
            print("Месяца нумеруются от 1 до 12")
    except Exception as error:
        print(f' Ошибка! \n {error} \n Введите целое число')

# решение через словарь
dict_season = {(1, 2, 12): 'Winter', (3, 4, 5): 'Srping', (6, 7, 8): 'Summer', (9, 10, 11): 'Autumn'}
for i in dict_season.keys():
    if month in i:
        print(f'Месяц {month} приходится на {dict_season.get(i)}')
        break

# решение через лист [0, 1, 2, 3]
list_season = ['Winter', 'Srping', 'Summer', 'Autumn']
for i in list_season:
    if list_season.index(i) == month//3 and month//12 == 0:
        print(list_season[month//3])
        break
    elif month//12 == 1:
        print(list_season[0])
        break