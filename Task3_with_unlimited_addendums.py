while True :
    try :
        number = int(input("Введите число"))
        if  number>0:
            break
        else:
            print("Введите положительное целое число")
    except :
        print("Введите положительное целое число")

i=0
Addendum=""
Summa=0
while i < number:
    i+=1
    Addendum = Addendum+str(number)
    Summa = Summa + int(Addendum)
    print(f' {i} слагамое {Addendum}')

print(f' Итоговая сумма {Summa}')