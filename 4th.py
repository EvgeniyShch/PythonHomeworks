while True: #проверка ввода на положительное целое число
    try:
        number = int(input("Введите положительное целое число"))
        if  number>0:
            break
        elif number<=0:
            print("Число должно быть положительным")
    except:
        print("Некорректный ввод. Введите положительное целое число")

i=0
maxnumber = 0
degree = len(str(number))
calculatednumber = number

while i <= len(str(number)) :
    i+=1
    checknumber = calculatednumber // (10**degree)
    calculatednumber = calculatednumber % (10**degree)
    degree-=1
    # print(checknumber, calculatednumber, degree, i, maxnumber)  # для проверки
    if  maxnumber < checknumber :
        maxnumber = checknumber

print(f' Самая большая цифра в числе {number} это {maxnumber}')