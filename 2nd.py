while True:
    try:
        userseconds = int(input("Введите количество секунд"))
        if userseconds>0:
            break
        else :
            print("Некорректный ввод. Введите количество секунд > 0")
    except:
        print("Некорректный ввод. Введите количество секунд")

hours = userseconds//3600
minutes = userseconds%3600//60
seconds = userseconds%3600%60

if hours>24:
    hours=hours%24

usertime ="{}{}:{}{}:{}{}".format(hours//10,hours%10,minutes//10,minutes%10,seconds//10,seconds%10)

print(f"Введенное Вами количество {userseconds} секунд в формате ЧЧ:MM:CC равняется {usertime} ")

print("А ниже будет решение с помощью библиотеки Time")

import time # решение с помощью библиотеки time
#localtime = time.asctime( time.localtime(time.time()) ) - локальное время
usertime2 = time.strftime("%H:%M:%S", time.gmtime(userseconds))
print(f"Введенное Вами количество {userseconds} секунд в формате ЧЧ:MM:CC равняется {usertime2} ")