def func_division (num1, num2):
	try :
		return round(num1 / num2, 2)
	except ZeroDivisionError as error1:
		return "Ошибка - недопустимое деление на 0", error1
	

while True:
    try:
        print("Данная программа делит 1 число на 2")
        a = float(input("Введите делимое\n"))
        b = float(input("Введите делитель\n"))
        break
    except ValueError as error2:
        print("Аргументы содержат недопустимые значения", error2)
        print("Введите значения еще раз")

print(f'Результат деления = {func_division(a, b)}')