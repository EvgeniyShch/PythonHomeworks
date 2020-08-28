Income = int(input("Введите выручку компании"))
Expenses = int(input("Веедите расходы компании"))

if Income < Expenses :
    print("Вы работаете в убыток, срочно поменяйте руководоство!")
else :
    print(f'Вы работаете в прибыль, Ваша рентабельность {((Income-Expenses)/Income)*100//1} процентов')
    Employees = int(input("Введите количество сотрудников"))
    print(f'Прибыль на одного сотрудника составляет : {Income/Employees*100//1}')