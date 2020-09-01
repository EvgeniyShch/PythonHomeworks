import random
number = random.randint(1,40)
print(f'Число {number}')
list1 = []
for i in range(1, 40, random.randrange(3, 10, 2)):
    list1.append(i)
print(f'Изначальный список {list1}')
list1.sort(reverse=True)
print(f'Отсортированный список {list1}')

for i in list1:
    if number > i:
        list1.insert(list1.index(i),number)
        break
    elif number == i:
        continue
    elif number <= min(list1):
        list1.append(number)
        break
print(f'Отсортированный список с числом {number} по порядку {list1}')