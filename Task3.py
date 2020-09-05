def my_func(num1, num2, num3, *args, **kwargs):
    return sum([num1, num2, num3]) - min([num1, num2, num3])
       

while True:
    try:
        print("Данная программа суммирует 2 макс числа из введенных 3 чисел")
        a = float(input("Введите 1 число\n"))
        b = float(input("Введите 2 число\n"))
        c = float(input("Введите 3 число\n"))
        break
    except ValueError as error1:
        print("Аргументы содержат недопустимые значения", error1)
        print("Введите значения еще раз")


print(f'Сумма 2 максимальных чисел = {my_func(a, b, c)}')