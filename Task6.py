result = int(input("Введите результат за 1 день"))
finalresult = int(input("Введите ожидаемый финальный результат"))

#print(type(result)) # тип был int
i = 1
while result < finalresult :
    i+=1
    result*=1.1
# print(type(result)) # тип стал float - динамический язык
print(f'на {i} день спортсмен достиг результата {finalresult} км')