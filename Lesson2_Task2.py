while True:
    try:
        countoflist = int(input("Введите количество значений массива"))
        if countoflist > 0:
            break
        else:
            print("Введите целое число > 0")
    except Exception as error:
        print(f' Ошибка! \n {error} \n Введите целое число')
list1 = []
for el in range(countoflist):
    list1.append(input(f'Введите значение {el} элемента массива\n'))
    
print(list1, "- введенный массив")

# решение через цикл while
el=0
while el < countoflist-1:
    list1[el], list1[el+1] = list1[el+1], list1[el]
    el+=2
print(list1, "- измененный массив через цикл while") 
# решение через цикл for 
for el in range(1, countoflist, 2):
    list1[el-1], list1[el] = list1[el], list1[el-1]

print(list1, "- измененный массив через цикл for")