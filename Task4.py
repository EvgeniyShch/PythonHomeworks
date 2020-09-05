def my_func1(num1, num2, *args, **kwargs):
    return num1**num2

def my_func2(num1, num2, *args, **kwargs):
    num3 = 1
    for i in range(abs(num2)):
        num3 *= num1
    return 1/num3

while True:
    try:
        print("Данная программа возведение числа 1 в степень числа 2")
        a = float(input("Введите 1 положительное целое число\n"))
        b = int(input("Введите 2 отрицательное число\n"))
        if a > 0 and b < 0:
            break
        else: 
            print("Введите числа как указано в задании")
    except ValueError as error1:
        print("Аргументы содержат недопустимые значения", error1)
        print("Введите значения еще раз")
        
print(f'Число в степени = {my_func1(a, b)}')
print(f'Число в степени = {my_func2(a, b)}')