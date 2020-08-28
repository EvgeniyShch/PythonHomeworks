while True:
    try :
        Income = float(input("Введите выручку компании"))
        Expenses = float(input("Веедите расходы компании"))
        if Income and Expenses >0:
            break
        else:
            print("Введите данные > 0")
    except :
        print("Введите правильные данные")

if Income < Expenses :
    print("Вы работаете в убыток, срочно поменяйте руководоство!")
else :
    print(f'Вы работаете в прибыль, Ваша рентабельность {((Income-Expenses)/Income)*100//1} процентов')
    Employees = int(input("Введите количество сотрудников"))
    print(f'Прибыль на одного сотрудника составляет : {(Income-Expenses)/Employees//1}')