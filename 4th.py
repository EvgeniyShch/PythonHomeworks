number = int(input("Введите положительное целое число"))

lenghtofnumber = len(str(number))

i=1
maxnumber = 0
degree = lenghtofnumber
calculatednumber = number

while i < lenghtofnumber :
    i+=1
    checknumber = calculatednumber // (10**degree)
    calculatednumber = calculatednumber % (10**degree)
    degree-=1
    if  maxnumber < checknumber :
        maxnumber = checknumber

print(maxnumber)