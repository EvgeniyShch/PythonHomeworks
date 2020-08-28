number = int(input("Введите число"))
lenghtofnumber = len(str(number))
print(lenghtofnumber) # для проверки длины

i=1
multiplier = 10

while i < lenghtofnumber :
    i+=1
    multiplier *=10

result = number*(multiplier**2) + 2*number*multiplier + 3*number
print(f' Сумма чисел {number} и {number*multiplier+number} и {number*(multiplier**2)+number*multiplier+number} будет {result}')