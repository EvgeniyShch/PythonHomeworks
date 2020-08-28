while True :
    try :
        number = int(input("Введите число"))
        if  number>0:
            break
        else:
            print("Введите положительное целое число")
    except :
        print("Введите положительное целое число")

i=1
multiplier = 10

while i < len(str(number)) :
    i+=1
    multiplier *=10

result = number*(multiplier**2) + 2*number*multiplier + 3*number
print("Результат введенного числа N будет представлен в виде суммы N + NN + NNN")
print(f'Сумма чисел {number} и {number*multiplier+number} и {number*(multiplier**2)+number*multiplier+number} будет {result}')