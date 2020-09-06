from itertools import count, cycle
from random import randint
life_stage = cycle(['Infant', 'Child', 'Teenager', 'Adult', 'Old', 'Rebirth'])

while True:
    try:
        a = int(input("Введите целое число от 1 до 5\n"))
        if a > 0 and a < 5:
            break
        else:
            print("Число должно быть от 1 до 5")
    except ValueError as error1:
        print(f'Ошибка! {error1}')

def gen_iterator(a):
    list1 = []
    limit = 15
    for i in count(a):
        # list1.append([randint(a, limit), next(life_stage)]) - если записывать сразу оба как лист
        list1.append(randint(a, limit))
        list1.append(next(life_stage))
        if i >= limit:
            break
    yield list1

print([i for i in next(gen_iterator(a))])