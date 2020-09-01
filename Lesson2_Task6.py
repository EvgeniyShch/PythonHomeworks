while True:
    try:
        number = int(input("Введите количество значений массива\n"))
        if number > 0:
            break
        else:
            print("Введите целое число > 0")
    except Exception as error:
        print(f' Ошибка! \n {error} \n Введите целое число')


# Реализация аналитики о товарах
dict1 = {"product": [], "price": [], "qty": [], "measure": []}

for i in range(number):
    for dictkey in dict1.keys():
        if dictkey == "price" or dictkey == "qty":
            dictvalue = int(input(f"Введите {dictkey}\n"))
        else:
            dictvalue = input(f"Введите {dictkey}\n")        
        dict1[dictkey].append(dictvalue)
print("-"*50) # разделители для удобства и наглядности
print("Реализация аналитики о товарах")
print("-"*50)
print(dict1)

# Реализация готовой структуры
print("-"*50)
print(f"Далее введите значения массива еще {number} раз")
print("-"*50)
list1 = []
for i in range(number):
    dict2 = dict({"product": input(f"Введите product\n"), "price": int(input(f"Введите price\n")), "qty": int(input(f"Введите qty\n")), "measure": input(f"Введите measure\n")})
    list1.append((i+1, dict2))
print("-"*50)
print("Реализация готовой структуры")
print("-"*50)
print(list1)