from random import randint
string = ""
with open("task5.txt", "w") as new_file_task5_1:
    numbers = [randint(1, 100) for i in range(100)]
    for i in numbers:
        string += str(i) + " " 
        # string += " ".join(str(i)) - не понимаю почему в данном случае метод Join работает неправильно, просьба объяснить
    new_file_task5_1.writelines(string)
with open("task5.txt", "r") as new_file_task5_2:
    for i in new_file_task5_2:
        stroka = i.split()
    summa = sum([int(i) for i in stroka])
print(f'Сумма чисел из файла {new_file_task5_2.name} = {summa}')